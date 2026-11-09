import json
import tempfile
import unittest
from pathlib import Path
from scripts.build_site import build, public_text, render_feed, render_sitemap, valid_image


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

    def test_rss(self):
        feed = render_feed([{"title":"Teste & desenvolvimento","slug":"teste-um","date":"2026-11-09","summary":"Concluído"}])
        self.assertIn("Teste &amp; desenvolvimento", feed)
        self.assertIn("dev.wyoplay.com", feed)

    def test_sitemap(self):
        self.assertIn("https://dev.wyoplay.com/", render_sitemap())

    def test_imagem_falsa(self):
        self.assertFalse(valid_image(b"arquivo-nao-png", ".png"))


if __name__ == "__main__":
    unittest.main()
