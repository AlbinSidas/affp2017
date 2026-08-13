# -*- coding: utf-8 -*-
import json, html, re, importlib.util
src = open('build.py', encoding='utf-8').read()
ns = {}
exec(src, ns)
EX, SV, BLOCKNAME = ns['EX'], ns['SV'], ns['BLOCKNAME']
css = ns['css']
esc = html.escape

CAT = {"GRUND":"Struktur och rutin","A":"A · Föra bollen","B":"B · 1 mot 1",
       "C":"C · Första touch och scanning","D":"D · Passning och understöd",
       "E":"E · Press och försvarsspel","MV":"MV · Målvakt","TEST":"T · Testövningar","SPEL":"G · Spelformer"}
ORDER = ["GRUND","A","B","C","D","E","MV","TEST","SPEL"]

def card(e):
    code,name,blk,area,tim,setup,howto,cps,step = e
    cp="".join(f"<li>{esc(c)}</li>" for c in cps)
    sd=f'<div class="step"><b>Nivåanpassning</b><br>{esc(step)}</div>' if step and step!="—" else ""
    svg = SV.get(code, "")
    fig = f'<div class="ex-fig">{svg}</div>' if svg else ''
    return f'''<article class="ex" id="ex-{code}"><div class="ex-top">{fig}
<div class="ex-body"><span class="ex-code">{esc(code)}</span><h3>{esc(name)}</h3>
<div class="meta">{esc(BLOCKNAME.get(blk,blk))} &nbsp;·&nbsp; {esc(area)} &nbsp;·&nbsp; {esc(tim)}</div>
<p><b>Så sätter du upp det.</b> {esc(setup)}</p>
<p><b>Så gör de.</b> {esc(howto)}</p></div></div>
<div class="cp"><h4>Coachpunkter</h4><ul>{cp}</ul>{sd}</div></article>'''

body=""; toc=""
for k in ORDER:
    items=[e for e in EX if e[2]==k]
    if not items: continue
    body+=f'<section id="cat-{k}"><div class="shead"><span class="num">{esc(k)}</span><h2>{esc(CAT[k])}</h2></div>'
    body+='<div class="exgrid">'+"".join(card(e) for e in items)+'</div></section>'
    toc+=f'<a href="#cat-{k}">{esc(CAT[k])}</a>'

idx="".join(f'<tr><td class="mono"><a href="#ex-{e[0]}">{esc(e[0])}</a></td><td>{esc(e[1])}</td><td>{esc(e[3])}</td><td>{esc(e[4])}</td></tr>' for e in EX)

HTML=f'''<!DOCTYPE html><html lang="sv"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Övningsbank — Åtvidabergs FF</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@400;500;600;700&family=Source+Sans+3:ital,wght@0,400;0,600;0,700;1,400&family=IBM+Plex+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>{css}</style></head><body>
<header class="hero"><div class="wrap">
<div class="eyebrow">Åtvidabergs FF · 02-REFERENS · Version 1.0</div>
<h1>Övnings<em>bank</em></h1>
<div class="sub">Föreningens gemensamma övningar. Varje övning har ett ID som betyder samma sak
i hela klubben, i alla åldrar, i alla år. Säsongsplaner hänvisar hit med kod — de skriver
aldrig av en övning.</div>
<div class="tri">
<div><strong>Hänvisa</strong><span>Skriv A3 i säsongsplanen. Kopiera aldrig texten.</span></div>
<div><strong>Behåll</strong><span>Ett ID återanvänds aldrig, så gamla planer går att läsa.</span></div>
<div><strong>Förbättra</strong><span>Rutan skrivs om, koden står kvar. Alla lag får förbättringen.</span></div>
</div></div></header>
<nav><div class="wrap"><a href="#index">Register</a>{toc}</div></nav>
<div class="wrap">
<section id="index"><div class="shead"><span class="num">00</span><h2>Register</h2></div>
<p class="lede">{len(EX)} övningar. Nya ID tilldelas i november, på förslag från vilken ledare som helst.
Se <span class="mono">_bygg/symboler-och-id.md</span> för konventionerna.</p>
<table><tr><th>ID</th><th>Namn</th><th>Yta</th><th>Tid</th></tr>{idx}</table>
</section>
{body}
<footer><p><b>Övningsbank · Åtvidabergs FF · 03-ovningsbank.html</b><br>
Symbolstandard i _bygg/symboler-och-id.md. Spelidé i 01-sa-spelar-vi.md.<br>
Förslag på nya övningar lämnas till fotbollsutvecklaren. Nya ID tilldelas i november.</p></footer>
</div></body></html>'''
open('../03-ovningsbank.html','w',encoding='utf-8').write(HTML)
print("bank:", len(HTML), "chars |", len(EX), "exercises")
