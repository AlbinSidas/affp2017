# -*- coding: utf-8 -*-
"""
Bygger LAGPARMEN.html — hela lagpärmen i EN fil, gjord för att skrivas ut
eller sparas som PDF (Ctrl+P → Spara som PDF).

Källor: markdownfilerna 01, 02, 08, 05, 06 samt övnings- och passdata ur build.py.
Markdownkonverteringen ligger i md.py och delas med doc.py.

Redigera aldrig LAGPARMEN.html. Redigera källan och kör om skriptet.

    python parm.py
"""
import html
from md import md, inline, shell

esc = html.escape

# ---------------------------------------------------------------- data ur build.py
src = open('build.py', encoding='utf-8').read()
ns = {}
exec(src, ns)

css       = ns['css']
EX        = ns['EX']
S         = ns['S']
ex_card   = ns['ex_card']
ses_card  = ns['ses_card']
keyhtml   = ns['keyhtml']

CAT = {"GRUND": "Struktur och rutin", "A": "A · Föra bollen", "B": "B · 1 mot 1",
       "C": "C · Första touch och scanning", "D": "D · Passning och understöd",
       "E": "E · Press och försvarsspel", "MV": "MV · Målvakt",
       "TEST": "T · Testövningar", "SPEL": "G · Spelformer"}
ORDER = ["GRUND", "A", "B", "C", "D", "E", "MV", "TEST", "SPEL"]

chapters = []   # (num, anchor, title)
parts = []


def add(num, anchor, title, inner):
    chapters.append((num, anchor, title))
    parts.append(f'''<section class="chap" id="{anchor}">
<div class="shead"><span class="num">{num:02d}</span><h2>{esc(title)}</h2></div>
{inner}
</section>''')


def add_md(num, srcfile, anchor, title_override=None):
    raw = open('../' + srcfile, encoding='utf-8').read()
    title, subtitle, lede, body = md(raw)
    title = title_override or title
    head = ''
    if subtitle:
        head += f'<p class="lede">{inline(subtitle)}</p>'
    if lede:
        head += f'<p class="note">{inline(lede)}</p>'
    add(num, anchor, title, head + body)


# ---------------------------------------------------------------- kapitel
add_md(1, '01-sa-spelar-vi.md', 'k1')
add_md(2, '02-sa-tranar-vi.md', 'k2')
add_md(3, '08-arshjul.md', 'k3')

banksec = ('<p class="lede">Samma symboler i alla bilder. Blå anfallare, koppar försvarare, '
           'grön målvakt. Vågig pil = med bollen, streckad = passning, heldragen = löpning utan boll.</p>'
           f'<div class="key">{keyhtml}</div>')
for k in ORDER:
    items = [e for e in EX if e[2] == k]
    if not items:
        continue
    banksec += f'<h3 class="mh2" id="cat-{k}">{esc(CAT[k])}</h3>'
    banksec += '<div class="exgrid">' + ''.join(ex_card(e) for e in items) + '</div>'
add(4, 'k4', 'Övningsbanken', banksec)

sesspart = ('<p class="lede">26 pass, augusti till oktober. Tidslinjen till vänster är passets '
            'ryggrad, kodrutan hänvisar till övningen i kapitel 04. Detta är en plan, inte ett '
            'kontrakt — väder, sjukdom och verkligheten tar tre eller fyra av dem. Komprimera '
            'aldrig för att komma ikapp, fortsätt bara där du är.</p>')
curw = None
for s in S:
    if s['w'] != curw:
        curw = s['w']
        sesspart += f'<div class="wk">Vecka {curw} &nbsp;—&nbsp; Block {esc(s["block"])}</div>'
    sesspart += ses_card(s)
add(5, 'k5', 'Säsongsplan höst 2026', sesspart)

add_md(6, '05-matning-och-utveckling.md', 'k6')
add_md(7, '06-spelarna-och-vuxna.md', 'k7')

# ---------------------------------------------------------------- sidan
toc = ''.join(
    f'<a class="tocrow" href="#{a}"><span class="tocnum">{n:02d}</span>'
    f'<span class="toctitle">{esc(t)}</span></a>' for n, a, t in chapters)
navlinks = ''.join(f'<a href="#{a}">{esc(t)}</a>' for n, a, t in chapters)

intro = f'''<section id="innehall">
<div class="shead"><span class="num">00</span><h2>Innehåll</h2></div>
<p class="lede">Sju kapitel. Behöver du bara en sak inför ett pass är det kapitel 04 —
din egen övning — och kapitel 05, dagens pass.</p>
<div class="toc">{toc}</div>

<div class="call"><h4>Det som betyder mest</h4>
<p><b>1. Bollkontakter.</b> Ingen kö, någonsin. Fler än två som väntar betyder att övningen
är fel upplagd. Fyra små banor slår en stor, varje gång.</p>
<p><b>2. Blicken.</b> Gruppens tydligaste svaghet och den största vinsten. Den kommer av
frågor och av säkrare touch, aldrig av tillsägelser.</p>
<p><b>3. Mod.</b> Ett dribblingsförsök är aldrig ett misstag. Det vi rättar är den säkra
bakåtpassningen, inte den misslyckade dribblingen.</p>
<p><b>4. Att de blir bättre.</b> Träningen finns för att spelarna ska utvecklas som
fotbollsspelare. Ett pass som inte utvecklade någon är ett misslyckat pass, även om alla
hade kul. Frågan efter varje pass: vad kan någon nu som hen inte kunde innan?</p></div>

<div class="call"><h4>Så delar vi upp arbetet</h4>
<p><b>Passvärd</b> — huvudtränaren, varje pass. Sätter koner innan någon kommer, håller
tiden, ropar rotation, avgör när något bryts och tar hand om den som behöver två minuters
paus. Rollen roterar inte.</p>
<p><b>Station</b> — var och en tar en station per pass och behöver bara kunna den. Det är
hela poängen med karusellen: ingen behöver förbereda fem övningar.</p>
<p><b>Observation</b> — en av oss kliver ur coachrollen två minuter per pass och tittar på
en enda spelare, under tystnad. Se kapitel 06.</p></div>
</section>'''

footer = '''<p><b>Lagpärmen · P9 · Åtvidabergs FF · säsongen 2026/27</b><br>
Byggd av <span class="mono">_bygg/parm.py</span> ur källfilerna 01, 02, 08, 05, 06 samt
övnings- och passdata i <span class="mono">_bygg/build.py</span>. Redigera aldrig den här filen —
redigera källan och kör om skriptet.<br>
Bygger på Svenska Fotbollförbundets spelarutbildningsplan och <i>Fotbollens spela, lek och lär</i>,
FIFA 11+ Kids samt klubbens spelidé.</p>
<p style="margin-top:14px">Träningen finns för att spelarna ska bli bättre på fotboll.
I barnfotbollen räknas ingen tabell, alla spelar ungefär lika mycket, alla provar alla
positioner, och ett dribblingsförsök är aldrig ett misstag.</p>
<p style="margin-top:14px;padding-top:12px;border-top:1px solid var(--line)"><b>Skrivet av Albin Sidås</b>, tränare för P9 i Åtvidabergs FF. Materialet är hans eget och är <b>inte Åtvidabergs FF:s officiella träningsmaterial</b> — det uttalar sig inte för föreningen, och andra lag i ÅFF arbetar på sina sätt. Frågor eller något som behöver lyftas: <span class="mono">albinsidas@gmail.com</span></p>
<p style="margin-top:14px">Systerdokument med egna PDF:er:
<span class="mono">09-positionsspel.md</span> (positionsspel från 7 mot 7),
<span class="mono">10-till-er-hemma.md</span> (till vårdnadshavare) och
<span class="mono">07-matguide.html</span> (mat och dryck).</p>'''

HTML = shell(
    title="Lagpärmen — P9, Åtvidabergs FF",
    css=css,
    eyebrow="Åtvidabergs FF · Pojkar 9 år · Säsongen 2026/27 · Version 3.0",
    h1a="Lag", h1b="pärmen",
    sub=(f"Allt vi behöver för att hålla träningen, i ett dokument. Spelidé, passets "
         f"uppbyggnad, årshjulet, {len(EX)} övningar med bild, {len(S)} färdiga pass, mätning "
         f"och utveckling. Skriven för lagets tränare. Skriv ut den eller spara den som PDF "
         f"— det är samma fil."),
    trio=[("Boll", "Vi vill ha bollen. Vi rensar aldrig i första hand."),
          ("Mod", "Vi går 1 mot 1. Att våga och misslyckas är alltid rätt."),
          ("Press", "Tappar vi den tar vi den tillbaka direkt.")],
    body=intro + '\n' + '\n'.join(parts),
    footer=footer,
    nav=navlinks,
)

with open('../LAGPARMEN.html', 'w', encoding='utf-8') as f:
    f.write(HTML)

kb = len(HTML.encode('utf-8')) / 1024
print("parm: %d chars (%.0f kB) | %d kapitel | %d övningar | %d pass"
      % (len(HTML), kb, len(chapters), len(EX), len(S)))
