from diagrams import *
import json
D = json.load(open('svgs.json', encoding='utf-8'))

FOOD = "#3E7D6E"; DRINK = "#2F6DA8"; PLAY = "#1B3A6B"; WARN = "#C4302B"; GOLD = "#B8892B"

def axis(x0, x1, y):
    return (f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="{INK}" stroke-width="2.5"/>')

def tick(x, y, t, sub=""):
    s = f'<line x1="{x}" y1="{y-6}" x2="{x}" y2="{y+6}" stroke="{INK}" stroke-width="2.5"/>'
    s += (f'<text x="{x}" y="{y+24}" font-size="13" font-weight="700" fill="{INK}" '
          f'text-anchor="middle" font-family="IBM Plex Mono, monospace">{t}</text>')
    if sub:
        s += lbl(x, y + 40, sub, 10, GREY, weight=500)
    return s

def chip(x, y, w, h, col, txt, sub="", above=True):
    s = f'<rect x="{x-w/2}" y="{y}" width="{w}" height="{h}" rx="4" fill="{col}"/>'
    s += (f'<text x="{x}" y="{y+19}" font-size="12.5" font-weight="700" fill="#fff" '
          f'text-anchor="middle" font-family="Oswald, sans-serif" letter-spacing="0.5">{txt}</text>')
    if sub:
        for i, ln in enumerate(sub.split("|")):
            s += (f'<text x="{x}" y="{y+36+i*14}" font-size="11" fill="#fff" opacity="0.92" '
                  f'text-anchor="middle" font-family="Source Sans 3, sans-serif">{ln}</text>')
    return s

def drop(x, y, r=9):
    return (f'<path d="M{x},{y-r*1.5} Q{x+r},{y-r*0.2} {x+r*0.72},{y+r*0.45} '
            f'A{r*0.75},{r*0.75} 0 1 1 {x-r*0.72},{y+r*0.45} Q{x-r},{y-r*0.2} {x},{y-r*1.5} z" '
            f'fill="{DRINK}"/>')

# ================= CUPDAGEN =================
s = head(800, 400)
s += lbl(400, 26, "CUPDAGEN", 19, INK, weight=700)
s += lbl(400, 46, "3–4 matcher à 20 minuter", 12, VERD)
Y = 210
s += axis(50, 760, Y)
pts = [(95,"08:00","hemma"),(215,"09:30","första match"),(330,"10:30",""),(445,"11:45",""),(560,"13:00","sista match"),(700,"14:30","hemma")]
for x,t,sub in pts: s += tick(x,Y,t,sub)
s += chip(215, Y-96, 96, 30, PLAY, "MATCH")
s += chip(330, Y-96, 96, 30, PLAY, "MATCH")
s += chip(445, Y-96, 96, 30, PLAY, "MATCH")
s += chip(560, Y-96, 96, 30, PLAY, "MATCH")
s += chip(93, Y-118, 132, 74, FOOD, "REJÄL FRUKOST", "Gröt, mackor, fil|2–3 tim före")
s += chip(700, Y-118, 132, 74, FOOD, "VANLIG MIDDAG", "Inget särskilt.|Bara ordentligt.")
for x in (272, 387, 502):
    s += chip(x, Y+62, 96, 56, GOLD, "LITET", "banan · macka|russin")
s += lbl(387, Y+140, "Små påfyllningar mellan matcherna — aldrig en stor lunch mitt i dagen.", 12, INK)
s += lbl(387, Y+160, "Full mage + 20 minuters match = ont i magen.", 11, WARN)
for x in (215, 272, 330, 387, 445, 502, 560):
    s += drop(x, Y-14)
s += lbl(388, Y-40, "vatten vid varje avbrott", 11, DRINK)
s += lbl(387, 388, "Ta med egen matsäck. Räkna inte med kiosken.", 12, COPPER)
s += tail()
D['MAT1'] = s

# ================= TRÄNINGSDAGEN =================
s = head(800, 420)
s += lbl(400, 26, "TRÄNINGSDAGEN", 19, INK, weight=700)
s += lbl(400, 46, "Träning 17:30 — tisdag 90 min, torsdag 60 min", 12, VERD)
Y = 200
s += axis(50, 760, Y)
for x,t,sub in [(95,"07:00","hemma"),(220,"11:00","skolan"),(395,"15:30","hemma"),(550,"17:30","träning"),(700,"19:30","hemma")]:
    s += tick(x,Y,t,sub)
s += chip(550, Y-90, 160, 28, PLAY, "TRÄNING")
s += chip(95, Y-116, 118, 72, FOOD, "FRUKOST", "Gröt eller|mackor + mjölk")
s += chip(220, Y-116, 118, 72, FOOD, "SKOLLUNCH", "Äter hen upp?|Fråga faktiskt.")
s += chip(700, Y-116, 128, 72, FOOD, "MIDDAG", "Sent, men ändå.|Även en liten.")
s += drop(510, Y-16); s += drop(550, Y-16); s += drop(590, Y-16)
s += lbl(550, Y-38, "flaska med", 10.5, DRINK)
# gap bracket below axis
s += f'<path d="M220,{Y+52} L220,{Y+60} L395,{Y+60} L395,{Y+52}" fill="none" stroke="{WARN}" stroke-width="2.5"/>'
s += lbl(307, Y+78, "4,5 timmar utan mat", 12, WARN, weight=700)
s += lbl(307, Y+95, "efter skollunchen", 10.5, WARN, weight=500)
# mellanmål box
s += f'<rect x="470" y="{Y+52}" width="210" height="96" rx="5" fill="{COPPER}"/>'
s += (f'<text x="575" y="{Y+76}" font-size="15" font-weight="700" fill="#fff" text-anchor="middle" '
      f'font-family="Oswald, sans-serif" letter-spacing="0.6">MELLANMÅLET</text>')
for i, ln in enumerate(["Macka med ost och mjölk.", "Fil, yoghurt, gröt. Frukt.", "Rejält — inte en frukt."]):
    s += f'<text x="575" y="{Y+98+i*16}" font-size="11.5" fill="#fff" text-anchor="middle" font-family="Source Sans 3, sans-serif">{ln}</text>'
s += f'<path d="M395,{Y+64} L462,{Y+90}" stroke="{COPPER}" stroke-width="2.5" marker-end="url(#arc)"/>'
s += lbl(400, Y+178, "Mellanmålet är träningsdagens viktigaste måltid.", 13.5, INK, weight=700)
s += lbl(400, Y+198, "Utan det kommer de tomma till 17:30 — och det syns på sista halvtimmen.", 11, VERD)
s += tail()
D['MAT2'] = s

# ================= MATCHDAGEN =================
s = head(800, 380)
s += lbl(400, 26, "MATCHDAGEN", 19, INK, weight=700)
s += lbl(400, 46, "Nästa år: 7 mot 7, en match per dag", 12, VERD)
Y = 190
s += axis(50, 760, Y)
for x,t,sub in [(110,"3 tim före","huvudmål"),(310,"1–1,5 tim före","litet"),(480,"AVSPARK",""),(660,"efter","hemma")]:
    s += tick(x,Y,t,sub)
s += chip(480, Y-92, 150, 30, PLAY, "MATCH")
s += chip(110, Y-118, 160, 74, FOOD, "HUVUDMÅL", "Pasta, ris, potatis.|Det hen brukar äta.")
s += chip(310, Y-118, 150, 74, GOLD, "LITET", "Banan, macka,|några russin.")
s += chip(660, Y-118, 150, 74, FOOD, "VANLIG MAT", "Inget särskilt|behövs.")
s += lbl(400, Y+72, "En topp i stället för många. Det är hela skillnaden mot cupdagen.", 13, INK, weight=700)
s += lbl(400, Y+94, "Matchen är kortare än en träning. Kroppen har redan det den behöver —", 11, VERD)
s += lbl(400, Y+112, "det handlar bara om att inte komma tom och inte komma proppmätt.", 11, VERD)
s += f'<rect x="150" y="{Y+134}" width="500" height="52" rx="4" fill="none" stroke="{WARN}" stroke-width="2.5"/>'
s += lbl(400, Y+156, "ALDRIG NÅGOT NYTT PÅ MATCHDAGEN", 12.5, WARN, weight=700)
s += lbl(400, Y+174, "Ny mat, ny dryck, nytt tillskott — testa på en träning först, aldrig före match.", 10.5, INK)
for x in (420, 480, 540):
    s += drop(x, Y-14)
s += tail()
D['MAT3'] = s

# ================= MATSÄCKEN =================
s = head(800, 300)
s += lbl(400, 28, "MATSÄCKEN TILL CUPEN", 17, INK, weight=700)
cols = [(140, FOOD, "PÅFYLLNING", ["Bananer", "Mackor med ost", "Russin", "Kex", "Torkad frukt"]),
        (330, DRINK, "DRYCK", ["Vatten, mycket", "Extra flaska", "Mjölk till maten", "— inget mer"]),
        (520, GOLD, "OM DET ÄR LÅNGT", ["Pastasallad", "Matlåda", "Smörgås med", "något matigt"]),
        (700, WARN, "LÅT BLI", ["Sportdryck", "Energidryck", "Godis i stället", "för mat", "Något nytt"])]
for cx, col, head_, items in cols:
    s += f'<rect x="{cx-82}" y="52" width="164" height="30" rx="4" fill="{col}"/>'
    s += (f'<text x="{cx}" y="72" font-size="12.5" font-weight="700" fill="#fff" text-anchor="middle" '
          f'font-family="Oswald, sans-serif" letter-spacing="0.6">{head_}</text>')
    for i, it in enumerate(items):
        s += f'<circle cx="{cx-64}" cy="{102+i*23}" r="3.5" fill="{col}"/>'
        s += lbl(cx - 52, 106 + i * 23, it, 11.5, INK, anchor="start", weight=500)
s += lbl(400, 258, "Godis på cupen är inte problemet. Godis i STÄLLET för mat är problemet.", 12, INK)
s += lbl(400, 278, "En cup är ett kalas. Låt det vara ett kalas — men se till att de äter riktig mat också.", 11, VERD)
s += tail()
D['MAT4'] = s

json.dump(D, open('svgs.json', 'w'))
print("total diagrams:", len(D))
