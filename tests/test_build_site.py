import json
import tempfile
import unittest
from pathlib import Path
from scripts.build_site import build, public_text, render_sitemap, valid_image, PUBLIC_SOURCES, append_activity_post


class PortalBuildTests(unittest.TestCase):
    def test_geracao_estatica(self):
        with tempfile.TemporaryDirectory() as folder:
            out = Path(folder) / "dist"
            build(False, out)
            self.assertTrue((out / "index.html").exists())
            self.assertEqual((out / "CNAME").read_text().strip(), "dev.wyoplay.com")
            data = json.loads((out / "content/site.json").read_text(encoding="utf-8"))
            self.assertGreaterEqual(len(data["projects"]), 5)
            self.assertGreaterEqual(len(data["posts"]), 5)
            self.assertNotIn("github.com", (out / "index.html").read_text())
            self.assertNotIn("github.com", (out / "content/site.json").read_text())

    def test_endereco_privado_proibido(self):
        with self.assertRaises(ValueError):
            public_text("Projeto hospedado em https://github.com/conta/repo")

    def test_sem_rss_ou_referencias_a_repositorios(self):
        with tempfile.TemporaryDirectory() as folder:
            out = Path(folder) / "dist"
            build(False, out)
            self.assertFalse((out / "feed.xml").exists())
            html = (out / "index.html").read_text(encoding="utf-8")
            self.assertNotIn("RSS</a>", html)
            self.assertNotIn("jokersamabr.github.io", html.lower())
            self.assertNotIn("github.com", html.lower())
            self.assertFalse((out / "automation").exists())

    def test_fontes_publicas_autorizadas(self):
        sources = json.loads(PUBLIC_SOURCES.read_text(encoding="utf-8"))["sources"]
        self.assertEqual({x["project_id"] for x in sources}, {"assetstudio", "midgardstudio"})
        self.assertTrue(all(x["visibility"] == "public" for x in sources))

    def test_cartoes_privados_sem_repositorio_exportado(self):
        with tempfile.TemporaryDirectory() as folder:
            out = Path(folder) / "dist"
            build(False, out)
            data = json.loads((out / "content/site.json").read_text(encoding="utf-8"))
            self.assertTrue({"next", "superzip", "emulator"}.issubset({p["id"] for p in data["projects"]}))
            self.assertNotIn("github.com", (out / "content/site.json").read_text(encoding="utf-8"))

    def test_atividade_verificada_nao_inventa_release(self):
        site = {"posts": []}
        project = {"id": "midgardstudio", "title": "Midgard Studio"}
        append_activity_post(site, project, "2026-11-09T20:30:00Z")
        append_activity_post(site, project, "2026-11-09T21:40:00Z")
        self.assertEqual(len(site["posts"]), 1)
        post = site["posts"][0]
        self.assertEqual(post["slug"], "activity-midgardstudio-2026-11-09")
        self.assertEqual(post["publishedAt"], "2026-11-09T20:30:00Z")
        self.assertIn("não significa", post["summary"])
        self.assertNotIn("github.com", json.dumps(post))

    def test_atividade_ignora_data_invalida(self):
        site = {"posts": []}
        append_activity_post(site, {"id": "emulator", "title": "Base protegida"}, "invalid")
        self.assertEqual(site["posts"], [])

    def test_sitemap(self):
        self.assertIn("https://dev.wyoplay.com/", render_sitemap())

    def test_imagem_falsa(self):
        self.assertFalse(valid_image(b"arquivo-nao-png", ".png"))


if __name__ == "__main__":
    unittest.main()
