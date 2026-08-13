# -*- coding: utf-8 -*-
"""
Bygger fristående dokument ur markdown — ett dokument, en html-fil, en PDF.

Används för de dokument som har en egen mottagare och därför inte hör hemma i
lagpärmen: positionsspelet (tränarna) och hemsidan till vårdnadshavarna.

    python doc.py

Diagram läggs in i markdown med en egen rad:

    @fig  KOD | Bildtext | Förklarande mening under bilden

där KOD är en nyckel i pos_svgs.json. Saknas nyckeln byggs dokumentet ändå,
med en tydlig platshållare, så att texten aldrig blockeras av en bild.
"""
import os, json, html, re
from md import md, inline, shell

esc = html.escape

src = open('build.py', encoding='utf-8').read()
ns = {}
exec(src, ns)
css = ns['css']

SVG = {}
if os.path.exists('pos_svgs.json'):
    SVG = json.load(open('pos_svgs.json', encoding='utf-8'))


# ---------------------------------------------------------------- diagram
def extract_figs(text):
    """Byt ut @fig-rader mot tokens. Returnerar (text, [(token, html)])."""
    figs = []

    def repl(m):
        parts = [p.strip() for p in m.group(1).split('|')]
        code = parts[0]
        cap = parts[1] if len(parts) > 1 else ''
        exp = parts[2] if len(parts) > 2 else ''
        svg = SVG.get(code)
        if svg:
            inner = svg
        else:
            inner = (f'<div style="padding:26px;text-align:center;border:1px dashed var(--line);'
                     f'border-radius:3px;color:var(--grey);font-family:monospace;font-size:12px">'
                     f'[diagram {esc(code)} saknas]</div>')
        h = (f'<div class="fig"><div class="cap">{esc(cap)}</div>{inner}'
             + (f'<p class="exp">{inline(exp)}</p>' if exp else '') + '</div>')
        tok = f'FIGTOKEN{len(figs)}ZZ'
        figs.append((tok, h))
        return tok

    text = re.sub(r'^@fig\s+(.+)$', repl, text, flags=re.M)
    return text, figs


def build(srcfile, outfile, title, eyebrow, h1a, h1b, sub, trio, footer):
    raw = open('../' + srcfile, encoding='utf-8').read()
    raw, figs = extract_figs(raw)
    # Titel, underrubrik och ingress sitter redan på omslaget — ta dem inte två gånger.
    _t, _sub, _lede, body = md(raw)

    body = f'<section class="chap nobreak">{body}</section>'
    for tok, h in figs:
        body = body.replace(f'<p>{tok}</p>', h).replace(tok, h)

    HTML = shell(title=title, css=css, eyebrow=eyebrow, h1a=h1a, h1b=h1b,
                 sub=sub, trio=trio, body=body, footer=footer)
    with open('../' + outfile, 'w', encoding='utf-8') as f:
        f.write(HTML)
    missing = len(re.findall(r'\[diagram [A-Z0-9-]+ saknas\]', HTML))
    print("%-28s %6.0f kB | %d diagram%s" % (
        outfile, len(HTML.encode('utf-8')) / 1024, len(figs),
        f" | {missing} SAKNAS" if missing else ""))


# ---------------------------------------------------------------- dokumenten
build(
    '09-positionsspel.md', '09-positionsspel.html',
    title="Positionsspel — från 7 mot 7 och uppåt",
    eyebrow="Åtvidabergs FF · Utbildningsmaterial för tränare · Version 1.0",
    h1a="Positions", h1b="spelet",
    sub=("Hur laget står, varför det står så, och i vilken ordning det lärs ut — från "
         "7 mot 7 till 11 mot 11. Skriven för oss tränare, inte för spelarna. Det här är "
         "den del av utbildningen som är lättast att göra för tidigt och för mycket, "
         "och därför står det lika tydligt vad vi väntar med som vad vi lär ut."),
    trio=[("Bredd", "Planen görs stor när vi har bollen."),
          ("Stöd", "Alltid en vinkel, aldrig en rak linje."),
          ("Press", "Närmast går. Övriga stänger inåt.")],
    footer=('<p><b>Positionsspel · P9 · Åtvidabergs FF</b><br>'
            'Systerdokument till <span class="mono">01-sa-spelar-vi.md</span>, som äger spelidén, '
            'och till lagpärmen, som äger passen. Byggs av <span class="mono">_bygg/doc.py</span> '
            'ur <span class="mono">09-positionsspel.md</span> — redigera aldrig html-filen.</p>'
            '<p style="margin-top:14px;padding-top:12px;border-top:1px solid var(--line)"><b>Skrivet av Albin Sidås</b>, tränare för P9 i Åtvidabergs FF. Materialet är hans eget och är <b>inte Åtvidabergs FF:s officiella träningsmaterial</b> — det uttalar sig inte för föreningen, och andra lag i ÅFF arbetar på sina sätt. Frågor eller något som behöver lyftas: <span class="mono">albinsidas@gmail.com</span></p>'
            '<p style="margin-top:14px">Positionsspel är ett verktyg för att spelarna ska förstå '
            'spelet, aldrig ett skäl att sluta dribbla. Skyddsreglerna i '
            '<span class="mono">01-sa-spelar-vi.md</span> står över allt i det här dokumentet.</p>'),
)

build(
    '10-till-er-hemma.md', '10-till-er-hemma.html',
    title="Till er hemma — P9, Åtvidabergs FF",
    eyebrow="Åtvidabergs FF · Pojkar 9 år · Till vårdnadshavare",
    h1a="Till er ", h1b="hemma",
    sub=("Vad vi vill med träningen, vad ni kan förvänta er av oss, och vad vi behöver "
         "av er och av spelarna för att det ska fungera. Två sidor. Spara den — vi kommer "
         "att hänvisa till den under året i stället för att skicka nya meddelanden."),
    trio=[],
    footer=('<p><b>Till er hemma · P9 · Åtvidabergs FF</b><br>'
            'Gäller tills vi säger något annat och gås igenom på föräldramötet varje säsong. '
            'Har du en fråga om något som står här — ta den med oss direkt, hellre tidigt än sent.</p>'
            '<p style="margin-top:14px;padding-top:12px;border-top:1px solid var(--line)"><b>Skrivet av Albin Sidås</b>, tränare för P9 i Åtvidabergs FF. Materialet är hans eget och är <b>inte Åtvidabergs FF:s officiella träningsmaterial</b> — det uttalar sig inte för föreningen, och andra lag i ÅFF arbetar på sina sätt. Frågor eller något som behöver lyftas: <span class="mono">albinsidas@gmail.com</span></p>'
            '<p style="margin-top:14px">Mat och dryck runt träning, match och cup står i '
            'matguiden, som är ett eget blad.</p>'),
)
