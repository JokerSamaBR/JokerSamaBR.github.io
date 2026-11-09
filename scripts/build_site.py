#!/usr/bin/env python3
"""Gerador do portal: exporta exclusivamente manifestos públicos com opt-in."""
import argparse
import base64
import json
import os
import re
import shutil
from datetime import datetime, time, timezone
from email.utils import format_datetime
from pathlib import Path, PurePosixPath
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[1]
SITE_URL = "https://dev.wyoplay.com"
ALLOWED_URLS = {"", "https://www.wyoplay.com/", "https://digital.wyoplay.com/"}
CATEGORIES = {"Projeto", "Ferramentas", "Engenharia", "Atualizações"}
MANIFEST = "docs/PUBLIC_SHOWCASE.json"
IMAGE_DIR = "docs/public-showcase/images/"
MAX_IMAGE_BYTES = 4 * 1024 * 1024
IMAGE_TYPES = {".png", ".jpg", ".jpeg", ".webp"}
SLUG = re.compile(r"^[a-z][a-z0-9-]{1,70}$")
FORBIDDEN_LINK = re.compile(r"https?://|www\.|github\.com|raw\.githubusercontent\.com", re.I)


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def public_text(s, max_len=350):
    if not isinstance(s, str) or not 0 < len(s.strip()) <= max_len:
        raise ValueError("texto público inválido")
    if FORBIDDEN_LINK.search(s):
        raise ValueError("manifesto contém URL externa ou endereço GitHub")
    return s.strip()


def public_date(s):
    if not isinstance(s, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", s):
        raise ValueError("data inválida")
    datetime.strptime(s, "%Y-%m-%d")
    return s


def github_json(url, token=""):
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "WYO-Public-Showcase"}
    if token:
        headers["Authorization"] = "Bearer " + token
    try:
        with urlopen(Request(url, headers=headers), timeout=20) as response:
            return json.load(response)
    except HTTPError as exc:
        if exc.code == 404:
            return None
        raise RuntimeError("Falha na API GitHub (HTTP " + str(exc.code) + ")") from None


def github_file(repo, path, token):
    url = "https://api.github.com/repos/" + repo + "/contents/" + quote(path, safe="/")
    data = github_json(url, token)
    if data is None or data.get("type") != "file":
        return None
    if data.get("encoding") != "base64":
        raise ValueError("resposta de arquivo inválida")
    raw = base64.b64decode(data["content"])
    if len(raw) > MAX_IMAGE_BYTES:
        raise ValueError("arquivo maior que limite de 4 MiB")
    return raw


def valid_image(data, ext):
    return (ext == ".png" and data.startswith(b"\x89PNG\r\n\x1a\n")
            or ext in {".jpg", ".jpeg"} and data.startswith(b"\xff\xd8\xff")
            or ext == ".webp" and data[:4] == b"RIFF" and data[8:12] == b"WEBP")


def sync_source(source, site, dist, token=""):
    pid = source["project_id"]
    project = next((p for p in site["projects"] if p["id"] == pid), None)
    if project is None:
        raise ValueError("projeto não cadastrado: " + pid)
    repo = source["repository"]
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repo):
        raise ValueError("repositório inválido")
    if source["visibility"] == "private" and not token:
        print("SKIP " + pid + ": falta token restrito para fontes privadas")
        return
    auth = token if source["visibility"] == "private" else os.getenv("GITHUB_TOKEN", "")
    if source["visibility"] == "public":
        response = github_json("https://api.github.com/repos/" + repo + "/commits?per_page=1", auth)
        if isinstance(response, list) and response:
            project["lastActivity"] = response[0]["commit"]["committer"]["date"]
    raw = github_file(repo, MANIFEST, auth)
    if raw is None:
        print("SKIP " + pid + ": manifesto público ausente")
        return
    if len(raw) > 128 * 1024:
        raise ValueError("manifesto grande demais")
    m = json.loads(raw.decode("utf-8"))
    if m.get("publish") is not True or m.get("project_id") != pid:
        print("SKIP " + pid + ": publicação não autorizada")
        return
    for key in ("description", "status"):
        if key in m:
            project[key] = public_text(m[key], 550 if key == "description" else 90)
    image_paths = []
    for src in m.get("images", [])[:5]:
        if not isinstance(src, str):
            raise ValueError("caminho de imagem inválido")
        path = PurePosixPath(src)
        if not src.startswith(IMAGE_DIR) or ".." in path.parts or path.suffix.lower() not in IMAGE_TYPES:
            raise ValueError("imagem não permitida: deve ficar em docs/public-showcase/images/")
        raw_image = github_file(repo, src, auth)
        if raw_image is None or not valid_image(raw_image, path.suffix.lower()):
            raise ValueError("imagem inválida ou ausente")
        local = dist / "assets" / "demos" / pid / path.name
        local.parent.mkdir(parents=True, exist_ok=True)
        local.write_bytes(raw_image)
        image_paths.append("/" + local.relative_to(dist).as_posix())
    if image_paths:
        project["images"] = image_paths
    seen = {p["slug"] for p in site["posts"]}
    for entry in m.get("updates", [])[:20]:
        slug = entry.get("slug")
        if not isinstance(slug, str) or not SLUG.fullmatch(slug) or slug in seen:
            continue
        category = entry.get("category", "Atualizações")
        if category not in CATEGORIES:
            category = "Atualizações"
        post = {
            "slug": slug,
            "title": public_text(entry.get("title"), 120),
            "date": public_date(entry.get("date")),
            "category": category,
            "project": project["title"],
            "summary": public_text(entry.get("summary"), 350),
            "sections": [],
        }
        for s in entry.get("sections", [])[:8]:
            section = {"title": public_text(s.get("title"), 120)}
            if s.get("body"):
                section["body"] = public_text(s["body"], 1200)
            if s.get("bullets"):
                section["bullets"] = [public_text(x, 240) for x in s["bullets"][:12]]
            post["sections"].append(section)
        if image_paths:
            post["images"] = image_paths
        site["posts"].append(post)
        seen.add(slug)
    print("OK " + pid + ": conteúdo público aprovado importado")


def render_sitemap():
    return ('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
            '<url><loc>' + SITE_URL + '/</loc></url><url><loc>' + SITE_URL +
            '/post.html</loc></url></urlset>\n')


def build(remote=False, out=None):
    out = Path(out) if out else ROOT / "dist"
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    for name in ("index.html", "post.html", "CNAME", ".nojekyll"):
        shutil.copy2(ROOT / name, out / name)
    shutil.copytree(ROOT / "assets", out / "assets")
    (out / "content").mkdir()
    site = read_json(ROOT / "content" / "site.json")
    for p in site["projects"]:
        if p.get("url", "") not in ALLOWED_URLS:
            p["url"] = ""
        p["images"] = [img for img in p.get("images", [])
                       if isinstance(img, str) and img.startswith("/assets/demos/")
                       and (out / img.lstrip("/")).is_file()]
    if remote:
        token = os.getenv("WYO_PUBLIC_FEED_READ_TOKEN", "")
        source_config = os.getenv("WYO_PUBLIC_SOURCES_JSON", "").strip()
        if source_config:
            try:
                sources = json.loads(source_config)
                if not isinstance(sources, dict) or not isinstance(sources.get("sources"), list):
                    raise ValueError("estrutura inválida no segredo de fontes")
            except (ValueError, json.JSONDecodeError) as exc:
                raise ValueError("WYO_PUBLIC_SOURCES_JSON inválido") from exc
            for src in sources["sources"]:
                if not isinstance(src, dict) or not isinstance(src.get("project_id"), str):
                    raise ValueError("origem sem identificador válido")
                try:
                    sync_source(src, site, out, token)
                except (ValueError, RuntimeError, URLError, json.JSONDecodeError) as exc:
                    print("AVISO " + src["project_id"] + ": não sincronizado (" + type(exc).__name__ + ")")
        else:
            print("SKIP: nenhuma origem configurada; segredos não fornecidos")
    for p in site["projects"]:
        p.pop("repository", None)
        p.pop("source", None)
    (out / "content" / "site.json").write_text(json.dumps(site, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (out / "sitemap.xml").write_text(render_sitemap(), encoding="utf-8")
    (out / "robots.txt").write_text("User-agent: *\nAllow: /\nSitemap: " + SITE_URL + "/sitemap.xml\n", encoding="utf-8")
    print("OK: " + str(len(site["projects"])) + " projetos e " + str(len(site["posts"])) + " artigos")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--remote", action="store_true")
    parser.add_argument("--output", default=str(ROOT / "dist"))
    args = parser.parse_args()
    build(args.remote, Path(args.output).resolve())
