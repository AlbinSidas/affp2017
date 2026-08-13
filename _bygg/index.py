# -*- coding: utf-8 -*-
"""
Bygger index.html — landningssidan för GitHub Pages.

Den länkar bara till HTML och PDF, aldrig till markdownfilerna. Skälet är att
GitHub Pages serverar .md som råtext, vilket ser trasigt ut för en förälder som
klickar. Allt innehåll i markdownfilerna finns ändå publicerat: tränarmaterialet
i sin helhet i LAGPARMEN.html.

    python index.py
"""
import io, os, html
from md import EXTRA_CSS, FONTS

esc = html.escape

src = open('build.py', encoding='utf-8').read()
ns = {}
exec(src, ns)
css = ns['css']
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def card(href, kicker, title, text, meta):
    finns = os.path.exists(os.path.join(ROOT, href))
    warn = '' if finns else '<div class="saknas">filen är inte byggd än</div>'
    return f'''<a class="kort" href="{esc(href)}">
<div class="kicker">{esc(kicker)}</div>
<h3>{esc(title)}</h3>
<p>{esc(text)}</p>
<div class="meta">{esc(meta)}</div>{warn}</a>'''


TRANARE = [
    card('LAGPARMEN.html', 'Allt i ett', 'Lagpärmen',
         'Spelidé, passets uppbyggnad, årshjulet, 42 övningar med bild, 26 färdiga pass '
         'och hur vi mäter om träningen fungerar. Hela tränarmaterialet i ett dokument.',
         'Webb · även som PDF'),
    card('09-positionsspel.html', 'Utbildning', 'Positionsspelet',
         'Hur laget står och varför, från 7 mot 7 och uppåt. Principerna i inlärningsordning, '
         'tio övningar och en färdighetstrappa.',
         'Webb · även som PDF'),
    card('11-metoden.html', 'Resonemang', 'Metoden',
         'Varför övningarna ser ut som de gör, varför periodiseringen är uppbyggd som den '
         'är, hur nästa säsong planeras, och hur metoden bär upp genom 9 mot 9 och 11 mot 11.',
         'Webb · även som PDF'),
    card('03-ovningsbank.html', 'Referens', 'Övningsbanken',
         '42 övningar med diagram, uppställning, coachpunkter och nivåanpassning. '
         'Varje övning har ett ID som betyder samma sak för alltid.',
         'Webb'),
    card('04-sasongsplan-host-2026.html', 'Säsong', 'Säsongsplanen',
         '26 pass från augusti till oktober, med tidslinje för varje pass och kod till '
         'varje övning.',
         'Webb · hösten 2026'),
]

HEMMA = [
    card('10-till-er-hemma.html', 'Till er hemma', 'Vad vi lovar, och vad vi behöver',
         'Vad vi vill med träningen, vad ni kan förvänta er av oss, och vad vi behöver av '
         'er och av spelarna för att det ska fungera.',
         'Webb · även som PDF'),
    card('07-matguide.html', 'Mat och dryck', 'Matguiden',
         'Mellanmål före träning, mat på cupdagen, dryck. Infografik att spara i telefonen.',
         'Webb · även som PDF'),
]

PDF = [
    ('Lagparmen.pdf', 'Lagpärmen', 'Tränare'),
    ('Positionsspel.pdf', 'Positionsspelet', 'Tränare'),
    ('Metoden.pdf', 'Metoden', 'Tränare'),
    ('Till-er-hemma.pdf', 'Till er hemma', 'Vårdnadshavare'),
    ('Matguide.pdf', 'Matguiden', 'Vårdnadshavare'),
]

pdfrader = ''.join(
    '<tr><td><a href="%s">%s</a></td><td>%s</td><td class="mono">%s</td></tr>'
    % (f, namn, till, ('%.1f MB' % (os.path.getsize(os.path.join(ROOT, f)) / 1048576))
       if os.path.exists(os.path.join(ROOT, f)) else '—')
    for f, namn, till in PDF)

EXTRA = """
.kortgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:16px;margin:8px 0 34px}
.kort{display:block;background:var(--card);border:1px solid var(--line);border-radius:4px;
  padding:20px 22px 18px;text-decoration:none;color:var(--ink);transition:border-color .12s}
.kort:hover{border-color:var(--copper)}
.kort .kicker{font-family:'IBM Plex Mono',monospace;font-size:10.5px;letter-spacing:.16em;
  text-transform:uppercase;color:var(--copper);font-weight:700;margin-bottom:8px}
.kort h3{font-size:25px;text-transform:uppercase;font-weight:600;margin-bottom:7px;color:var(--blue)}
.kort p{font-size:15px;margin:0 0 12px;color:#3A4340;line-height:1.5}
.kort .meta{font-family:'IBM Plex Mono',monospace;font-size:11px;letter-spacing:.1em;color:var(--grey)}
.kort .saknas{margin-top:8px;font-family:'IBM Plex Mono',monospace;font-size:11px;color:var(--copper)}
.fyra{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:14px;margin:6px 0 30px}
.fyra div{background:var(--card);border:1px solid var(--line);border-left:4px solid var(--copper);
  border-radius:0 4px 4px 0;padding:15px 17px}
.fyra strong{display:block;font-family:'Oswald',sans-serif;font-size:19px;text-transform:uppercase;
  letter-spacing:.02em;color:var(--blue);margin-bottom:5px}
.fyra span{font-size:14.5px;color:#3A4340;line-height:1.45}
"""

HTML = f'''<!DOCTYPE html>
<html lang="sv"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>P9 — Åtvidabergs FF</title>
<meta name="description" content="Träningsmaterialet för ett barnfotbollslag. Spelidé, övningar, säsongsplan och riktlinjer — öppet för alla att läsa och använda.">
{FONTS}
<style>{css}{EXTRA_CSS}{EXTRA}</style></head><body>

<header class="cover"><div class="wrap">
<div class="eyebrow">Åtvidabergs FF · Pojkar födda 2017</div>
<h1>P<em>9</em></h1>
<div class="sub">Hela träningsmaterialet för ett barnfotbollslag — spelidén, övningarna,
säsongsplanen och vad vi lovar spelarna och deras familjer. Ingenting här är hemligt.
Det är så vi vill arbeta, och det tål att läsas av vem som helst.</div>
</div></header>

<div class="wrap">

<section id="tranare">
<div class="shead"><span class="num">01</span><h2>För tränare</h2></div>
<p class="lede">Behöver du bara en sak: läs lagpärmen. Allt annat finns i den.</p>
<div class="kortgrid">{''.join(TRANARE)}</div>
</section>

<section id="hemma">
<div class="shead"><span class="num">02</span><h2>För vårdnadshavare</h2></div>
<p class="lede">Två blad. Det andra är mest bilder.</p>
<div class="kortgrid">{''.join(HEMMA)}</div>
</section>

<section id="grunden">
<div class="shead"><span class="num">03</span><h2>Det materialet vilar på</h2></div>
<div class="fyra">
<div><strong>Bollkontakter</strong><span>Ingen kö, någonsin. Fyra små banor slår en stor, varje gång.</span></div>
<div><strong>Blicken</strong><span>Att titta innan man får bollen. Den kommer av frågor, aldrig av tillsägelser.</span></div>
<div><strong>Mod</strong><span>Ett dribblingsförsök är aldrig ett misstag. Det vi rättar är den säkra bakåtpassningen.</span></div>
<div><strong>Att de blir bättre</strong><span>Ett pass som inte utvecklade någon är ett misslyckat pass, även om alla hade kul.</span></div>
</div>

<div class="call"><h4>Och det materialet aldrig gör</h4>
<p>Ingen toppning och ingen tabellräkning — alla spelar ungefär lika mycket. Ingen
permanent nivåindelning, ingen selektering, inga fasta positioner. Ingen fast målvakt före
tolv år. Inga test som rangordnar barn. Inga namn på enskilda spelare någonstans i
materialet. Aldrig kommentarer om ett barns kropp eller vikt.</p>
<p>Det följer svensk barnfotbolls värdegrund och Svenska Fotbollförbundets riktlinjer för
åldrarna 8–12, och det står över allt annat i materialet.</p></div>
</section>

<section id="pdf">
<div class="shead"><span class="num">04</span><h2>Att skriva ut</h2></div>
<p class="lede">Fem PDF:er, byggda ur samma källor som webbsidorna. Alla går att mejla
eller lägga i lagchatten som de är.</p>
<table>
<tr><th>Fil</th><th>Till vem</th><th>Storlek</th></tr>
{pdfrader}
</table>
</section>

<section id="anvand">
<div class="shead"><span class="num">05</span><h2>Ta det och gör det till ert</h2></div>
<p class="lede">Materialet är skrivet för ett lag, men nästan ingenting i det är unikt för
just det laget.</p>
<p style="max-width:74ch">Övningsbanken, årshjulet, mätningen och föräldrabrevet fungerar
för vilken årskull som helst — det är datum, spelform och truppstorlek som behöver bytas.
Är du tränare i ÅFF eller någon annanstans: kopiera, ändra och gör om det så att det
passar er.</p>
<p style="max-width:74ch">Materialet är licensierat under <b>CC BY-SA 4.0</b>. Använd det
fritt, även kommersiellt, så länge du anger varifrån det kommer och delar vidare under
samma licens.</p>
<div class="call"><h4>En regel värd att behålla om du bygger vidare</h4>
<p><b>Övnings-ID är fasta för alltid.</b> <span class="mono">A3</span> är Grindar, i varje
dokument och varje år. Ett ID återanvänds aldrig, så gamla säsongsplaner går fortfarande
att läsa, och förbättras en övning skrivs rutan om medan koden står kvar.</p>
<p>Det är den regeln som gör att flera lag kan prata om samma övning utan att missförstå
varandra.</p></div>
</section>

<footer>
<p><b>P9 · Åtvidabergs FF</b><br>
Bygger på Svenska Fotbollförbundets spelarutbildningsplan och <i>Fotbollens spela, lek och
lär</i>, samt FIFA 11+ Kids.<br>
Sidorna byggs ur källfilerna med <span class="mono">_bygg/bygg-allt.py</span>. Redigera
aldrig en genererad fil för hand.</p>
<div class="call" style="margin-top:6px"><h4>Vem som står bakom materialet</h4>
<p>Materialet är skrivet och ägs av <b>Albin Sidås</b>, tränare för P9 i Åtvidabergs FF.</p>
<p><b>Det här är inte Åtvidabergs FF:s officiella träningsmaterial.</b> Det uttalar sig inte
för föreningen, för styrelsen eller för andra lag. Andra lag i ÅFF arbetar på sina sätt, och
ingenting här ska läsas som att klubben tillämpar eller har godkänt det som står här.</p>
<p>Det beskriver hur <b>ett</b> lag har valt att arbeta. Det är skrivet för att rymmas innanför
Svenska Fotbollförbundets riktlinjer för barnfotboll — men urvalet, tolkningarna och
avvägningarna är mina egna, och jag svarar för dem.</p>
<p>Frågor, invändningar eller något som behöver lyftas — hör av dig direkt:
<b><span class="mono">albinsidas@gmail.com</span></b></p></div>

<p style="margin-top:14px">Träningen finns för att spelarna ska bli bättre på fotboll.
I barnfotbollen räknas ingen tabell, alla spelar ungefär lika mycket, alla provar flera
positioner, och ett dribblingsförsök är aldrig ett misstag.</p>
</footer>

</div></body></html>'''

with io.open(os.path.join(ROOT, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(HTML)
print("index: %.0f kB" % (len(HTML.encode('utf-8')) / 1024))
