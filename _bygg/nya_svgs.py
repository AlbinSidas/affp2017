# -*- coding: utf-8 -*-
"""
Ritar diagrammen till de nya övningarna D1–D6 och E1–E4 (skrivs till svgs.json)
och till positionsspelsdokumentet (skrivs till pos_svgs.json).

    python nya_svgs.py

Symbolkonventionerna är bindande, se symboler-och-id.md: blå = anfallare/vårt lag,
koppar = försvarare/motståndare, grön = målvakt, vågig pil = med bollen,
streckad = passning, heldragen = löpning utan boll.
"""
import json, os
from diagrams import *

D = json.load(open('svgs.json', encoding='utf-8')) if os.path.exists('svgs.json') else {}
P = json.load(open('pos_svgs.json', encoding='utf-8')) if os.path.exists('pos_svgs.json') else {}


def wrap(body, w=400, h=300):
    return head(w, h) + body + tail()


# ================================================================ D-övningar
# D1 · Rondo 5 mot 2
s = field(70, 55, 260, 190)
s += dim(70, 45, "12 × 12 m  ·  5 mot 2")
for x, y in [(90, 75), (310, 75), (330, 200), (200, 235), (70, 175)]:
    s += player(x, y)
s += player(175, 130, COPPER) + player(235, 165, COPPER)
s += pas(103, 79, 296, 75)
s += pas(315, 90, 328, 185)
s += ball(103, 88)
s += lbl(200, 275, "Flytta dig innan du får bollen. Aldrig rak linje.", 12)
D['D1'] = wrap(s)

# D2 · Öppen kropp
s = field(30, 60, 340, 155)
s += dim(30, 50, "12 × 12 m  ·  tre spelare")
s += player(80, 140, BLUE, "A") + player(200, 140, BLUE, "B") + player(320, 95, BLUE, "C")
s += pas(93, 140, 186, 140)
s += pas(212, 133, 307, 99)
s += run(200, 118, 200, 96, VERD)
s += lbl(200, 88, "halvvänd", 11, VERD)
s += ball(120, 152)
s += lbl(200, 245, "B tar emot med kroppen öppen mot planen", 12)
s += lbl(200, 263, "och spelar vidare i samma rörelse.", 12)
D['D2'] = wrap(s)

# D3 · Trianglar
s = field(40, 45, 320, 200)
s += dim(40, 35, "20 × 20 m  ·  sex spelare")
pts = [(95, 90), (215, 70), (320, 120), (270, 210), (150, 215), (70, 165)]
for x, y in pts:
    s += player(x, y)
for a, b in [(0, 1), (1, 2), (2, 0)]:
    s += line(pts[a][0], pts[a][1], pts[b][0], pts[b][1], COPPER, 2, "5 4")
s += pas(108, 88, 202, 73)
s += ball(95, 101)
s += lbl(200, 275, "Efter din passning: bilda en triangel med bollen", 12)
D['D3'] = wrap(s)

# D4 · Spel med kantzoner
s = field(30, 45, 340, 200)
s += dashbox(30, 45, 340, 34) + dashbox(30, 211, 340, 34)
s += dim(30, 35, "30 × 25 m  ·  4 mot 4  ·  zoner 3 m")
s += goal(24, 122, 46, vertical=True) + goal(370, 122, 46, vertical=True)
for x, y in [(120, 155), (185, 120), (250, 175), (150, 62)]:
    s += player(x, y)
for x, y in [(160, 190), (230, 110), (290, 150)]:
    s += player(x, y, COPPER)
s += pas(133, 152, 148, 76)
s += run(163, 62, 250, 62)
s += ball(133, 165)
s += lbl(200, 275, "Bara anfallande lag i zonerna. Mål därifrån räknas dubbelt.", 12)
D['D4'] = wrap(s)

# D5 · Spela ut bakifrån
s = field(30, 45, 340, 200)
s += dim(30, 35, "Halv 7-mannaplan  ·  5 mot 3 + mv")
s += goal(24, 122, 46, vertical=True)
s += line(255, 45, 255, 245, COPPER, 2, "7 5")
s += lbl(255, 262, "över linjen med kontroll", 11, COPPER)
s += player(62, 145, VERD, "1")
s += player(110, 70, BLUE, "2") + player(110, 220, BLUE, "3")
s += player(170, 145, BLUE, "6")
s += player(215, 95, BLUE, "9")
for x, y in [(160, 95), (150, 195), (205, 145)]:
    s += player(x, y, COPPER)
s += pas(75, 140, 100, 78)
s += ball(80, 152)
s += lbl(200, 282, "Brett och lågt först. Är sexan täckt går bollen till en back.", 12)
D['D5'] = wrap(s)

# D6 · Fyra mål, två färger
s = field(45, 45, 310, 200)
s += dim(45, 35, "25 × 25 m  ·  4 mot 4  ·  fyra konmål")
for x, y in [(60, 60), (340, 60), (60, 230), (340, 230)]:
    s += cone(x - 14, y) + cone(x + 14, y)
for x, y in [(140, 110), (215, 160), (170, 205)]:
    s += player(x, y)
for x, y in [(255, 105), (235, 195), (130, 165)]:
    s += player(x, y, COPPER)
s += pas(152, 108, 240, 72)
s += ball(150, 121)
s += lbl(200, 275, "Tätt vid ett mål betyder öppet vid ett annat.", 12)
D['D6'] = wrap(s)

# ================================================================ E-övningar
# E1 · Närmast går
s = field(50, 45, 300, 200)
s += dim(50, 35, "20 × 20 m  ·  3 mot 3")
s += goal(44, 122, 44, vertical=True) + goal(350, 122, 44, vertical=True)
s += player(215, 130, COPPER)
s += player(160, 130, BLUE) + player(150, 200, BLUE) + player(190, 70, BLUE)
s += ball(228, 138)
s += run(173, 130, 200, 130)
s += run(158, 192, 185, 165, GREY)
s += run(196, 82, 208, 105, GREY)
s += lbl(120, 118, "närmast går", 11, INK)
s += lbl(200, 275, "Framme innan tränaren räknat till tre. Räkna högt.", 12)
D['E1'] = wrap(s)

# E2 · Två som samarbetar
s = field(50, 55, 300, 175)
s += dim(50, 45, "18 × 14 m  ·  2 mot 2")
s += goal(44, 122, 44, vertical=True) + goal(350, 122, 44, vertical=True)
s += player(255, 120, COPPER) + player(280, 195, COPPER)
s += player(205, 120, BLUE) + player(155, 160, BLUE)
s += ball(268, 128)
s += run(218, 120, 240, 120)
s += line(155, 160, 255, 120, VERD, 2, "5 4")
s += lbl(150, 140, "täcker", 11, VERD)
s += lbl(205, 103, "pressar", 11, INK)
s += lbl(200, 262, "Den bakre ska se både bollen och sin kompis.", 12)
D['E2'] = wrap(s)

# E3 · Styr mot linjen
s = field(40, 60, 320, 165)
s += dim(40, 42, "25 × 18 m  ·  1 mot 1")
s += goal(34, 120, 44, vertical=True)
s += line(40, 62, 360, 62, COPPER, 3)
s += lbl(200, 82, "sidlinjen är en försvarare gratis", 11, COPPER)
s += player(265, 160, COPPER)
s += player(215, 135, BLUE)
s += dribble(255, 152, 175, 90, COPPER)
s += ball(252, 170)
s += lbl(200, 250, "Kom snett. Kroppen bestämmer riktningen före fötterna.", 12)
D['E3'] = wrap(s)

# E4 · Fem sekunder
s = field(30, 45, 340, 200)
s += dim(30, 35, "30 × 25 m  ·  4 mot 4 + två jokrar")
s += goal(24, 122, 46, vertical=True) + goal(370, 122, 46, vertical=True)
s += player(140, 145, BLUE)
s += player(230, 110, BLUE) + player(250, 190, BLUE)
s += player(175, 100, COPPER) + player(185, 195, COPPER)
s += ball(153, 152)
s += run(153, 145, 218, 115)
s += run(263, 190, 340, 160)
s += lbl(285, 92, "10 sek = dubbelt", 11, COPPER)
s += lbl(200, 275, "Mål inom tio sekunder räknas dubbelt. Bollen tillbaka", 12)
s += lbl(200, 291, "inom fem sekunder ger en poäng.", 12)
D['E4'] = wrap(s)

# ================================================================ positionsspel
# 2-3-1 i 7 mot 7
s = field(25, 40, 350, 220)
s += line(200, 44, 200, 256, FIELDLINE, 1.5)
s += goal(19, 128, 44, vertical=True) + goal(375, 128, 44, vertical=True)
s += player(55, 150, VERD, "1")
s += player(115, 78, BLUE, "2") + player(115, 222, BLUE, "3")
s += player(160, 150, BLUE, "6")
s += player(245, 66, BLUE, "7") + player(245, 234, BLUE, "11")
s += player(255, 150, BLUE, "9")
s += dim(25, 30, "7 mot 7  ·  2-3-1")
s += lbl(200, 285, "Sexan bakom bollen. Sjuan och elvan ute vid linjerna.", 12)
P['231'] = wrap(s)

# Tre korridorer
s = field(25, 40, 350, 220)
s += line(25, 113, 375, 113, COPPER, 2, "7 5")
s += line(25, 187, 375, 187, COPPER, 2, "7 5")
s += goal(19, 128, 44, vertical=True) + goal(375, 128, 44, vertical=True)
s += lbl(34, 80, "höger", 11, COPPER, "start")
s += lbl(34, 155, "mitten", 11, COPPER, "start")
s += lbl(34, 228, "vänster", 11, COPPER, "start")
s += player(110, 75, BLUE) + player(245, 70, BLUE)
s += player(150, 150, BLUE) + player(255, 145, BLUE)
s += player(120, 222, BLUE) + player(250, 225, BLUE)
s += dim(25, 30, "Aldrig fler än två av oss i samma korridor")
s += lbl(200, 285, "Lösningen på bikupan. Den går att räkna från sidlinjen.", 12)
P['korridorer'] = wrap(s)

# Triangel, aldrig linje
s = lbl(105, 34, "FEL — rak linje", 13, COPPER)
s += lbl(300, 34, "RÄTT — triangel", 13, VERD)
s += field(20, 45, 170, 175)
s += player(50, 130, BLUE) + player(120, 130, COPPER) + player(170, 130, BLUE)
s += line(50, 130, 170, 130, COPPER, 2, "4 4")
s += ball(50, 146)
s += lbl(105, 200, "en försvarare täcker båda", 11, COPPER)
s += field(215, 45, 170, 175)
s += player(245, 130, BLUE) + player(305, 130, COPPER) + player(355, 80, BLUE)
s += pas(258, 126, 344, 86)
s += ball(245, 146)
s += lbl(300, 200, "försvararen måste välja", 11, VERD)
s += lbl(200, 262, "Kan du dra ett rakt streck genom dig, bollen och en", 12)
s += lbl(200, 279, "motståndare — flytta dig två meter i sidled.", 12)
P['triangel'] = wrap(s, 400, 300)

# Press och täckning
s = field(25, 45, 350, 200)
s += player(255, 120, COPPER)
s += ball(268, 128)
s += player(200, 120, BLUE)
s += run(213, 120, 238, 120)
s += player(150, 165, BLUE)
s += line(150, 165, 250, 122, VERD, 2, "5 4")
s += player(135, 95, BLUE)
s += run(148, 100, 178, 112, GREY)
s += lbl(200, 103, "U1 närmast går", 11, INK)
s += lbl(140, 188, "U2 täcker bakom", 11, VERD)
s += dim(25, 35, "Press och täckning")
s += lbl(200, 272, "En går. En står bakom. Aldrig två på samma boll.", 12)
P['press'] = wrap(s)

# Uppspelsmönstret
s = field(25, 40, 350, 220)
s += goal(19, 128, 44, vertical=True)
s += player(60, 150, VERD, "1")
s += player(105, 62, BLUE, "2") + player(105, 238, BLUE, "3")
s += player(165, 150, BLUE, "6")
s += player(175, 105, COPPER) + player(170, 200, COPPER) + player(230, 150, COPPER)
s += pas(73, 143, 92, 72)
s += pas(105, 75, 152, 140)
s += run(118, 62, 175, 62)
s += ball(78, 158)
s += lbl(300, 100, "1  brett och lågt", 12, INK, "start")
s += lbl(300, 122, "2  sexan om fri", 12, INK, "start")
s += lbl(300, 144, "3  öppen kropp", 12, INK, "start")
s += lbl(300, 166, "4  annars tillbaka", 12, INK, "start")
s += dim(25, 30, "Uppspelsmönstret i 7 mot 7")
P['uppspel'] = wrap(s)

json.dump(D, open('svgs.json', 'w', encoding='utf-8'), ensure_ascii=False)
json.dump(P, open('pos_svgs.json', 'w', encoding='utf-8'), ensure_ascii=False)
print("svgs.json: %d nycklar | pos_svgs.json: %d nycklar" % (len(D), len(P)))
