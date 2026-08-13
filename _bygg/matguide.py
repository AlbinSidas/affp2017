# -*- coding: utf-8 -*-
import json, html
SV = json.load(open('svgs.json', encoding='utf-8'))
src = open('build.py', encoding='utf-8').read(); ns = {}
exec(src[:src.index('# ---------------------------------------------------------------- sessions')] +
     src[src.index('css = """'):src.index('def ex_card(e):')], ns)
css = ns['css']
esc = html.escape

extra = """
.fig{background:var(--sand);border:1px solid var(--line);border-radius:4px;
  padding:16px;margin:18px 0}
.fig svg{width:100%;height:auto;display:block}
.big{font-family:'Oswald',sans-serif;font-size:clamp(20px,3vw,27px);text-transform:uppercase;
  font-weight:600;color:var(--blue);margin:34px 0 6px;letter-spacing:.01em}
.rule{border:0;border-top:1px solid var(--line);margin:34px 0}
.rank{counter-reset:r;list-style:none;padding:0;margin:14px 0}
.rank li{counter-increment:r;position:relative;padding:14px 0 14px 58px;
  border-top:1px solid var(--line);font-size:16.5px}
.rank li:last-child{border-bottom:1px solid var(--line)}
.rank li::before{content:counter(r);position:absolute;left:0;top:12px;
  font-family:'Oswald',sans-serif;font-size:26px;font-weight:600;color:var(--copper);
  line-height:1}
.rank b{display:block;font-family:'Oswald',sans-serif;text-transform:uppercase;
  font-size:18px;font-weight:500;letter-spacing:.02em;color:var(--ink);margin-bottom:2px}
.warn{border-left:4px solid #C4302B;background:#FDF4F3}
.warn h4{color:#C4302B}
"""

HTML = f'''<!DOCTYPE html><html lang="sv"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Mat och dryck — Åtvidabergs FF</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@400;500;600;700&family=Source+Sans+3:ital,wght@0,400;0,600;0,700;1,400&family=IBM+Plex+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>{css}{extra}</style></head><body>

<header class="hero"><div class="wrap">
<div class="eyebrow">Åtvidabergs FF · 02-REFERENS · För ledare och vårdnadshavare</div>
<h1>Mat och <em>dryck</em></h1>
<div class="sub">Barnfotboll, 8–12 år. Tre situationer: cupdagen, träningsdagen och matchdagen.
Det här är inte idrottsnutrition. Det handlar om att barnen har ätit tillräckligt
och druckit tillräckligt — inget mer avancerat än så.</div>
<div class="tri">
<div><strong>Tillräckligt</strong><span>De flesta problem är att barnet ätit för lite, inte fel.</span></div>
<div><strong>Vanlig mat</strong><span>Inga tillskott, ingen sportdryck, inga specialprodukter.</span></div>
<div><strong>Matglädje</strong><span>Aldrig prat om vikt. Aldrig mat som belöning eller straff.</span></div>
</div></div></header>

<nav><div class="wrap">
<a href="#viktigast">Det viktigaste</a>
<a href="#traning">Träningsdagen</a>
<a href="#cup">Cupdagen</a>
<a href="#match">Matchdagen</a>
<a href="#dryck">Dryck</a>
<a href="#granser">Gränser</a>
</div></nav>

<div class="wrap">

<section id="viktigast"><div class="shead"><span class="num">01</span><h2>Det viktigaste, i ordning</h2></div>
<p class="lede">Om ni bara orkar med en sak, ta den första. Den löser mer än de andra tillsammans.</p>
<ol class="rank">
<li><b>Mellanmål efter skolan</b>Skollunchen ligger runt elva. Träningen börjar 17:30. Det är fyra och en halv timme utan mat, efter en hel skoldag. Ett rejält mellanmål vid tre–fyra är den enskilt viktigaste måltiden på en träningsdag — och den som oftast missas.</li>
<li><b>Vatten, och en egen flaska</b>Barn dricker sällan tillräckligt av sig själva. De känner inte törst lika tydligt som vuxna och de glömmer bort det när det är roligt. Flaska med till varje träning, drick i varje paus — inte bara när någon säger till.</li>
<li><b>Ät något efter kvällsträning</b>De kommer hem vid halv åtta. Det känns sent, och frestelsen är att hoppa över. Låt bli att hoppa över. Även en macka och ett glas mjölk är bättre än ingenting — det påverkar både sömnen och nästa dag.</li>
<li><b>Frukost varje dag</b>Trivialt, men det är den vanligaste orsaken till att ett barn är slut redan på skollunchen.</li>
<li><b>Inget nytt på matchdagen</b>Ny mat, ny dryck, något man aldrig testat. Testa på en vanlig träning i stället.</li>
</ol>
<div class="call"><h4>Och det här är inte på listan</h4>
<p>Proteinpulver, sportdryck, energidryck, kosttillskott, återhämtningsdrycker,
kolhydratsuppladdning. Inget av det hör hemma hos en nioåring, och det finns inget
stöd för att det skulle hjälpa i den här åldern.</p>
<p>Det mesta som skrivs om idrottsnutrition är skrivet för tonåringar eller vuxna elitidrottare.
Det går inte att skala ner till barn — det ska helt enkelt inte tillämpas alls.</p></div>
</section>

<section id="traning"><div class="shead"><span class="num">02</span><h2>Träningsdagen</h2></div>
<p class="lede">Träning 17:30. Tisdag 90 minuter, torsdag 60 minuter. Skillnaden mellan
de två passen spelar mindre roll än man tror — det är luckan efter skolan som avgör hur
kvällen blir.</p>
<div class="fig">{SV['MAT2']}</div>

<div class="two">
<div class="call"><h4>Mellanmålet ska vara ett mål, inte en frukt</h4>
<p>En banan räcker inte till ett barn som ska träna i nittio minuter. Macka med ost eller
smör och pålägg, fil eller yoghurt med flingor, gröt, en smörgås till. Plus frukt om de vill.</p>
<p>Praktiskt: ha det klart hemma, eller skicka med i väskan om barnet går på fritids.</p></div>
<div class="call"><h4>Middagen blir sen — och det är okej</h4>
<p>Hemma vid 19:15, mat vid halv åtta. Det är senare än man vill, men det fungerar
förutsatt att mellanmålet var ordentligt.</p>
<p>Är barnet för trött för att äta: en macka, ett glas mjölk, lite fil. Något är alltid
bättre än inget.</p></div>
</div>

<div class="call"><h4>Frågan som säger mest</h4>
<p>Fråga barnet <b>om det åt upp skollunchen</b>, inte om det åt lunch. Många barn äter
väldigt lite i skolmatsalen — det är stökigt, kort om tid, eller så var det något de inte
gillade. Ett barn som inte åt lunch och inte fick mellanmål har i praktiken varit utan
mat sedan frukosten.</p></div>
</section>

<section id="cup"><div class="shead"><span class="num">03</span><h2>Cupdagen</h2></div>
<p class="lede">Tre till fyra matcher à tjugo minuter, utspridda över en dag. Den svåraste
situationen — inte för att det är avancerat, utan för att dagen är lång och det är lätt
att ingen äter ordentligt.</p>
<div class="fig">{SV['MAT1']}</div>

<div class="call"><h4>Regeln för cupdagen: smått och ofta</h4>
<p>Tjugo minuters match kräver ingenting särskilt under tiden. Det som behövs är att
barnet inte blir tommare för varje match. Alltså: <b>små påfyllningar mellan matcherna
i stället för en stor lunch mitt på dagen.</b></p>
<p>En stor måltid en timme före avspark ger ont i magen. En hel dag utan mat ger ett barn
som är gnälligt, okoncentrerat och tråkigt att vara med redan i match tre. Mitten emellan
är banan, mackan och russinen.</p></div>

<div class="fig">{SV['MAT4']}</div>

<div class="call"><h4>Om godiset</h4>
<p>En cup är ett kalas. Det ska den få vara, och godis är inte problemet.</p>
<p>Problemet är godis <b>i stället för</b> mat — vilket är precis vad som händer när ingen
tagit med något annat och kiosken är det enda alternativet. Ta med egen matsäck, så löser
det sig av sig självt.</p></div>
</section>

<section id="match"><div class="shead"><span class="num">04</span><h2>Matchdagen — nästa år</h2></div>
<p class="lede">Från 7 mot 7 blir det oftast en match per dag i stället för fyra.
Det gör saken enklare, inte svårare.</p>
<div class="fig">{SV['MAT3']}</div>

<div class="two">
<div class="call"><h4>Vad som ändras från cupdagen</h4>
<p>En topp i stället för många. Man behöver inte hushålla med energin över en hel dag —
det räcker med ett ordentligt mål tre timmar före och något litet en timme före.</p>
<p>Matchen är dessutom kortare än en träning. Kroppen har redan det den behöver.</p></div>
<div class="call"><h4>Tidig avspark</h4>
<p>Match klockan nio betyder inte att man ska upp klockan sex och äta. Ät frukost som vanligt,
lite tidigare, och ta något litet på vägen. Sömn slår måltidstiming.</p></div>
</div>
</section>

<section id="dryck"><div class="shead"><span class="num">05</span><h2>Dryck</h2></div>
<p class="lede">Kortaste avsnittet i dokumentet, för att svaret är kort.</p>
<div class="call"><h4>Vatten. Det är hela svaret.</h4>
<p>Amerikanska barnläkarföreningen är tydlig: vatten ska vara barns huvudsakliga
vätskekälla före, under och efter fysisk aktivitet. Sportdryck är i regel onödigt för barn
i vanlig idrottsaktivitet, och avråds uttryckligen efter korta träningar och matcher.
Tumregeln som brukar anges är att sportdryck kan ha en roll först vid aktivitet över en
timme i stark värme — vilket inte beskriver en oktoberkväll i Åtvidaberg.</p>
<p><b>Energidryck hör inte hemma i barns och ungdomars kost över huvud taget.</b>
Det är inte en avvägning, det är ett nej.</p>
<p>Mjölk till maten är bra. Saft och läsk är kalas, inte vätskeersättning.</p></div>

<div class="call"><h4>Det verkliga problemet är inte vad de dricker</h4>
<p>Det är att de inte dricker. Barn dricker sällan tillräckligt frivilligt under aktivitet,
och att vara törstig är redan ett tecken på att man börjat bli uttorkad.</p>
<p>Praktiskt för ledare: <b>lägg in en drickapaus i varje pass, även när ingen bett om det.</b>
Fem sekunder efter varje station i karusellen räcker. På cupdagar: drick vid varje avbrott,
inte bara efter matcherna.</p></div>
</section>

<section id="granser"><div class="shead"><span class="num">06</span><h2>Gränser — det som gäller alla vuxna runt laget</h2></div>
<p class="lede">Den här delen är viktigare än allt annat i dokumentet. Den handlar inte om
prestation utan om att inte göra skada.</p>

<div class="call warn"><h4>Aldrig, av någon vuxen, i något sammanhang</h4>
<p><b>Kommentera aldrig ett barns vikt, kropp eller kroppsform.</b> Inte uppmuntrande,
inte skämtsamt, inte "bara som ett konstaterande". Inte till barnet, inte till en annan
vuxen inom hörhåll.</p>
<p><b>Begränsa aldrig ett barns mat för att förbättra prestation.</b> Nioåringar växer.
Att äta för lite är ett långt större problem i den här åldern än att äta för mycket.</p>
<p><b>Dela aldrig in mat i bra och dålig.</b> Mat är mat. Moraliserande språk kring
mat i barnidrott hänger ihop med problem senare, och vinsten på planen är noll.</p>
<p><b>Använd aldrig mat som belöning eller straff.</b> Inte glass för att man vann,
inte indraget fika för att man skötte sig dåligt.</p></div>

<div class="call"><h4>Om du som ledare blir orolig för ett barns ätande</h4>
<p>Om ett barn regelbundet inte äter, pratar nedsättande om sin kropp, eller där något
annat känns fel — <b>ta det inte med barnet.</b></p>
<p>Ta ett lugnt, enskilt samtal med vårdnadshavare, formulerat som en observation
och inte som en diagnos. Är oron större än så är rätt väg skolsköterska eller
vårdcentral, inte fotbollsklubben. Vi är fotbollsledare och det är en gräns värd
att hålla.</p></div>

<div class="call"><h4>Vad vi faktiskt vill uppnå</h4>
<p>Livsmedelsverket beskriver vårdnadshavarens uppdrag i två delar: att barnet får
näringsriktig mat, och att barnet får bra matvanor och <b>matglädje</b>.</p>
<p>Den andra delen är den vi som förening lättast förstör och sällan förbättrar.
Ett barn som lämnar fotbollen med ett avslappnat förhållande till mat har fått
något mer värt än några procents bättre uthållighet i en cup.</p></div>
</section>

<footer><p><b>Mat och dryck · Åtvidabergs FF · 07-matguide.html</b><br>
Ledarnas version med bakgrund finns i 06-spelarna-och-vuxna.md.
Åtaganden kring barns hälsa och bemötande i 06-spelarna-och-vuxna.md.</p>
<p style="margin-top:14px">Underlag: Livsmedelsverkets kostråd för barn 2–17 år · American Academy of Pediatrics,
klinisk rapport om sport- och energidrycker för barn och ungdomar · AAP:s riktlinjer om
vätska och värme vid barnidrott.</p>
<p style="margin-top:14px"><b>Det här är allmän vägledning för friska barn i lagidrott.
Har ett barn en sjukdom, allergi, specialkost eller något annat som påverkar ätandet
gäller det som sjukvården sagt — inte det här dokumentet.</b></p></footer>
</div></body></html>'''

open('../07-matguide.html','w',encoding='utf-8').write(HTML)
print("matguide:", len(HTML), "chars")
