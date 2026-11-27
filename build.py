"""Baut index.html aus kapitel/*.md und template.html.

Format je Kapitel:  ## <Nummer> | <Titel>, Absätze durch Leerzeilen getrennt,
letzter Absatz beginnt mit **Ermittlerfrage:**
"""
import glob, json, re, pathlib

root = pathlib.Path(__file__).parent
chapters = []
for f in sorted(glob.glob(str(root / "kapitel" / "*.md"))):
    for part in re.split(r"^## ", pathlib.Path(f).read_text(encoding="utf-8"), flags=re.M)[1:]:
        head, body = part.split("\n", 1)
        n, title = [x.strip() for x in head.split("|", 1)]
        paras = [p.strip() for p in body.strip().split("\n\n") if p.strip()]
        q = paras.pop()
        assert q.startswith("**Ermittlerfrage:**"), f"Kapitel {n}: Ermittlerfrage fehlt"
        chapters.append({"n": int(n), "t": title, "p": paras,
                         "q": q.replace("**Ermittlerfrage:**", "").strip()})
assert [c["n"] for c in chapters] == list(range(1, 25)), "Es müssen genau die Kapitel 1–24 sein"
data = json.dumps(chapters, ensure_ascii=False).replace("</", "<\\/")
html = (root / "template.html").read_text(encoding="utf-8").replace("__DATA__", data)
(root / "index.html").write_text(html, encoding="utf-8")
for c in chapters:
    print(c["n"], c["t"], len(" ".join(c["p"]).split()), "Wörter")
