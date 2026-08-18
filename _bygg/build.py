# -*- coding: utf-8 -*-
import json, html

SV = json.load(open('svgs.json', encoding='utf-8'))

# ---------------------------------------------------------------- exercises
EX = [
("ANK","Ankomstaktivitet — boll var","GRUND","Egen yta, bort från stora målet","10–15 min",
 "Markera en ankomstyta med koner INNAN någon kommer, och lägg den så att stora målet ligger utanför. Sätt ut sex konmål utspridda i ytan, gärna vända åt olika håll. En boll per spelare.",
 "Rullande start — det börjar med den som kommer först. Uppgiften är enkel och sägs en gång i augusti, sedan aldrig mer: gör mål i så många OLIKA konmål du hinner. Samma mål två gånger i rad räknas inte.",
 ["Problemet är kön, inte skjutandet. Tio spelare vid ett mål ger en bollkontakt var trettionde sekund. Sex mål ger noll kö och tvingar fram förflyttning med boll mellan varje avslut.",
  "Slå inte ihjäl skjutandet — mångfaldiga målen i stället. Att skjuta är det roligaste de vet, och det ska få vara kvar. Det är avståndet mellan målen som blir bollkontakterna.",
  "Ett mål är en magnet. Ligger stora målet inne i ytan hamnar de där, oavsett vad du säger. Flytta ytan i stället för att tjata.",
  "Ställ dig själv i ankomstytan. Tränaren är också en magnet.",
  "Kräv i övrigt ingenting. Den som hellre bara dribblar runt gör det. Den som busar med en boll får ändå tvåhundra kontakter."],
 "Variant när de tröttnar: TULL PÅ SKOTTET — du får skjuta, men först efter tre grindar. Behåller belöningen, lägger ett pris på den. Fungerar också bra veckan före cup."),

("A1","Färgvästen","A","20 × 20 m","6–8 min",
 "Alla i rutan med varsin boll. Tränaren står utanför med tre västar: gul, blå, grå.",
 "Tränaren håller upp en väst. GUL = för bollen snabbt in i ytan. BLÅ = långsamt, nära foten. GRÅ = stanna med sulan. Ingen ropar något — spelarna måste titta upp för att se vilken väst som hålls upp.",
 ["Att inget ropas är hela poängen. Den som har huvudet nere missar bytet.",
  "MOD: gult betyder verkligen snabbt. Beröm den som vågar accelerera.",
  "Håll upp två västar samtidigt när de börjat fatta — då måste de välja.",
  "Byt västhand ibland så att de tittar på västen och inte på var du står."],
 "Krymp rutan för att göra det svårare. Bara svag fot för den som vill ha en utmaning."),

("A2","Kungen av banan","A","18 × 18 m","6–8 min",
 "Alla i rutan med varsin boll.",
 "Skydda din egen boll samtidigt som du slår ut andras. Blir din boll utsparkad: fem sulrullningar utanför rutan, sen in igen.",
 ["Enorm bollkontaktvolym och de tror att det är en lek. Det är hela poängen.",
  "MOD: den som bara gömmer sig i hörnet skyddar men vågar inte. Skicka in dem.",
  "Var inte domare. De löser det själva."],
 "De två starkaste får bara använda svag fot, eller bara skydda med en arm."),

("A3","Grindar","A","25 × 20 m, 10 grindar","6–8 min",
 "Tio grindar av koner utspridda slumpmässigt, olika breda.",
 "Hur många grindar hinner du dribbla igenom på 60 sekunder? Skriv upp siffran. Slå ditt eget rekord nästa gång.",
 ["Tävling mot sig själv, inte mot varandra. Avgörande för de fyra–fem som ligger efter.",
  "Samma grind två gånger i rad räknas inte — tvingar dem att lyfta huvudet och välja.",
  "Skriv upp siffrorna. De kommer fråga efter dem."],
 "Olika breda grindar — spelaren väljer själv vilka hen tar. Detta är autonomispaken."),

("A4","Hajar och små fiskar","A","25 × 18 m","6–8 min",
 "Alla med boll på ena kortsidan. Två hajar utan boll i mitten.",
 "Ta dig över till andra sidan med bollen. Tappar du din boll blir du haj.",
 ["MOD: den som väntar på att någon annan ska gå först — skicka iväg dem först nästa omgång.",
  "Fartförändring är svaret, inte finter. Peka på den som saktar in och drar iväg.",
  "Kör många korta omgångar, inte få långa."],
 "Smalare kanal = svårare. Den som vill ha det svårare kan starta som haj."),

("A5","Mållinjespel","A","30 × 20 m, 3 mot 3","8–10 min",
 "Målzon markerad på båda kortsidorna.",
 "Poäng genom att FÖRA bollen över motståndarens linje under kontroll. Passning över linjen räknas inte.",
 ["Regeln gör hela jobbet. Du behöver knappt coacha.",
  "BOLL + MOD i en övning: de måste behålla bollen och de måste gå framåt med den.",
  "Låt dem spela. Max en frysning."],
 "Bredare zon = lättare. Smalare = svårare."),

("B1","Fintstationen","B","3 rutor · 6 × 6 m","10–12 min",
 "Tre små rutor bredvid varandra, en kon i mitten av varje. En finta per ruta. Spelaren väljer själv vilken ruta hen börjar i och byter när hen vill.",
 "Tre steg i varje ruta: först mot konen, sedan mot en passiv försvarare som står stilla med armarna i kors, sist mot en levande försvarare. Alla behöver inte nå steg tre.",
 ["Valet är poängen. Tvinga ingen till en viss finta eller ett visst steg.",
  "Fintan ska göras i FART. En finta på stället lurar ingen. Kräv att de går igenom efteråt.",
  "MOD: beröm försöket varje gång, oavsett hur det går.",
  "Låt dem hitta på en egen och döpa den. Du får en Pizzavändning. De gör den 400 gånger."],
 "Steg tre är valfritt. Passiv försvarare räcker långt och bygger självförtroende."),

("B2","1 mot 1 till två mål","B","20 × 14 m","10–12 min",
 "Två små mål bredvid varandra på ena kortsidan.",
 "Anfallare mot försvarare. Anfallaren får göra mål i vilket som av de två målen. Löpande, max två i kö.",
 ["Två mål tvingar försvararen att välja sida — det är där finter blir meningsfulla.",
  "MOD: den som lägger tillbaka istället för att gå — det är felet vi rättar. Inte den misslyckade dribblingen.",
  "Byt anfallare/försvarare varannan gång."],
 "STEP: större yta = lättare för anfallaren. De två starkaste försvarar 2 mot 1."),

("B3","1 mot 1 från rullad boll","B","18 × 14 m","8–10 min",
 "Ett mål. Två spelare i led, en på varje sida om dig.",
 "Du rullar in bollen. Båda springer. Den som kommer först anfaller, den andra försvarar.",
 ["Kaotiskt och de älskar det. Tränar övergångsögonblicket utan att du behöver förklara det.",
  "Variera rullningen — ibland närmare den ena.",
  "Säg nästan ingenting. Bara rulla nästa boll."],
 "Rulla närmare den svagare spelaren så hen får bollen oftare."),

("B4","3 mot 3 med bonuspoäng","B","30 × 20 m","15–20 min",
 "Två små mål. Tre lag som roterar.",
 "Mål = 1 poäng. Mål efter en övervunnen motståndare = 3 poäng.",
 ["Detta är blockets viktigaste övning. Regeln bygger MOD in i spelet.",
  "Räkna högt när någon får 3. De kommer jaga det.",
  "BOLL: rensa räknas aldrig som en lösning. Påminn en gång, sen låt vara."],
 "Bara svag fot för den som vill ha en utmaning. En extra touch i eget område för den som behöver mer tid."),

("B5","Styra anfallaren","B","15 × 20 m","8–10 min",
 "En yta med ett mål i ena änden och en kon i vardera hörnet vid mittlinjen. Anfallaren startar med boll mot målet. Försvararen startar framför målet.",
 "Anfallaren ska ta sig till mål. Försvararen vinner om anfallaren i stället hamnar ute vid någon av konerna — eller om anfallaren stannar av. Försvararen behöver alltså inte vinna bollen för att lyckas.",
 ["SNETT, INTE RAKT. Kommer försvararen rakt framifrån är båda vägarna öppna. Kommer hen snett från ena sidan är den vägen redan stängd och anfallaren tvingas åt andra hållet. Det här är den viktigaste punkten.",
  "SNABBT FRAM, SEDAN BROMSA. Spring de första metrarna för att stänga ytan, sakta sedan ner de sista. Kommer man i full fart hela vägen blir man passerad av första touchen.",
  "HALVÖPPEN KROPP. Stå med ena foten och axeln framåt, inte med bröstet rakt mot anfallaren. Fyrkantig kropp betyder att man måste vända helt för att följa med — och då är man redan slagen.",
  "EN ARMLÄNGD. Nära nog att kunna nå bollen om anfallaren tappar den, långt nog att hinna reagera. Står man för nära blir man passerad, för långt bort får anfallaren fritt fram.",
  "FÖLJ MED, TACKLA INTE. Att fördröja är en vinst. Tacklingen kommer bara när bollen ligger löst — och gör den inte det, fortsätt bara följa med."],
 "Steg 1: anfallaren går i gångfart, försvararen övar bara ställning och vinkel. Steg 2: halvfart. Steg 3: fullt. Bredare yta gynnar anfallaren, smalare gynnar försvararen."),

("C1","Nummer bakom","C","Par, 8 m mellan","8–10 min",
 "Två och två. En boll per par.",
 "A passar till B. Innan bollen kommer fram håller A upp fingrar bakom sig. B måste säga siffran INNAN bollen når fram.",
 ["Vändningen på huvudet är hela poängen. Siffran är bara ett skäl att vända den.",
  "Coachord hela blocket: TITTA INNAN DU FÅR DEN.",
  "Om de tittar för sent — passa långsammare först, snabba upp sen."],
 "Långsammare passning för den som behöver mer tid. Två siffror för den som vill ha det svårare."),

("C2","Touch genom grind","C","Par + två grindar","10–12 min",
 "Två grindar, en snett framåt vänster och en snett framåt höger om mottagaren, cirka två meter bort. Tränaren står bakom mottagaren.",
 "Partnern passar. Mottagarens första touch ska gå genom en av grindarna. Vilken avgörs av tränaren bakom — och det går bara att veta genom att titta över axeln medan bollen är på väg.",
 ["Skillnaden mellan att STOPPA bollen och att ta den NÅGONSTANS. Det är hela C-blocket i en övning.",
  "Titten ska ske medan bollen rullar, inte efter att den kommit fram. Fråga: när tittade du?",
  "Öppen kropp innan bollen kommer — halvvänd redan när den är på väg.",
  "Byt vilken grind som är närmast varannan omgång så att båda fötterna används."],
 "NIVÅ 1: en enda grind, ingen tränare bakom. Bara touchen. NIVÅ 2: två grindar, tränaren pekar med armen innan passningen slås. NIVÅ 3: tränaren går och ställer sig vid en av grindarna först när bollen lämnat passarens fot — spelaren måste titta sent och ändå hinna välja den andra. Nivå 3 är svår. Ta den bara med dem som klarat nivå 2 tryggt."),

("C3","Fyra mål","C","25 × 20 m, 3 mot 3","15–20 min",
 "Fyra små mål, två på varje kortsida.",
 "Vanligt 3 mot 3, men två mål att välja mellan i varje riktning.",
 ["Bästa scanningsspelet som finns i den här åldern. Huvudet måste upp för att se vilket mål som är öppet.",
  "Fråga efter mål: vilket mål var öppet? De vet oftast.",
  "MOD gäller fortfarande — de får gå förbi någon på vägen."],
 "Ett tredje mål i mitten för det svagare laget om det behövs."),

("C4","Vänd och gå","C","20 × 16 m","8–10 min",
 "Ett mål. Inspelare med boll, mottagare med ryggen mot mål.",
 "Ta emot med ryggen mot mål, vänd, för bollen mot mål och avsluta.",
 ["Titta över axeln INNAN bollen kommer. Fråga: vem stod bakom dig?",
  "Öppen kropp — halvvänd redan när bollen är på väg.",
  "Detta är förberedelsen för 7 mot 7 nästa år. Säg det till dem."],
 "Lägg till en passiv försvarare bakom för den som vill ha det svårare."),

("C5","Huvudet uppe","C","20 × 15 m","6–8 min",
 "Alla med varsin boll i rutan. En tränare rör sig runt inne i ytan.",
 "Spelarna för bollen fritt. Tränaren håller upp fingrar med jämna mellanrum — den som ser ropar siffran. Tränaren flyttar sig hela tiden så att det inte går att lära sig var hen står.",
 ["Blicken UNDER förflyttning, inte mellan. Det är svårare än det låter och det är precis det som saknas i match.",
  "Går det trögt: sänk farten först. Kontroll före blick, alltid.",
  "Den som aldrig ser siffran har troligen en touch som kräver att hen tittar ner. Då är det A-blocket som är svaret, inte fler tillsägelser.",
  "Byt till färger eller handtecken när siffror blivit för lätt."],
 "Större yta och långsammare tempo för den som behöver mer tid. Två tränare som visar samtidigt för den som vill ha det svårare."),

("C6","Frågan före","C","3 mot 1 i ruta","8–10 min",
 "Tre spelare i en ruta mot en försvarare. Byt försvarare varje minut.",
 "Vanligt håll-bollen-spel, men innan varje passning ställer tränaren en fråga högt till mottagaren: \u0022Var står den fria?\u0022 eller \u0022Hur många är bakom dig?\u0022. Frågan ställs FÖRE passningen.",
 ["Blicken följer en fråga, aldrig en tillsägelse. Titta upp betyder ingenting för ett barn — det finns inget att titta efter.",
  "Frågan före situationen. Ställs den efteråt är det ett förhör och de slutar svara.",
  "Rätt svar är mindre viktigt än att huvudet vred sig. Beröm vridningen.",
  "Efter ett par veckor: sluta ställa frågan högt och se om de tittar ändå. Det är hela testet."],
 "Fyra mot en för den som tycker det är svårt. Två försvarare för den som tycker det är lätt."),

("D1","Rondo 5 mot 2","D","Ruta 12 × 12 m","5 min",
 "Fem spelare runt om rutan, två i mitten. En boll. Körs varje pass från 7 mot 7 och uppåt.",
 "Håll bollen. Ingen räkning, inga poäng — bara bollen som rullar. BYT DE TVÅ I MITTEN PÅ TID, var fyrtiofemte sekund, aldrig på misstag.",
 ["Understödsvinkeln är hela poängen. Kan man dra ett rakt streck genom dig, bollen och en motståndare står du fel — flytta dig två meter i sidled.",
  "Flytta dig INNAN du får bollen, inte efter. Det är samma färdighet som blicken, med fötterna.",
  "En touch när du kan, två när du måste. Aldrig som regel — som ambition.",
  "Byter man på misstag hamnar samma två barn i mitten varje vecka, inför alla. Då blir rondon det de tycker sämst om i stället för det passet börjar med. Byt på tid.",
  "Tolv meter, inte åtta. Fem meter mellan spelarna gör det till en reaktionsövning där den svagare halvan aldrig får en ren touch."],
 "Större ruta och fri touch för den som tycker det är svårt. Mindre ruta och max två touch för den som tycker det är lätt."),

("D2","Öppen kropp","D","12 × 12 m, tre per grupp","8–10 min",
 "Tre spelare: A på ena sidan, B i mitten, C bakom B. En boll.",
 "A passar till B. B ska ta emot HALVVÄND — kroppen öppen mot planen — och spela vidare till C. Byt plats efter fem bollar.",
 ["Titta över axeln innan bollen kommer. Den som tittar först när bollen är framme har redan förlorat tid.",
  "Ta emot med den bortre foten. Då tar första touchen dig runt i stället för att stoppa bollen.",
  "Det här är C-blocket med en passning i slutet. Säg det till spelarna — de gillar att känna igen sig.",
  "Kroppen ska öppnas innan bollen kommer, inte medan den rullar."],
 "Lägg till en passiv försvarare bakom B. Aktiv försvarare som får bryta för den som vill ha det svårare — fråga vem som vill, peka aldrig ut."),

("D3","Trianglar","D","20 × 20 m, sex spelare","8–10 min",
 "Sex spelare i en ruta, en boll. Inga mål.",
 "Passa och rör dig. Enda regeln: efter din passning ska du flytta dig så att du bildar en triangel med bollen och en lagkamrat. Ingen får stå still efter en passning.",
 ["Passa och gå. Aldrig passa och titta — det är det vanligaste felet och det syns direkt.",
  "Den som står stilla är osynlig. Säg det en gång, sedan räcker det att peka.",
  "Räkna trianglar högt i tio sekunder om de tappar idén. Sluta räkna när den är tillbaka.",
  "Från elva–tolv år kan tredje mannen introduceras här: bollen går vidare direkt till den som redan är i rörelse."],
 "Lägg in en försvarare när det flyter. Sedan två. Fler spelare gör det lättare, färre svårare."),

("D4","Spel med kantzoner","D","30 × 25 m, 4 mot 4","12–15 min",
 "Vanlig bana med en zon på cirka tre meter längs varje sidlinje, markerad med koner.",
 "Vanligt spel, men i sidzonerna får bara det anfallande laget vara. Mål räknas dubbelt om anfallet gick genom en zon.",
 ["Regeln gör jobbet. Säg ingenting om bredd — den kommer av sig själv när det lönar sig att stå där.",
  "Den som springer in i zonen får vara ensam där. Det är hela belöningen och den räcker.",
  "Detta är M1 och M6 i samma övning: gör planen stor, och vänd spelet när det är stängt.",
  "Blir det stopp i zonen: påminn om att man får dribbla ut ur den. Zonen är en frizon, inte en fälla."],
 "Bredare zoner gör det lättare. Smalare gör det svårare. Ta bort dubbla poängen när bredden sitter."),

("D5","Spela ut bakifrån","D","Halv 7-mannaplan · mv + 4 mot 3","12–15 min",
 "Åtta spelare: målvakt och fyra utespelare mot tre försvarare. Backarna startar brett och lågt, sexan i mitten. En linje markerad tvärs över mitten.",
 "Anfallande lag ska ta bollen från eget målområde över mittlinjen under kontroll. Försvarande lag får poäng för att vinna bollen och göra mål i ett litet konmål.",
 ["Brett och lågt först, sedan framåt. Backarna nästan ut till hörnflaggorna — det känns fel för dem och det är rätt.",
  "Är sexan täckt går bollen till en back, inte in i röran. Att välja bort mitten är ett bra beslut.",
  "Öppen kropp vid varje mottagning. Se D2.",
  "Tillbaka till målvakten och över till andra sidan är ALLTID ett bra beslut, aldrig ett misslyckande. Säg det högt varje gång det händer.",
  "De kommer att tappa bollen och släppa in mål av det här. Det är priset, och det är värt det."],
 "5 mot 2 om det är för svårt, 5 mot 4 om det är för lätt. Ändra antalet försvarare, inte reglerna."),

("D6","Fyra mål, två färger","D","25 × 25 m, 4 mot 4","12–15 min",
 "Fyra konmål, ett i varje hörn. Varje lag anfaller två av dem och försvarar två.",
 "Vanligt spel mot två mål var. Är det tätt vid det ena målet är det öppet vid det andra.",
 ["Samma idé som C3, men nu måste bollen flyttas med passningar för att hinna byta sida.",
  "Frågan är alltid densamma: vilket mål är öppet? Ställ den före, inte efter.",
  "Vänd spelet i stället för att tvinga. Den som kör huvudet i väggen vid ett mål har missat att det andra står tomt.",
  "Bra sista övning före spel — den flyttar blicken utan att någon behöver säga blick."],
 "Fri touch som grund. Max tre touch för dem som vill ha det svårare. Aldrig touchbegränsning i vanligt spel."),

("E1","Närmast går","E","20 × 20 m, 3 mot 3","8–10 min",
 "Två konmål, små lag, tät yta. Tränaren står vid sidan och räknar högt.",
 "Vanligt spel med en enda regel: när ni tappar bollen ska den som är närmast vara framme på bollhållaren innan tränaren räknat till tre. Räkna högt, varje gång.",
 ["Räkningen ÄR övningen. Slutar du räkna försvinner beteendet samma minut.",
  "Beröm den som går, även när hen inte vinner bollen. Det är försöket vi bygger.",
  "Bromsa in innan. Den som springer in i full fart blir passerad i full fart.",
  "Kom snett, inte rakt framifrån — då styr kroppen redan bollen åt ett håll."],
 "Räkna till fyra för den som har långt att springa. Till två för den som vill ha det svårare."),

("E2","Två som samarbetar","E","18 × 14 m, 2 mot 2 + väntande par","8–10 min",
 "Ett litet mål på vardera kortsidan. Två par på banan, ett eller två par utanför. Du står vid sidan med bollarna.",
 "Rulla in en boll till det ena paret — de anfaller, det andra paret försvarar. Omgången är slut vid mål, boll ut, eller efter cirka trettio sekunder. Nytt par in. Försvararna: en pressar, en täcker snett bakom, och de byter roll när bollen flyttar sig.",
 ["Den enda försvarsövningen där vi tränar samarbete i stället för duell. Därför behövs den.",
  "Den bakre ska kunna se både bollen och sin kompis samtidigt. Står hen rakt bakom ser hen ingenting.",
  "Låt dem prata: säg jag har dig högt. De tycker om det och det gör beteendet synligt.",
  "Två som går på samma boll är det fel vi rättar. Peka på det lugnt varje gång."],
 "Ge anfallarna en extra spelare när försvaret blir för bra. 3 mot 2 är en bra utmaning."),

("E3","Styr mot linjen","E","25 × 18 m, 1 mot 1 och 2 mot 2","8–10 min",
 "Bana med tydlig sidlinje markerad med koner. Ett mål.",
 "Anfallaren ska ta sig till mål. Försvararen får poäng för att vinna bollen — men också för att tvinga ut anfallaren över sidlinjen.",
 ["Sidlinjen är en försvarare gratis. Det är hela idén och den håller hela vägen upp i seniorfotboll.",
  "Kroppen bestämmer riktningen innan fötterna gör det. Kom snett.",
  "Stå kvar på fötterna. Tacklingen på marken är sista utvägen och nästan alltid fel vid den här åldern.",
  "Poäng för att styra, inte bara för att vinna — annars kastar de sig in i tacklingar."],
 "Smalare bana gör det lättare för försvararen. Bredare gör det svårare."),

("E4","Fem sekunder","E","30 × 25 m, 4 mot 4 + två jokrar","12–15 min",
 "Vanlig bana med mål eller konmål. Två jokrar som alltid spelar med bollhållande lag.",
 "Två regler samtidigt. Vinner ett lag bollen och gör mål inom tio sekunder räknas målet dubbelt. Vinner de tillbaka bollen inom fem sekunder efter att ha tappat den får de en poäng utan att göra mål.",
 ["Den bästa omställningsövningen vi har, och den enda som tränar båda riktningarna på en gång.",
  "Kör båda reglerna samtidigt från början. En i taget blir två tråkiga övningar i stället för en bra.",
  "Säg ingenting under spelet. Räkna bara högt — fem, fyra, tre — och låt räkningen coacha.",
  "Omställningar sker fyrtio till sextio gånger per match. Ingen annan övning ger lika mycket per minut."],
 "Ingen. Den fungerar för alla nivåer samtidigt, vilket är ovanligt — därför är den bra att avsluta med."),

("G1","3 mot 3 på flera banor","SPEL","Delad plan","20–25 min",
 "Dela planen i tre eller fyra små banor. Konmål eller små mål.",
 "3 mot 3 på varje bana samtidigt. Byt lag var femte minut. 18 spelare = tre banor. 13 = två banor plus en joker.",
 ["Alla spelar hela tiden. Ingen står still. Detta är hela veckans bollkontaktvolym.",
  "Blanda lagen om varannan gång. Varje spelare ska både få vara bland de starkaste i en grupp och bland de svagare i en annan.",
  "Lägg blockets villkor på spelet (mållinje / bonuspoäng / fyra mål)."],
 "Sätt de fyra–fem svagaste i samma spel som varandra i ETT av passen, aldrig varje gång."),

("G2","5 mot 5 — diamanten","SPEL","Halva 7-mot-7-planen","12–15 min",
 "Fem mot fem, uppställning 1-2-1.",
 "Vanligt spel. Introducera numren som ord: sexa, tvåa, trea, nia. Alla spelar alla nummer under hösten.",
 ["Numren är ett SPRÅK, inte positioner. Ingen är sexa — man är sexa idag.",
  "BOLL: vi spelar ut, vi rensar inte. Acceptera att det kostar mål.",
  "Ingen taktisk instruktion under spelet. Låt dem spela."],
 "Ingen. Alla spelar samma spel."),

("KAR","Karusellen — så bemannar ni passet","GRUND","Hela ytan","20–22 min",
 "Tre stationer bredvid varandra. En tränare per station. Grupperna roterar medsols var sjunde minut.",
 "Sätt tre grupper om sex (tisdag) eller två om sex–sju (torsdag). Grupperna byter station på din signal, tränarna står kvar.",
 ["Tränaren står kvar, gruppen flyttar. Det betyder att varje tränare bara behöver kunna EN övning per pass — inte fem.",
  "Sätt grupperna på nytt varje vecka. Dra lott eller dela på färg. Aldrig fasta nivågrupper.",
  "Huvudtränaren är passvärd varje pass: håller tiden, ropar rotation, avgör när något bryts, tar hand om den som behöver två minuters paus. Rollen roterar inte — ni andra ska kunna komma direkt till er station.",
  "Den som är klar med uppgiften ska inte vänta in gruppen. Ge en svårare version på plats: svag fot, mindre yta, en touch. Extra svårighet är en utmärkelse, aldrig ett straff."],
 "Är ni bara två tränare: kör två stationer istället för tre, 9–10 minuter styck."),

("MV1","Målvaktsbågen","MV","Stort mål","8–10 min",
 "Fem till sex spelare i en båge framför målet, cirka åtta meter ut, en boll var. En målvakt i mål. Numrera bågen 1, 2, 3, 4, 5.",
 "Servarna skjuter eller kastar i tur och ordning, ett efter ett utan paus. Målvakten arbetar sig längs bågen och måste flytta fötterna mellan varje. När varvet är klart byter målvakt — nästa i bågen går in, den gamla ställer sig sist.",
 ["Löpande i stället för en och en. Ingen står och tittar, och alla får målvaktsträning under hösten.",
  "Kroppen bakom bollen. Alltid. Det är hela tekniken i den här åldern.",
  "Servarna räknar räddningar åt varandra — det ger dem en uppgift mellan sina skott.",
  "Korgen lågt, W-greppet högt. Rensar målvakten med händerna har hen inte fångat."],
 "Servarna bestämmer själva om de kastar eller skjuter. Mjukare och närmare för de som är osäkra."),

("MV2","Fallteknik i sidled","MV","Gräs · hela gruppen parvis","8–10 min",
 "Hela gruppen två och två, utspridda på gräs med god plats mellan paren. En arbetar, en servar och tittar. Ingen boll och inget mål till att börja med. Alla par ligger på samma steg samtidigt så att du kan se hela gruppen.",
 "Fem steg, och man börjar alltid på marken och arbetar uppåt: 1) sittande med benen ut — tippa åt sidan och landa. 2) knästående. 3) hukande. 4) stående, servaren rullar bollen åt sidan. 5) stående i rörelse. Fem fall per sida, byt. Boll läggs till först när steg 3 sitter.",
 ["VI DYKER INTE, VI SJUNKER IHOP. Vid nio år ska ingen vara i luften. Kroppen sänks åt sidan och landar — den kastas inte. Dykningen kommer om fem år.",
  "LANDA LÄNGS HELA SIDAN. Kontakten ska rulla av längs kroppen: yttersida av ben, höft, revben, axel. Landar man på en punkt — armbågen, höftkulan, axelspetsen — tar den punkten hela kraften.",
  "NEDERSTA HANDEN HÖR HEMMA PÅ BOLLEN, ALDRIG I MARKEN. Det här är den enda punkten som verkligen betyder något. Instinkten att ta emot med handen skickar kraften rakt upp i handled, armbåge och nyckelben, och det är så unga målvakter bryter armar. Titta efter just den handen, hela tiden.",
  "HUVUDET IFRÅN MARKEN. Hakan bort från bröstet, blicken mot bollen. Vrid aldrig in ansiktet i underlaget.",
  "Servaren har en uppgift: titta på nedersta handen och säga till. Det ger den som tittar något att göra och lär ut tekniken lika bra som att göra den."],
 "Steg 1 och 2 räcker långt och är helt tillräckligt för många. Ingen tvingas högre, och det ska aldrig kommenteras att någon stannar kvar på ett lägre steg. Underlaget avgör: aldrig på grus, aldrig på frusen mark, aldrig på konstgräs utan långa byxor."),

("MV3","Spela ut under press","MV","Halva ytan","10–12 min",
 "Målvakt i mål, tre utespelare framför (numren 2, 3 och 6), två pressare. Tre mottagare står i en målzon i andra änden. Åtta till nio spelare igång samtidigt.",
 "Målvakten ska rulla eller passa ut till en av de tre, som sedan ska få bollen vidare in i målzonen. Två pressare försöker vinna den. Vinner pressarna byter de plats med två i kedjan. Målvakten roterar var nittionde sekund.",
 ["Detta är BOLL vid källan. Målvakten är första anfallaren, inte sista försvararen.",
  "Vi rensar aldrig i första hand — inte heller med händerna.",
  "Mottagarna ska gå bort och komma tillbaka. Står de stilla finns ingen fri.",
  "Målvakten ska också kunna ta emot en bakåtpassning med foten. Det kommer i matcherna."],
 "Ta bort en pressare för att göra det lättare. Lägg till en tredje för den som vill ha det svårare."),

("G3","7 mot 7 på hel plan","SPEL","Hel 7-mot-7-plan","10–15 min",
 "Sju mot sju med målvakt, uppställning 2-3-1. Numren 1 · 2 · 3 · 6 · 7 · 11 · 9.",
 "Vanligt spel på hel plan. Samma nummer som i femmannaspelet — sexan står fortfarande bakom bollen, nian är fortfarande högst upp. Nytt är att sjuan och elvan håller bredden ute vid linjerna.",
 ["Tre saker, inte fler: HÅLL BREDDEN (7 och 11 ute vid linjen), SEXAN BAKOM BOLLEN, MÅLVAKTEN SPELAR UT.",
  "Ingen taktisk instruktion under spelet. Säg det före, låt dem spela, säg det igen efter.",
  "Bredden är det svåraste. Niåringar dras mot bollen som magneter. Ställ 7 och 11 på plats med handen i stället för att ropa.",
  "MOD gäller på hel plan också. Stora ytor betyder fler 1 mot 1, inte färre."],
 "Alla spelar alla nummer under hösten. Ingen är sexa — man är sexa idag."),

("T1","Test — grindar 60 sek","TEST","25 × 20 m, 10 grindar","4 min",
 "Tio grindar av koner utspridda, olika breda. Samma uppställning varje testdag — mät upp och fotografera den första gången.",
 "Hur många grindar hinner spelaren dribbla igenom på 60 sekunder? Samma grind två gånger i rad räknas inte. Partnern räknar högt.",
 ["Mäter bollkontroll i fart plus förmågan att välja nästa grind med huvudet uppe.",
  "Kravet att byta grind är det som gör att blicken måste upp. Släpp inte på det.",
  "Skriv siffran på spelarens eget kort direkt, inte på en lista."],
 "Ingen. Samma uppställning för alla, annars mäter ni ingenting."),

("T2","Test — sulrullningar 30 sek","TEST","På stället","4 min",
 "En boll. Ingen yta behövs. En partner som räknar och tar tid.",
 "Rulla bollen i sidled fram och tillbaka med sulan, växelvis fot. Räkna vartannat, alltså antal dubbelrullningar på 30 sekunder.",
 ["Det test som minst påverkas av längd, styrka och födelsemånad. Nästan rent färdighetsmått.",
  "Kvalitet före fart — bollen ska vara under kontroll. Slarviga rullningar räknas inte.",
  "Partnern räknar högt. Det gör siffran trovärdig för den som gör testet."],
 "Ingen. Alla gör samma test — det är hela poängen med självjämförelse."),

("T3","Test — svag fot mot mål","TEST","8 m från mål","4 min",
 "Tio bollar i rad, åtta meter från ett litet mål eller konmål.",
 "Tio skott, bara med svag fot. Räkna antal mål. Skott utanför räknas inte.",
 ["Svagfotsförmåga är nästan rent inlärd. Därför ett av de ärligaste testen i den här åldern.",
  "Bestäm svag fot en gång i augusti och håll den hela hösten.",
  "Samma avstånd, samma mål, varje gång. Annars mäter ni ingenting."],
 "Ingen. Flytta aldrig konerna för att någon ska få en bättre siffra."),

("T4","Test — första touch genom grind","TEST","Par + en grind","4 min",
 "En grind två meter snett framför mottagaren. Samma avstånd varje testdag.",
 "Tio passningar. Räkna hur många gånger av tio första touchen går genom grinden. Studsar bollen genom efter två touchar räknas den inte.",
 ["Mäter om touchen går UT UR fötterna eller bara stoppas.",
  "Passaren ska slå lika hårt varje gång. Låt samma spelare passa hela testet.",
  "Byt sida på grinden halvvägs — fem åt vardera hållet."],
 "Ingen. Flytta aldrig grinden för att någon ska få en bättre siffra."),

("T5","Test — vändningar 45 sek","TEST","8 m mellan koner","4 min",
 "Två koner med åtta meter mellan.",
 "För bollen fram och tillbaka mellan konerna. Vänd med sulan vid varje kon. Räkna antal vändningar på 45 sekunder.",
 ["Mäter bollkontroll i fart plus vändningsteknik — kärnan i höstens block A.",
  "Vändningen ska ske vid konen, inte tre meter före. Partnern dömer.",
  "Båda fötterna används automatiskt eftersom riktningen växlar."],
 "Ingen."),

("T6","Test — titta före","TEST","Par + en visare","4 min",
 "Passare framför, en som visar siffror bakom mottagaren. Åtta meter mellan passare och mottagare.",
 "Tio passningar. Visaren håller upp fingrar när bollen lämnat passarens fot. Mottagaren måste säga rätt siffra INNAN bollen når fram. Sägs den efteråt räknas den inte.",
 ["Mäter om vändningen på huvudet sker medan bollen är på väg — vilket är hela poängen.",
  "Visaren ska byta antal fingrar varje gång, annars gissar de.",
  "Låt samma person visa under hela testet så att timingen blir lika för alla."],
 "Ingen."),

("G4","5 mot 5 med sidostation","SPEL","5-mot-5-planen + yta bredvid","20–25 min",
 "En bana för 5 mot 5 med målvakter, och en yta bredvid för den tredje gruppen. Sätt båda innan passet börjar.",
 "Passar 15–18 spelare: tio på banan och resten vid sidan. Sidogruppen kör en övning ur kvällens tema. Rotera var sjätte minut: sidogruppen går in och ett av lagen går ut. Alla spelar ungefär lika mycket över passet.",
 ["Tre grupper, inte två. Med så många spelare på en 5-mot-5-plan blir ett enda stort spel en klunga där halva truppen aldrig rör bollen.",
  "Sidostationen är ingen bänk. Välj en övning med hög bollkontaktvolym — A2, B2 eller C3 fungerar alltid — så att den gruppen får FLER touchar än de som spelar, inte färre.",
  "Rotera på klockan, inte på känsla. Ropa bytet högt och byt hela grupper, aldrig enskilda spelare.",
  "Håll rotationen tajt. Sex minuter känns kort och är rätt — det är väntan mellan omgångarna som dödar ett pass.",
  "En ledare vid spelet, en vid sidostationen. Är ni tre tar den tredje observationen, se 05-matning-och-utveckling.md."],
 "Är ni 11–14 den kvällen: 4 mot 4 på banan och resten vid sidan, samma rotation. Är ni över tjugo: två banor och en sidogrupp."),

("TRK","Så delar du tisdagsplanen","GRUND","7-mot-7-planen","—",
 "Dela planen i tre banor med koner innan någon kommer.",
 "En trupp på 16–20 = tre banor à 3 mot 3. Ingen står still, ingen väntar. Öppna aldrig hela ytan förrän sista kvarten.",
 ["En 7-mot-7-plan med en full trupp niåringar är en nackdel om du använder den hel.",
  "De fyra–fem svagaste får noll bollkontakter på stor yta. På liten yta måste de röra bollen.",
  "Sätt konerna innan de kommer. Alltid."],
 "—"),
]

BLOCKNAME = {"GRUND":"Grund","A":"Block A","B":"Block B","C":"Block C","D":"Block D","E":"Block E","SPEL":"Spel","MV":"Målvakt","TEST":"Testövning"}

# ---------------------------------------------------------------- sessions
def tue(w, date, block, theme, slots, focus):
    return dict(n=0, w=w, day="Tisdag", date=date, dur=90, pitch="7 mot 7",
                block=block, theme=theme, slots=slots, focus=focus)

def thu(w, date, block, theme, slots, focus):
    return dict(n=0, w=w, day="Torsdag", date=date, dur=60, pitch="5 mot 5",
                block=block, theme=theme, slots=slots, focus=focus)

S = []

# ---- BLOCK A -------------------------------------------------------------
S.append(tue(1,"4 aug","A","Föra bollen — introduktion",
 [("0:00","ANK","Ankomst — boll var"),("0:15","11+","FIFA 11+ Kids"),
  ("0:25","KAR","Karusell:  A1 Färgvästen  ·  A3 Grindar  ·  MV1 Målvaktsbågen"),
  ("0:47","G1","3 mot 3 på tre banor — mållinjeregel"),
  ("1:12","G3","7 mot 7 på hel plan — bredd, sexan, målvakten spelar ut"),
  ("1:25","—","Avslut: en sak du provade idag")],
 "Första passet. Sätt ankomstrutinen och karusellrutinen — båda gäller resten av hösten."))

S.append(thu(1,"6 aug","A","Föra bollen — volym",
 [("0:00","ANK","Ankomst — boll var"),("0:10","11+","Kort uppvärmning med boll"),
  ("0:17","KAR","Två stationer:  A2 Kungen av banan  ·  A1 Färgvästen"),
  ("0:35","A5","Mållinjespel 3 mot 3 på två banor + joker"),
  ("0:45","G3","7 mot 7 eller 6 mot 6 på största möjliga yta")],
 "Tät yta, hög volym. Prata nästan inte alls."))

S.append(tue(2,"11 aug","A","Fartförändring",
 [("0:00","ANK","Ankomst"),("0:15","11+","FIFA 11+ Kids"),
  ("0:25","KAR","Karusell:  A4 Hajar  ·  A3 Grindar  ·  MV2 Fallteknik i sidled (hela gruppen)"),
  ("0:47","G1","3 mot 3 på tre banor"),
  ("1:12","G3","7 mot 7 på hel plan — bredd, sexan, målvakten spelar ut"),
  ("1:25","—","Avslut")],
 "Fartförändring är veckans ord. MV2 först utan boll — fallet ska sitta innan bollen kommer in."))

S.append(thu(2,"13 aug","A","Skydda och gå",
 [("0:00","ANK","Ankomst"),("0:10","11+","Kort uppvärmning"),
  ("0:17","KAR","Två stationer:  A2 Kungen av banan  ·  A1 Färgvästen — två västar samtidigt"),
  ("0:35","G1","3 mot 3 på två banor + joker"),
  ("0:45","G3","7 mot 7 eller 6 mot 6 på största möjliga yta")],
 "Två korta stationer istället för ett långt block. CUP PÅ SÖNDAG: lägg inget nytt till idag. "
 "Ta två minuter i slutet om cupdagen — tider, mat, att alla spelar ungefär lika mycket."))

S.append(tue(3,"18 aug","A","Block A förlängt — tvåledarpass",
 [("0:00","ANK","Ankomst — boll var. Koner ute innan första spelaren kommer."),
  ("0:15","A1","Färgvästen med hela gruppen — ledaren står stilla utanför rutan"),
  ("0:25","KAR","DUBBEL karusell, två stationer:  A3 Grindar  ·  A4 Hajar. Två varv om sex minuter."),
  ("0:50","A5","Mållinjespel — två banor, 4 mot 4 och 5 mot 5"),
  ("1:12","G3","Största möjliga yta, jämna lag"),
  ("1:27","—","Avslut: en sak du provade idag")],
 "TVÅ LEDARE. Testdagen är flyttad till 25 augusti — den kräver tre vuxna och odelad "
 "uppmärksamhet, och en halvgjord mätning är värre än ingen. Upplägget här är byggt för få "
 "övergångar och övningar som rullar själva: A1 kräver att ledaren står still med västarna, "
 "A3 räknar spelarna själva, och mållinjeregeln behöver ingen domare. Block A förlängs en "
 "vecka — det kostar ingenting, temat behöver ändå sina tjugo möten. Är ni arton: 9 mot 9 sist."))

S.append(thu(3,"20 aug","A","Volym",
 [("0:00","ANK","Ankomst"),("0:10","11+","Kort uppvärmning"),
  ("0:17","KAR","Tre stationer:  A4 Hajar  ·  A2 Kungen av banan  ·  A3 Grindar"),
  ("0:35","G4","5 mot 5 + sidostation: A3 Grindar med mållinjeregel. Rotera var sjätte minut.")],
 "Sista renodlade A-passet. Kolla grindsiffrorna mot vecka 1."))

S.append(tue(4,"25 aug","A→B","TESTDAG 1 — utgångsläge",
 [("0:00","ANK","Ankomst"),("0:15","11+","FIFA 11+ Kids"),
  ("0:25","TEST","Testdag: T1 · T2 · T3 · T6, fyra min per station"),
  ("0:50","G1","3 mot 3 — mållinjeregeln FINNS KVAR"),
  ("1:12","G3","7 mot 7 på hel plan"),
  ("1:25","—","Dela ut Kopparkorten")],
 "Dela ut korten idag. Säg tydligt: du tävlar mot dig själv, ingen annan. Ingen lista sätts upp. "
 "Testdagen flyttades hit från den 18:e. BRYGGAN GÄLLER ÄNDÅ: mållinjeregeln ligger kvar i "
 "spelet, och fintan introduceras på torsdag i stället för idag."))

S.append(thu(4,"27 aug","A→B","Brygga: bonuspoängen introduceras",
 [("0:00","ANK","Ankomst"),("0:10","11+","Kort uppvärmning"),
  ("0:17","KAR","Tre stationer:  A2 Kungen av banan  ·  B1 Fintstationen  ·  A3 Grindar"),
  ("0:35","G4","5 mot 5 med bonuspoäng + sidostation: B1 Fintstationen. Förklara bonusen på 20 sekunder.")],
 "Bonuspoängen kommer nu och sitter kvar i sju veckor. CUP PÅ SÖNDAG: det är det enda nya idag, "
 "och den är värd att ta med sig dit — den belönar exakt det vi vill se i cupen."))

# ---- BLOCK B -------------------------------------------------------------
S.append(tue(5,"1 sep","B","1 mot 1 — introduktion",
 [("0:00","ANK","Ankomst"),("0:15","11+","FIFA 11+ Kids"),
  ("0:25","KAR","Karusell:  B1 Fintstationen  ·  B2 1 mot 1 till två mål  ·  MV2 Fallteknik i sidled (hela gruppen)"),
  ("0:47","B4","3 mot 3 med bonuspoäng, tre banor"),
  ("1:12","G3","7 mot 7 på hel plan — bredd, sexan, målvakten spelar ut"),
  ("1:25","—","Avslut")],
 "Blockets kärna. Beröm varje försök att gå förbi, oavsett utfall. Inled med cupfrågan: "
 "vem gick förbi någon i söndags? Det är den enda cupuppföljning vi gör."))

S.append(thu(5,"3 sep","B","Duellvolym",
 [("0:00","ANK","Ankomst"),("0:10","11+","Kort uppvärmning"),
  ("0:17","KAR","Tre stationer:  B2 1 mot 1 till två mål  ·  B1 Fintstationen  ·  B3 Rullad boll"),
  ("0:35","G4","5 mot 5 med bonuspoäng + sidostation: B2 1 mot 1. Rotera var sjätte minut.")],
 "Ren dueltäthet. Räkna högt varje gång någon får 3 poäng."))

S.append(tue(6,"8 sep","B","Duell och försvar",
 [("0:00","ANK","Ankomst"),("0:15","11+","FIFA 11+ Kids"),
  ("0:25","KAR","Karusell:  B5 Styra anfallaren  ·  B2 1 mot 1 till två mål  ·  MV1 Målvaktsbågen"),
  ("0:47","B4","3 mot 3 med bonuspoäng"),
  ("1:12","G3","7 mot 7 — numren"),
  ("1:25","—","Avslut")],
 "Höstens enda renodlade försvarspass. B5 handlar om att komma snett och styra, inte om att "
 "vinna bollen — ge poäng för att tvinga ut anfallaren över linjen. Bonuspoängen ligger kvar i spelet."))

S.append(thu(6,"10 sep","B","Egen finta",
 [("0:00","ANK","Ankomst"),("0:10","11+","Kort uppvärmning"),
  ("0:17","KAR","Tre stationer:  B1 Egen finta  ·  B2 1 mot 1 stege  ·  B3 Rullad boll"),
  ("0:35","G4","5 mot 5 med bonuspoäng + sidostation: B1 Egen finta. Rotera var sjätte minut.")],
 "Autonomi hela passet. De väljer, du räknar. CUP PÅ SÖNDAG: inget nytt, lätt pass, "
 "och sista 7-mot-7-spelet med numren innan formen införs på tisdag."))

S.append(tue(7,"15 sep","B","Kaos, beslut — och 2-3-1 införs",
 [("0:00","ANK","Ankomst"),("0:15","11+","FIFA 11+ Kids"),
  ("0:25","KAR","Karusell:  B3 Rullad boll  ·  B1 Egen påhittad finta  ·  MV3 Spela ut under press"),
  ("0:47","B4","3 mot 3 med bonuspoäng"),
  ("1:12","G3","7 mot 7 i 2-3-1 — formen införs, tre coachpunkter före, tystnad under"),
  ("1:25","—","Avslut")],
 "Två dagar efter cupen: börja med att fråga vem som gick förbi någon. Låt dem döpa sina finter. "
 "Sista kvarten är första gången 2-3-1 ritas upp — elva dagar till träningsmatchen 26 sep. "
 "Se 09-positionsspel.md kapitel 4."))

S.append(thu(7,"17 sep","B","Duellvolym",
 [("0:00","ANK","Ankomst"),("0:10","11+","Kort uppvärmning"),
  ("0:17","KAR","Tre stationer:  B5 Styra anfallaren  ·  B3 Rullad boll  ·  B2 1 mot 1 till två mål"),
  ("0:35","G4","5 mot 5 med bonuspoäng + sidostation: B3 Rullad boll. Rotera var sjätte minut.")],
 "Försvarsspelets enda pass i höst: kom nära, stå kvar på fötterna. Räkna även 1-mot-1-försök i en match."))

S.append(tue(8,"22 sep","B→C","TESTDAG 2 — halvtid",
 [("0:00","ANK","Ankomst"),("0:15","11+","FIFA 11+ Kids"),
  ("0:25","TEST","Testdag: T1 · T2 · T3 · T6. Korten med hemifrån."),
  ("0:50","B4","3 mot 3 — bonuspoängen FINNS KVAR"),
  ("1:12","G3","7 mot 7 i 2-3-1"),
  ("1:25","—","Avslut")],
 "Här syns de första riktiga hoppen. Peka på förbättringen, inte på nivån. BRYGGAN GÄLLER ÄNDÅ: "
 "bonuspoängen ligger kvar i spelet, och C1 med coachordet TITTA INNAN DU FÅR DEN kommer på "
 "torsdag. Fyra veckor sedan testdag 1, fyra veckor till testdag 3."))

S.append(thu(8,"24 sep","B→C","GENERALREPETITION — 7 mot 7",
 [("0:00","ANK","Ankomst"),("0:10","11+","Kort uppvärmning"),
  ("0:17","KAR","EN station:  C1 Nummer bakom"),
  ("0:27","G3","7 mot 7 i 2-3-1 — resten av passet. Numren delas ut och roteras.")],
 "Träningsmatchen är om två dagar och det här är enda gången formen kan sättas innan dess. "
 "En station, inte tre. Tre coachpunkter sagda FÖRE: håll bredden, sexan bakom bollen, "
 "målvakten spelar ut. Sedan tystnad. Med full trupp blir det 7 mot 7 plus några som "
 "roterar in var tredje minut — byt hela positioner, inte enskilda spelare."))

# ---- BLOCK C -------------------------------------------------------------
S.append(tue(9,"29 sep","C","Första touchen",
 [("0:00","ANK","Ankomst"),("0:15","11+","FIFA 11+ Kids"),
  ("0:25","KAR","Karusell:  C1 Nummer bakom  ·  C2 Touch genom grind  ·  MV2 Fallteknik i sidled (hela gruppen)"),
  ("0:47","C3","Fyra mål 3 mot 3, tre banor"),
  ("1:12","G3","7 mot 7 på hel plan — bredd, sexan, målvakten spelar ut"),
  ("1:25","—","Avslut")],
 "Skillnaden mellan att STOPPA bollen och att ta den NÅGONSTANS. Första passet efter "
 "träningsmatchen i 7 mot 7: fråga vad som kändes annorlunda mot 5 mot 5. Svaret brukar bli "
 "att det var längre till varandra — och det är precis vad C-blocket och bredden handlar om."))

S.append(thu(9,"1 okt","C","Touchvolym",
 [("0:00","ANK","Ankomst"),("0:10","11+","Kort uppvärmning"),
  ("0:17","KAR","Tre stationer:  C2 Touch genom grind  ·  C1 Nummer bakom  ·  C4 Vänd och gå"),
  ("0:35","G4","5 mot 5 + sidostation: C3 Fyra mål. Rotera var sjätte minut.")],
 "Båda fötterna. Flytta grinden till andra sidan hela tiden."))

S.append(tue(10,"6 okt","C","Vända bort från press",
 [("0:00","ANK","Ankomst"),("0:15","11+","FIFA 11+ Kids"),
  ("0:25","KAR","Karusell:  C4 Vänd och gå  ·  C6 Frågan före  ·  MV3 Spela ut under press"),
  ("0:47","C3","Fyra mål"),
  ("1:12","G3","7 mot 7 på hel plan — bredd, sexan, målvakten spelar ut"),
  ("1:25","—","Avslut")],
 "Säg till dem varför vi kör det här: cupen i 7 mot 7 är om fyra dagar, och att kunna vända "
 "bort från press är det som gör den större ytan hanterbar. De gillar att veta varför."))

S.append(thu(10,"8 okt","C","GENERALREPETITION — inför cupen",
 [("0:00","ANK","Ankomst"),("0:10","11+","Kort uppvärmning"),
  ("0:17","KAR","EN station:  C5 Huvudet uppe"),
  ("0:27","G3","7 mot 7 i 2-3-1 — resten av passet. Bredden och sexan.")],
 "Tvådagarscupen är om två dagar. Samma upplägg som 24 sep: en station, sedan spel i formen, "
 "7 mot 7 plus tre som roterar in. "
 "De två svåraste sakerna är att sjuan och elvan håller bredden och att sexan inte springer "
 "förbi bollen — säg dem före, säg ingenting under. Prata också igenom cupdagen: mat, "
 "rotation av nummer, att alla spelar ungefär lika mycket."))

S.append(tue(11,"13 okt","C","Öppen kropp",
 [("0:00","ANK","Ankomst"),("0:15","11+","FIFA 11+ Kids"),
  ("0:25","KAR","Karusell:  C2 Touch genom grind  ·  C4 Vänd och gå med störare  ·  MV1 Målvaktsbågen"),
  ("0:47","C3","Fyra mål"),
  ("1:12","G3","7 mot 7 på hel plan — bredd, sexan, målvakten spelar ut"),
  ("1:25","—","Avslut")],
 "Halvvänd redan när bollen är på väg. Visa det, säg det inte. LÄTT PASS: två cupdagar i "
 "benen. Kort karusell, mycket spel, låg röst. Fråga vad de är stolta över från cupen."))

S.append(thu(11,"15 okt","C","Volym",
 [("0:00","ANK","Ankomst"),("0:10","11+","Kort uppvärmning"),
  ("0:17","KAR","Tre stationer:  C6 Frågan före  ·  C5 Huvudet uppe  ·  C2 Touch genom grind"),
  ("0:35","G4","5 mot 5 + sidostation: C3 Fyra mål. Rotera var sjätte minut.")],
 "Sista renodlade C-passet."))

S.append(tue(12,"20 okt","C","Allt tillsammans",
 [("0:00","ANK","Ankomst"),("0:15","11+","FIFA 11+ Kids"),
  ("0:25","TEST","TESTDAG 3 — T1 · T2 · T3 · T6, sista mätningen"),
  ("0:50","B4","3 mot 3 med bonuspoäng"),
  ("1:12","G3","7 mot 7 på hel plan — bredd, sexan, målvakten spelar ut"),
  ("1:25","—","Avslut: vad är du bäst på nu som du inte var i augusti?")],
 "Visa dem kurvan från augusti. Detta är hela höstens bevis — och det enda de kommer minnas av mätningen."))

S.append(thu(12,"22 okt","C","Spelarnas val",
 [("0:00","ANK","Ankomst"),("0:10","11+","Kort uppvärmning"),
  ("0:17","—","Spelarna väljer tre övningar från hösten, en per station"),
  ("0:35","G4","5 mot 5 + sidostation: spelarnas val. Rotera var sjätte minut.")],
 "Låt dem välja. Du får veta vilka övningar som faktiskt landade."))

S.append(tue(13,"27 okt","—","Fritt",
 [("0:00","ANK","Ankomst"),("0:15","11+","FIFA 11+ Kids"),
  ("0:25","—","Spelarnas val"),
  ("0:47","G1","3 mot 3 på tre banor"),
  ("1:12","G3","7 mot 7 på hel plan — bredd, sexan, målvakten spelar ut"),
  ("1:25","—","Avslut säsong")],
 "Spela. Säg nästan ingenting."))

S.append(thu(13,"29 okt","—","Avslutning",
 [("0:00","ANK","Ankomst"),("0:10","—","Vad de vill"),
  ("0:30","—","Match, föräldrar mot barn om ni vill"),
  ("0:55","—","Avslutning")],
 "Fråga varje spelare vad hen kan nu som hen inte kunde i augusti — det är höstens egentliga facit. Räkna sedan truppen och jämför med 4 augusti."))

for i, s in enumerate(S):
    s['n'] = i + 1

# --------------------------------------------------------------- 7-mot-7-trappan
# G3-slotten sist i varje pass är höstens löpande förberedelse inför träningsmatchen
# i 7 mot 7 den 26 september och cupen 10-11 oktober. Den följer en trappa: fritt spel,
# sedan numren, sedan formen, sedan bredden och sexan.
#
# Blocken A/B/C rörs inte — de är ryggraden. Hela 7-mot-7-förberedelsen ligger här.
# P1-P3 lämnas som de kördes.
G3_TRAPPA = [
    (4,  8,  "7 mot 7 på största möjliga yta — bara spel, inga instruktioner"),
    (9,  12, "7 mot 7 — NUMREN: alla får ett nummer högt, roteras varje spel"),
    (13, 16, "7 mot 7 i 2-3-1 — formen och de tre coachpunkterna"),
    (17, 20, "7 mot 7 i 2-3-1 — bredden (7 och 11) och sexan bakom bollen"),
    (21, 26, "7 mot 7 på största möjliga yta — låt det sitta"),
]
for s in S:
    for lo, hi, txt in G3_TRAPPA:
        if lo <= s['n'] <= hi:
            s['slots'] = [(tm, c, txt if c == "G3" else w) for tm, c, w in s['slots']]
            break

# ---------------------------------------------------------------- html
def esc(t): return html.escape(str(t))

exlookup = {e[0]: e for e in EX}

css = """
:root{
  --ink:#10161C; --blue:#1B3A6B; --copper:#A85B2B; --verd:#3E7D6E;
  --paper:#E9ECE8; --card:#FFFFFF; --line:#CBD1CA; --grey:#6E766F;
  --sand:#DFE3DD;
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--paper);color:var(--ink);
  font-family:'Source Sans 3',system-ui,sans-serif;font-size:16.5px;line-height:1.55}
.wrap{max-width:980px;margin:0 auto;padding:0 20px 100px}
h1,h2,h3,h4,.disp{font-family:'Oswald',Impact,sans-serif;font-weight:500;
  letter-spacing:.01em;margin:0}
.mono{font-family:'IBM Plex Mono',monospace}

/* hero */
header.hero{background:var(--blue);color:#fff;padding:52px 0 0;margin-bottom:0;
  border-bottom:9px solid var(--copper)}
.hero .wrap{padding-bottom:44px}
.eyebrow{font-family:'IBM Plex Mono',monospace;font-size:12px;letter-spacing:.22em;
  text-transform:uppercase;color:#9FC3D9;margin-bottom:22px}
.hero h1{font-size:clamp(46px,9.5vw,104px);line-height:.88;text-transform:uppercase;
  font-weight:600;letter-spacing:-.005em}
.hero h1 em{font-style:normal;color:var(--copper);
  -webkit-text-stroke:1.5px var(--copper);color:transparent}
.tri{display:flex;gap:0;margin-top:38px;border-top:1px solid rgba(255,255,255,.28)}
.tri div{flex:1;padding:20px 18px 6px;border-right:1px solid rgba(255,255,255,.28)}
.tri div:last-child{border-right:0}
.tri strong{display:block;font-family:'Oswald',sans-serif;font-size:27px;
  text-transform:uppercase;color:#fff;font-weight:600;letter-spacing:.03em}
.tri span{font-size:14.5px;color:#BCD2E2;display:block;margin-top:5px;line-height:1.4}
.sub{margin-top:26px;font-size:17px;color:#CFE0EC;max-width:58ch}

/* nav */
nav{position:sticky;top:0;z-index:50;background:var(--paper);
  border-bottom:1px solid var(--line);padding:0}
nav .wrap{display:flex;gap:2px;overflow-x:auto;padding:0 20px;
  scrollbar-width:none}
nav .wrap::-webkit-scrollbar{display:none}
nav a{font-family:'Oswald',sans-serif;font-size:13.5px;text-transform:uppercase;
  letter-spacing:.09em;color:var(--grey);text-decoration:none;padding:15px 15px;
  white-space:nowrap;border-bottom:3px solid transparent}
nav a:hover,nav a:focus{color:var(--blue);border-bottom-color:var(--copper);outline:none}

/* sections */
section{padding-top:64px}
.shead{display:flex;align-items:baseline;gap:16px;
  border-bottom:2px solid var(--ink);padding-bottom:9px;margin-bottom:8px}
.shead h2{font-size:clamp(28px,4.6vw,42px);text-transform:uppercase;font-weight:600}
.shead .num{font-family:'IBM Plex Mono',monospace;font-size:12px;color:var(--copper);
  letter-spacing:.16em;font-weight:600}
.lede{font-size:17.5px;color:#3A4340;max-width:66ch;margin:16px 0 30px}

/* key */
.key{background:var(--card);border:1px solid var(--line);border-radius:4px;
  padding:22px 24px;display:grid;grid-template-columns:repeat(auto-fit,minmax(148px,1fr));
  gap:16px 22px;margin-bottom:14px}
.key div{display:flex;align-items:center;gap:11px;font-size:14.5px}
.key svg{flex:none}

/* exercise cards */
.exgrid{display:flex;flex-direction:column;gap:18px}
.ex{background:var(--card);border:1px solid var(--line);border-radius:4px;
  overflow:hidden;scroll-margin-top:64px}
.ex-top{display:flex;gap:0;flex-wrap:wrap}
.ex-fig{flex:1 1 340px;min-width:290px;background:var(--sand);padding:14px;
  display:flex;align-items:center;justify-content:center}
.ex-fig svg{width:100%;height:auto;display:block}
.ex-body{flex:1 1 340px;min-width:290px;padding:22px 24px}
.ex-code{font-family:'IBM Plex Mono',monospace;font-size:12px;font-weight:700;
  letter-spacing:.14em;color:#fff;background:var(--copper);padding:3px 8px;
  border-radius:2px;display:inline-block}
.ex-body h3{font-size:26px;text-transform:uppercase;margin:11px 0 3px;font-weight:600}
.meta{font-family:'IBM Plex Mono',monospace;font-size:12.5px;color:var(--verd);
  letter-spacing:.04em;margin-bottom:14px;font-weight:500}
.ex-body p{margin:0 0 11px;font-size:15.5px}
.ex-body p b{color:var(--blue)}
.cp{background:#F4F6F3;border-top:1px solid var(--line);padding:18px 24px}
.cp h4{font-family:'IBM Plex Mono',monospace;font-size:11px;letter-spacing:.17em;
  text-transform:uppercase;color:var(--copper);margin-bottom:9px;font-weight:700}
.cp ul{margin:0;padding-left:19px}
.cp li{font-size:15px;margin-bottom:6px}
.step{margin-top:13px;padding-top:12px;border-top:1px dashed var(--line);
  font-size:14.5px;color:#3A4340}
.step b{font-family:'IBM Plex Mono',monospace;font-size:11px;letter-spacing:.14em;
  color:var(--verd);text-transform:uppercase}

/* session cards */
.wk{font-family:'Oswald',sans-serif;text-transform:uppercase;font-size:14px;
  letter-spacing:.2em;color:var(--copper);margin:38px 0 12px;font-weight:600;
  border-top:1px solid var(--line);padding-top:14px}
.ses{background:var(--card);border:1px solid var(--line);border-radius:4px;
  margin-bottom:14px;overflow:hidden;scroll-margin-top:64px}
.ses-h{display:flex;align-items:center;gap:14px;flex-wrap:wrap;
  padding:15px 22px;background:var(--blue);color:#fff}
.ses-h .pid{font-family:'IBM Plex Mono',monospace;font-size:12px;font-weight:700;
  background:rgba(255,255,255,.16);padding:3px 8px;border-radius:2px;letter-spacing:.1em}
.ses-h .d{font-family:'Oswald',sans-serif;font-size:22px;text-transform:uppercase;
  font-weight:500;letter-spacing:.03em}
.ses-h .t{font-family:'IBM Plex Mono',monospace;font-size:12.5px;color:#AEC8DC;
  margin-left:auto;letter-spacing:.05em}
.ses-th{padding:14px 22px 4px;font-size:16.5px}
.ses-th b{font-family:'Oswald',sans-serif;text-transform:uppercase;font-weight:500;
  font-size:19px;letter-spacing:.02em;display:block;color:var(--blue)}
.spine{padding:14px 22px 8px;position:relative}
.spine::before{content:"";position:absolute;left:26px;top:20px;bottom:14px;
  width:2px;background:var(--sand)}
.row{display:flex;gap:16px;align-items:flex-start;padding:7px 0;position:relative}
.row .tm{font-family:'IBM Plex Mono',monospace;font-size:13px;font-weight:600;
  color:var(--verd);width:54px;flex:none;padding-left:16px;position:relative}
.row .tm::before{content:"";position:absolute;left:-1px;top:5px;width:9px;height:9px;
  background:var(--card);border:2.5px solid var(--verd);border-radius:50%}
.row:last-child .tm::before{background:var(--verd)}
.row .cd{flex:none;width:44px}
.row .cd a{font-family:'IBM Plex Mono',monospace;font-size:11px;font-weight:700;
  color:var(--copper);text-decoration:none;border:1px solid var(--copper);
  padding:1px 5px;border-radius:2px;letter-spacing:.06em}
.row .cd a:hover{background:var(--copper);color:#fff}
.row .cd span{font-family:'IBM Plex Mono',monospace;font-size:11px;color:#B4BAB3;
  padding:1px 5px}
.row .wt{font-size:15.5px;flex:1}
.focus{background:#F4F6F3;border-top:1px solid var(--line);padding:13px 22px;
  font-size:15px}
.focus b{font-family:'IBM Plex Mono',monospace;font-size:10.5px;letter-spacing:.16em;
  text-transform:uppercase;color:var(--copper);display:block;margin-bottom:3px}
.bridge .ses-h{background:var(--copper)}
.bridge .ses-h .t{color:#F3DCCB}

/* callouts */
.call{border-left:4px solid var(--copper);background:var(--card);
  padding:18px 22px;margin:22px 0;border-radius:0 4px 4px 0;
  border-top:1px solid var(--line);border-right:1px solid var(--line);
  border-bottom:1px solid var(--line)}
.call h4{font-family:'IBM Plex Mono',monospace;font-size:11px;letter-spacing:.17em;
  text-transform:uppercase;color:var(--copper);margin-bottom:8px;font-weight:700}
.call p{margin:0 0 9px;font-size:16px}
.call p:last-child{margin-bottom:0}
.two{display:grid;grid-template-columns:1fr 1fr;gap:16px}
@media(max-width:700px){.two{grid-template-columns:1fr}}
table{width:100%;border-collapse:collapse;background:var(--card);
  border:1px solid var(--line);font-size:15px;margin:8px 0 20px}
th{background:var(--blue);color:#fff;font-family:'Oswald',sans-serif;font-weight:500;
  text-transform:uppercase;font-size:13px;letter-spacing:.08em;text-align:left;
  padding:10px 13px}
td{padding:10px 13px;border-top:1px solid var(--line);vertical-align:top}
td.mono{font-family:'IBM Plex Mono',monospace;font-size:13px;color:var(--verd);
  white-space:nowrap;font-weight:600}
.cardgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:16px;margin:8px 0 22px}
.pcard{background:var(--card);border:2px solid var(--ink);border-radius:4px;padding:0;overflow:hidden;max-width:420px}
.pc-h{background:var(--ink);color:#fff;font-family:'Oswald',sans-serif;font-size:15px;
  letter-spacing:.12em;padding:9px 14px;display:flex;justify-content:space-between;align-items:baseline}
.pc-h span{font-family:'IBM Plex Mono',monospace;font-size:9.5px;color:#9AA39C;letter-spacing:.1em}
.pc-n{padding:12px 14px 8px;font-family:'IBM Plex Mono',monospace;font-size:10.5px;
  letter-spacing:.14em;color:var(--grey);display:flex;align-items:baseline;gap:9px}
.pc-line{flex:1;border-bottom:1px solid var(--line);height:15px}
.pc-t{width:100%;border:0;margin:0;font-size:13px;background:transparent}
.pc-t th{background:transparent;color:var(--copper);font-family:'IBM Plex Mono',monospace;
  font-size:9.5px;letter-spacing:.1em;padding:4px 8px;text-align:center;border-bottom:1px solid var(--line)}
.pc-t th:first-child{width:44%}
.pc-t td{padding:7px 8px;border-top:1px solid #EDEFEC;font-size:12.5px}
.pc-t td:not(:first-child){border-left:1px solid var(--line);background:#FAFBFA;width:18%}
.pc-g{padding:11px 14px 4px;font-family:'IBM Plex Mono',monospace;font-size:9.5px;
  letter-spacing:.13em;color:var(--grey);display:flex;align-items:baseline;gap:9px}
.pc-f{background:var(--copper);color:#fff;font-family:'Oswald',sans-serif;font-size:12.5px;
  letter-spacing:.09em;padding:7px 14px;text-align:center;margin-top:8px}
footer{margin-top:70px;border-top:2px solid var(--ink);padding-top:26px;
  font-size:14.5px;color:var(--grey)}
a{color:var(--blue)}
@media print{
  nav{display:none} .ses,.ex{break-inside:avoid;page-break-inside:avoid}
  body{background:#fff;font-size:11pt} header.hero{background:#fff;color:#000}
  .hero h1{color:#000}
}
"""


def ex_card(e):
    code, name, blk, area, tim, setup, howto, cps, step = e
    svg = SV.get(code, "")
    cp = "".join(f"<li>{esc(c)}</li>" for c in cps)
    stepdiv = ""
    if step and step != "—":
        stepdiv = f'<div class="step"><b>Nivåanpassning</b><br>{esc(step)}</div>'
    # Utan diagram får texten hela bredden — en tom grå ruta ser ut som ett fel.
    figdiv = f'<div class="ex-fig">{svg}</div>' if svg else ''
    return f'''<article class="ex" id="ex-{code}">
<div class="ex-top">
{figdiv}
<div class="ex-body">
<span class="ex-code">{esc(code)}</span>
<h3>{esc(name)}</h3>
<div class="meta">{esc(BLOCKNAME.get(blk,blk))} &nbsp;·&nbsp; {esc(area)} &nbsp;·&nbsp; {esc(tim)}</div>
<p><b>Så sätter du upp det.</b> {esc(setup)}</p>
<p><b>Så gör de.</b> {esc(howto)}</p>
</div></div>
<div class="cp"><h4>Coachpunkter</h4><ul>{cp}</ul>{stepdiv}</div>
</article>'''


def ses_card(s):
    rows = ""
    for tm, code, txt in s['slots']:
        if code in exlookup:
            cd = f'<a href="#ex-{code}">{code}</a>'
        elif code == "11+":
            cd = '<span>11+</span>'
        else:
            cd = '<span>·</span>'
        rows += (f'<div class="row"><div class="tm">{esc(tm)}</div>'
                 f'<div class="cd">{cd}</div>'
                 f'<div class="wt">{esc(txt)}</div></div>')
    br = " bridge" if "→" in s['block'] else ""
    return f'''<article class="ses{br}" id="p{s['n']}">
<div class="ses-h"><span class="pid">P{s['n']}</span>
<span class="d">{esc(s['day'])} {esc(s['date'])}</span>
<span class="t">{s['dur']} MIN · {esc(s['pitch'])}-PLAN · BLOCK {esc(s['block'])}</span></div>
<div class="ses-th"><b>{esc(s['theme'])}</b></div>
<div class="spine">{rows}</div>
<div class="focus"><b>Fokus</b>{esc(s['focus'])}</div>
</article>'''


# key legend mini svgs
def mini(inner, w=34, h=26):
    return (f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}">'
            '<defs><marker id="m1" viewBox="0 0 10 10" refX="8" refY="5" '
            'markerWidth="5" markerHeight="5" orient="auto-start-reverse">'
            '<path d="M0,1 L9,5 L0,9 z" fill="#10161C"/></marker></defs>'
            + inner + '</svg>')

KEY = [
 (mini('<circle cx="17" cy="13" r="10" fill="#1B3A6B" stroke="#fff" stroke-width="2"/>'), "Spelare / anfallare"),
 (mini('<circle cx="17" cy="13" r="10" fill="#A85B2B" stroke="#fff" stroke-width="2"/>'), "Försvarare / motståndare"),
 (mini('<circle cx="17" cy="13" r="5" fill="#fff" stroke="#10161C" stroke-width="2"/>'), "Boll"),
 (mini('<path d="M17,4 L24,19 L10,19 z" fill="#A85B2B"/>'), "Kon"),
 (mini('<line x1="3" y1="13" x2="30" y2="13" stroke="#10161C" stroke-width="2.5" marker-end="url(#m1)"/>'), "Löpning utan boll"),
 (mini('<line x1="3" y1="13" x2="30" y2="13" stroke="#1B3A6B" stroke-width="2.5" stroke-dasharray="6 4" marker-end="url(#m1)"/>'), "Passning"),
 (mini('<path d="M3,13 Q9,5 15,13 Q21,21 29,13" fill="none" stroke="#10161C" stroke-width="2.5" marker-end="url(#m1)"/>'), "Föra bollen"),
 (mini('<rect x="4" y="10" width="26" height="6" fill="#10161C" rx="2"/>'), "Mål"),
]

keyhtml = "".join(f'<div>{sv}<span>{esc(t)}</span></div>' for sv, t in KEY)

exhtml = "".join(ex_card(e) for e in EX)

# sessions grouped by week
seshtml = ""
curw = None
for s in S:
    if s['w'] != curw:
        curw = s['w']
        blk = s['block']
        seshtml += f'<div class="wk">Vecka {curw} &nbsp;—&nbsp; Block {esc(blk)}</div>'
    seshtml += ses_card(s)

HTML = f'''<!DOCTYPE html>
<html lang="sv"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Kopparspelet — Träningsplan höst 2026, P9</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@400;500;600;700&family=Source+Sans+3:ital,wght@0,400;0,600;0,700;1,400&family=IBM+Plex+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>{css}</style></head><body>

<header class="hero"><div class="wrap">
<div class="eyebrow">Åtvidabergs FF · Pojkar 9 år · Höstsäsong 2026</div>
<h1>Koppar<em>spelet</em></h1>
<div class="sub">26 träningspass, 13 veckor, tre block. Tisdagar 90 minuter,
cirka 18 spelare, 7-mot-7-planen. Torsdagar 60 minuter, cirka 13 spelare,
5-mot-5-planen. Byggd för två till tre tränare. Varje övning har en bild,
varje pass en tidslinje.</div>
<div class="tri">
<div><strong>Boll</strong><span>Vi vill ha bollen. Vi rensar aldrig i första hand.</span></div>
<div><strong>Mod</strong><span>Vi går 1 mot 1. Att våga och misslyckas är alltid rätt.</span></div>
<div><strong>Press</strong><span>Tappar vi den tar vi den tillbaka direkt.</span></div>
</div>
</div></header>

<nav><div class="wrap">
<a href="#sa">Så använder du planen</a>
<a href="#bemanning">Bemanning</a>
<a href="#malvakt">Målvakt</a>
<a href="#match">Matchspel</a>
<a href="#nyckel">Teckenförklaring</a>
<a href="#ovningar">Övningsbank</a>
<a href="#pass">Alla 26 pass</a>
<a href="#matning">Mätning &amp; test</a>
<a href="#feedback">Feedback</a>
</div></nav>

<div class="wrap">

<section id="sa"><div class="shead"><span class="num">01</span><h2>Så använder du planen</h2></div>
<p class="lede">Två pass i veckan som gör olika saker. Tisdagen introducerar och breddar.
Torsdagen komprimerar och upprepar. Kör inte samma pass två gånger.</p>

<div class="call"><h4>Vad planen är till för</h4>
<p><b>Att spelarna ska bli bättre på fotboll.</b> Alla som vill spela är välkomna hit, men vi är
en fotbollsträning — inte en aktivitet som fyller en tisdagskväll. Skillnaden syns aldrig i vem
som får komma. Den syns i vad vi gör med timmarna när de är här.</p>
<p>Det spelar roll, för i gruppen finns spelare som verkligen vill bli bättre. De hörs sällan mest,
de förlorar mest på ett rörigt pass, och de är de första att tröttna om träningen inte ger dem något.</p>
<p><b>Ett pass som inte utvecklade någon är ett misslyckat pass, även om alla hade kul.</b>
Roligt är ett medel, inte ett kvitto. Frågan efter varje pass är: vad kan någon nu som hen inte
kunde innan? Hela resonemanget står i <span class="mono">02-sa-tranar-vi.md</span>.</p></div>

<table>
<tr><th style="width:22%"></th><th>Tisdag · 90 min · ~18 spelare</th><th>Torsdag · 60 min · ~13 spelare</th></tr>
<tr><td class="mono">Roll</td><td>Introducera och bredda</td><td>Komprimera och upprepa</td></tr>
<tr><td class="mono">Yta</td><td>7-mot-7-planen, delad i tre banor (se TRK)</td><td>5-mot-5-planen, två banor</td></tr>
<tr><td class="mono">Tyngdpunkt</td><td>Nytt tema, variation, större spel sist</td><td>Volym. Bollkontakter per minut.</td></tr>
<tr><td class="mono">Stationer</td><td>Tre — en per tränare</td><td>Två</td></tr>
<tr><td class="mono">Bäst för</td><td>Bredd och nytt tema — passar hela gruppen</td><td><b>De fyra–fem som ligger efter</b> — färre spelare och trängre yta tvingar in dem på bollen</td></tr>
<tr><td class="mono">Pratbudget</td><td>Max tre stopp</td><td>Ett stopp. Helst noll.</td></tr>
</table>

<div class="call"><h4>Blockstruktur</h4>
<p><b>Block A, vecka 1–4 — Föra bollen.</b> Bollmästeri i rörelse, med syfte.
Det är den version av bollmästeri de faktiskt engagerar sig i.</p>
<p><b>Block B, vecka 5–8 — 1 mot 1.</b> Byggs direkt ur A. Åldersgruppens mest
värdefulla enskilda färdighet, och den mest motiverande.</p>
<p><b>Block C, vecka 9–12 — Första touchen och titta före.</b> Förbereder
7 mot 7 nästa år, där bollen kommer längre ifrån och senare.</p>
<p><b>Bryggveckor är 4, 8 och 12.</b> Nytt tema i övningen, gammalt tema kvar i spelet.
Inga tvära byten. De känns igen på kopparfärgad rubrik.</p></div>

<div class="call"><h4>Det viktigaste beslutet i hela planen</h4>
<p>Bollmästeri körs <b>inte</b> som ett block. Det körs som ankomstaktivitet, varje pass,
hela hösten. Boll var, rullande start, ingen instruktion, inget krav.</p>
<p>Ingenting begärs, alltså vägras ingenting. De som älskar det jobbar. De som inte gör det
busar med en boll — vilket ändå är tvåhundra bollkontakter. Tio till femton minuter
gånger 26 pass är fem till sex timmar bollkontakt under hösten. Ett fyraveckorsblock
hade gett dig nittio minuter.</p></div>

<div class="call"><h4>Varningen: fri lek är inte samma sak som tom yta</h4>
<p>Den vanligaste kraschen i ankomstaktiviteten är att alla ställer sig på led vid stora målet
och skjuter. Då försvinner hela vinsten — tio spelare vid ett mål ger en bollkontakt var
trettionde sekund.</p>
<p>Det är inget uppförandeproblem. <b>Ett mål är en magnet, och en tom yta med ett mål i
är i praktiken en instruktion att skjuta.</b> Miljön säger åt dem vad de ska göra, och de lyder.</p>
<p>Lösningen är inte att förbjuda skjutandet utan att <b>mångfaldiga målen</b>: sex konmål
utspridda, stora målet utanför ytan. Skjutandet finns kvar som belöning, kön försvinner,
och sträckan mellan målen blir bollkontakterna. Se ANK i övningsbanken.</p></div>
</section>

<section id="bemanning"><div class="shead"><span class="num">02</span><h2>Bemanning och gruppindelning</h2></div>
<p class="lede">Att ni är två eller tre tränare är den enskilt största tillgången ni har.
Utnyttjad rätt förändrar den både vad ni kan träna och hur mycket var och en behöver förbereda.</p>

<div class="call"><h4>Karusellen — och varför den sparar er tid</h4>
<p>Tre stationer bredvid varandra, en tränare vid varje. Grupperna roterar medsols
var sjunde minut. <b>Tränaren står kvar, gruppen flyttar.</b></p>
<p>Det betyder att var och en av er bara behöver kunna <b>en</b> övning per pass, inte fem.
Ni läser er egen ruta i övningsbanken, kör den tre gånger, och blir bra på den.
För en ideell tränare är det skillnaden mellan tjugo minuters förberedelse och två.</p>
<p><b>Huvudtränaren är passvärd</b>, varje pass: sätter konerna innan någon kommer, håller tiden,
ropar rotation, avgör när något ska brytas och tar hand om den som behöver två minuters paus.
Rollen roterar inte. Passets ramar ska se likadana ut varje vecka, och det är det som gör att
ni andra kan gå direkt till er station och göra er övning bra i stället för att hålla reda på klockan.</p></div>

<h3 style="font-size:22px;text-transform:uppercase;margin:26px 0 10px">Så delar ni truppen</h3>
<table>
<tr><th>Antal</th><th>Bästa format</th><th>Kommentar</th></tr>
<tr><td class="mono">16–20</td><td>3 mot 3 på tre banor</td><td>Går jämnt ut. Ingen står still, ingen väntar. Det här är tisdagens grundformat.</td></tr>
<tr><td class="mono">16–20</td><td>5 mot 5 + 4 mot 4, med målvakt</td><td>Sista kvarten på tisdagen. Två banor, riktiga eller konmål.</td></tr>
<tr><td class="mono">15–18</td><td>Tre stationer à 5–6 spelare</td><td>Torsdagens karusell. En ledare per station, sex minuter, rotation medsols.</td></tr>
<tr><td class="mono">15–18</td><td><b>5 mot 5 + sidostation</b> (G4)</td><td><b>Torsdagens avslutning.</b> Tio spelar, resten kör en övning bredvid, rotera var sjätte minut. Sidogruppen ska få fler bollkontakter än de som spelar.</td></tr>
<tr><td class="mono">11–14</td><td>3 mot 3 på två banor + 1 joker</td><td>Jokern spelar med det lag som har bollen. Byt joker varannan minut — det är en eftertraktad roll, inte en reservplats.</td></tr>
<tr><td class="mono">11–14</td><td>4 mot 4 + sidostation</td><td>G4 med mindre lag. Samma rotation.</td></tr>
</table>

<div class="call"><h4>Sätt grupperna på nytt varje vecka</h4>
<p>Dra lott, dela på färg på västarna, eller räkna av. Aldrig fasta nivågrupper och aldrig
namn som går att rangordna.</p>
<p>Varje spelare behöver båda erfarenheterna under en säsong: att vara den starkaste i en grupp
och att vara bland de svagare i en annan. Den ena bygger ledarskap, den andra bygger utveckling.
Slumpade grupper ger det automatiskt, utan att någon tränare behöver fatta beslutet varje vecka.</p></div>
</section>

<section id="malvakt"><div class="shead"><span class="num">03</span><h2>Målvakt</h2></div>
<p class="lede">Att många vill stå i mål är en tillgång. Det betyder att ingen fastnar där,
och att ni kan rotera fritt utan att någon känner sig bestraffad.</p>

<div class="two">
<div class="call"><h4>Regler för hösten</h4>
<p>Alla som vill får prova, och alla provar minst en gång. <b>Ingen är fast målvakt före tolv års ålder.</b>
Ingen står i mål mer än halva ett pass eller halva en match. Den som stått ska alltid ut och spela
utespelare i samma pass.</p></div>
<div class="call"><h4>Målvakt är inte en parkeringsplats</h4>
<p>Den vanligaste missen i barnfotboll är att den svagaste spelaren hamnar i mål för att det
verkar snällt. Det ger färre bollkontakter, inte fler. Om någon av de fyra–fem som ligger efter
gärna står i mål — bra, men se till att de spelar ute lika mycket.</p></div>
</div>

<div class="call"><h4>Om falltekniken och FIFA 11+ Kids</h4>
<p>Fallteknik finns i FIFA 11+ Kids — det är <b>övning 7, "Roll Over"</b>, med fem
progressionssteg från långsam gång till snabb rullning från stående, 5–7 gånger per sida.
Den heter alltså inte "fallteknik" i programmet, vilket är varför den lätt missas.</p>
<p><b>Men det är inte samma sak som målvaktsfall.</b> Roll Over är en framåtrullning
över axeln som tar upp fart i ett fall framåt — en allmän fotbollsfärdighet som skyddar
handleder och huvud. Målvaktens fall är något annat: ett kontrollerat sammansjunkande
<i>i sidled</i>, där kroppen landar längs hela sidan och bollen hålls kvar.</p>
<p>Uppvärmningen bygger alltså vanan att gå till marken utan att ta emot med händerna.
MV2 lär ut den sidledsvariant som rotationen i mål faktiskt kräver. Kör båda.</p></div>

<div class="call"><h4>Målvakten och BOLL</h4>
<p>Det viktigaste ni lär ut i mål den här åldern är inte räddningar. Det är att
<b>målvakten är första anfallaren</b>. Hen rullar eller passar ut, hen tar emot bakåtpassningar
med foten, hen rensar aldrig i första hand. Det är klubbens spelidé vid sin källa,
och det är MV3 i övningsbanken.</p>
<p>Målvaktsstationen ligger med i karusellen på ungefär varannan tisdag. Det betyder att alla
hela truppen får grunderna under hösten — vilket är precis vad som behövs när ni roterar.</p></div>

<div class="call"><h4>Om målen</h4>
<p>Använd <b>konmål eller små mål i alla spel</b>. Ett fullstort mål bakom en niåring gör
målvakten uppgiven och matchen orättvis.</p>
<p>De stora målen används till <b>målvaktsstationen</b> — MV1 och MV3 — där en tränare servar
och det inte handlar om att förhindra mål. Där är den stora ramen en fördel: det finns plats
att falla, sträcka sig och röra sig utan att krocka med stolpen.</p></div>

</section>

<section id="match"><div class="shead"><span class="num">04</span><h2>Matchspel och matchförberedelse</h2></div>
<p class="lede">Hösten har fem match- och cupdagar, varav två i 7 mot 7. Spelarna vill
dessutom spela på hel plan. Allt det löses av samma sak: G3 ligger sist i varje pass —
men den är inte samma sak varje vecka längre, den följer en trappa fram till matcherna.</p>

<table>
<tr><th>Datum</th><th>Vad</th><th>Spelform</th><th>Passet före</th></tr>
<tr><td class="mono">16 aug</td><td>Cup</td><td>5 mot 5</td><td><a href="#p4">P4</a> — inget nytt</td></tr>
<tr><td class="mono">30 aug</td><td>Cup</td><td>5 mot 5</td><td><a href="#p8">P8</a> — inget nytt</td></tr>
<tr><td class="mono">13 sep</td><td>Cup</td><td>5 mot 5</td><td><a href="#p12">P12</a> — lätt pass</td></tr>
<tr><td class="mono">26 sep</td><td><b>Träningsmatch</b></td><td><b>7 mot 7</b></td><td><a href="#p16">P16</a> — generalrepetition</td></tr>
<tr><td class="mono">10–11 okt</td><td><b>Cup, två dagar</b></td><td><b>7 mot 7</b></td><td><a href="#p20">P20</a> — generalrepetition</td></tr>
</table>

<div class="call"><h4>Så förbereds 7 mot 7</h4>
<p>Träningsmatchen spelas 26 september och cupen 10–11 oktober. <b>Blocken ändras inte för
det.</b> A, B och C ligger kvar — ett tema behöver tre till fyra veckor och cuper är inget
skäl att bryta det. Hela förberedelsen ligger i G3-slotten, som finns sist i vartenda pass:</p>
<p><b>P4–P8</b> bara spel · <b>P9–P12</b> numren delas ut och roteras ·
<b>P13–P16</b> formen 2-3-1 · <b>P17–P20</b> bredden och sexan · <b>P21–P26</b> låt det sitta.</p></div>

<div class="call"><h4>Vad som skiljer en 7-mot-7-cup från en 5-mot-5-cup</h4>
<p><b>Ytan är större och avstånden längre.</b> Bollen måste färdas mellan spelare i stället
för genom dem. Det är därför C-blocket och bredden ligger där de ligger.</p>
<p><b>Fler nummer att rotera.</b> Sju positioner i stället för fem, och alla ska provas.</p>
<p><b>Målvakten spelar ut på riktigt.</b> Med mer yta bakom backarna blir utspelet både
farligare och mer värt. Vi rensar ändå inte i första hand — se skyddsreglerna.</p>
<p><b>De blir tröttare fortare.</b> Räkna med det på en tvådagarscup, och räkna med att
tisdagen efter ska vara ett lätt pass.</p></div>

<div class="call"><h4>Var G3 ligger</h4>
<p><b>Tisdagar, sista 12 minuterna.</b> Hel plan, 7 mot 7 med målvakt. Det är den delen
spelarna längtar efter och den fungerar bäst som belöning i slutet, inte som uppvärmning
i början.</p>
<p><b>Torsdagar, sista 12–15 minuterna.</b> Största möjliga yta. Har ni bara femmannaplanen
den dagen, kör 6 mot 6 med målvakt på hela den ytan i stället — det viktiga är att det
känns som match, inte att det är exakt sju.</p></div>

<div class="call"><h4>Tre saker, inte fler</h4>
<p>Frestelsen inför en cup är att lägga till taktik. Låt bli. G3 har tre coachpunkter
och de räcker hela hösten:</p>
<p><b>1. Håll bredden.</b> Sjuan och elvan står ute vid linjerna. Detta är det svåraste —
niåringar dras mot bollen som magneter. Ställ dem på plats med handen i stället för att ropa.</p>
<p><b>2. Sexan bakom bollen.</b> Det finns alltid någon i mitten bakom den som har bollen.</p>
<p><b>3. Målvakten spelar ut.</b> Rullar eller passar, rensar inte. BOLL vid källan.</p></div>

<h3 style="font-size:22px;text-transform:uppercase;margin:26px 0 10px">Veckan före cup eller match</h3>
<table>
<tr><th>När</th><th>Vad</th></tr>
<tr><td class="mono">Tisdag</td><td>Vanligt pass. Förläng G3 till 20 minuter. Låt alla prova det nummer de troligen spelar, och minst ett till.</td></tr>
<tr><td class="mono">Torsdag</td><td>Kort karusell, lång G3. Gå igenom numren en gång innan, säg ingenting under.</td></tr>
<tr><td class="mono">Matchdag</td><td>Alla spelar ungefär lika mycket. Alla provar flera nummer. Ingen tabell, inget snack om resultat efteråt.</td></tr>
</table>

<div class="call"><h4>Under matcherna</h4>
<p><b>Säg nästan ingenting.</b> Instinkten att ropa instruktioner är stark och nästan helt
kontraproduktiv. Heja. Ropa inte var de ska stå.</p>
<p><b>Rotera numren mellan matcherna i cupen.</b> Fem matcher är fem tillfällen att prova
olika positioner. Ingen ska spela samma nummer alla fem gångerna, inte heller den som
verkar passa bäst där.</p>
<p><b>Efteråt: prata om något någon provade.</b> Inte om resultatet. Se
<span class="mono">06-spelarna-och-vuxna.md</span>.</p></div>
</section>

<section id="nyckel"><div class="shead"><span class="num">05</span><h2>Teckenförklaring</h2></div>
<p class="lede">Samma symboler i alla bilder.</p>
<div class="key">{keyhtml}</div>
</section>

<section id="ovningar"><div class="shead"><span class="num">06</span><h2>Övningsbank</h2></div>
<p class="lede">{len(EX)} övningar, varav tre för målvakt. Färre övningar, fler upprepningar — ett barn
behöver möta en idé ett tjugotal gånger innan den är hens. Jaga inte nyheter.
Passen nedan hänvisar hit med kod. Kör ni karusell räcker det att varje tränare läser sin egen ruta.</p>
<div class="exgrid">{exhtml}</div>
</section>

<section id="pass"><div class="shead"><span class="num">07</span><h2>Alla 26 pass</h2></div>
<p class="lede">Tidslinjen till vänster är passets ryggrad. Kodrutan länkar till övningen.
Detta är en plan, inte ett kontrakt — väder, sjukdom och verkligheten tar tre eller fyra
av dem. Komprimera inte för att komma ikapp, fortsätt bara där du är.</p>
{seshtml}
</section>

<section id="matning"><div class="shead"><span class="num">08</span><h2>Mätning</h2></div>
<p class="lede">Kortversion. Hela resonemanget finns i <span class="mono">05-matning-och-utveckling.md</span> —
läs den innan första testdagen.</p>

<div class="call"><h4>Bevisstegen</h4>
<p><b>1. Kan i test</b> — tekniken finns, säger inget om spel.<br>
<b>2. Gör i spel när vi säger till</b> — lydnad, inte lärande.<br>
<b>3. Gör i spel när vi är tysta</b> — <b>detta är lärande.</b></p>
<p>Måste vi ropa "titta upp" för att det ska hända har det inte satt sig.
Därför mäter vi alltid utan att coacha under tiden.</p></div>

<h3 style="font-size:22px;text-transform:uppercase;margin:28px 0 10px">Kortet — fyra test, tre gånger</h3>
<table>
<tr><th>Test</th><th>Vad</th><th>Övning</th></tr>
<tr><td class="mono">T1</td><td>Grindar på 60 sek</td><td><a href="#ex-T1">T1</a></td></tr>
<tr><td class="mono">T2</td><td>Sulrullningar på 30 sek</td><td><a href="#ex-T2">T2</a></td></tr>
<tr><td class="mono">T3</td><td>10 skott med svag fot</td><td><a href="#ex-T3">T3</a></td></tr>
<tr><td class="mono">T6</td><td>10 bollar, säg siffran</td><td><a href="#ex-T6">T6</a></td></tr>
</table>
<p style="max-width:66ch">Testdagar: <a href="#p7">P7</a> 25 aug · <a href="#p15">P15</a> 22 sep ·
<a href="#p23">P23</a> 20 okt. Kortet är ett motivationsverktyg — varje spelare tävlar mot sin
egen förra siffra, aldrig mot någon annans.</p>

<h3 style="font-size:22px;text-transform:uppercase;margin:28px 0 10px">Observationerna — det som faktiskt svarar</h3>
<div style="background:var(--sand);padding:14px;border:1px solid var(--line);border-radius:4px;margin-bottom:18px">{SV["OBS"]}</div>
<table>
<tr><th>Obs</th><th>Vad vi räknar</th></tr>
<tr><td class="mono">O1</td><td>Av alla mottagningar: hur många föregicks av att spelaren vred huvudet bort från bollen?</td></tr>
<tr><td class="mono">O2</td><td>Av alla mottagningar: hur många gick första touchen framåt eller åt sidan?</td></tr>
</table>
<p style="max-width:66ch">Två minuter, en spelare, en tränare ur coachrollen. En spelare per tränare
per pass räcker för att hela truppen mäts var tredje vecka. <b>O1 är måttet att behålla
om vi bara orkar med ett.</b></p>

<div class="call"><h4>Tysta matchen</h4>
<p>En gång per block: fem minuter spel där alla ledare är helt tysta. Ingen coachning,
ingen uppmuntran, inga namn. Vi står still och tittar.</p>
<p>Det är den renaste observationen vi kan få — och första gången kommer den kännas
väldigt lång, vilket i sig säger något om hur mycket vi pratar.</p></div>

<div class="call"><h4>Vad vi aldrig gör</h4>
<p>Ingen resultatlista. Ingen rangordning. Aldrig underlag för lagindelning eller uttagning.
Ingen tvingas delta. Vi mäter aldrig bollinnehav.</p>
<p>Observationerna O1 och O2 stannar hos tränarna — de är ett mått på <b>vår</b> träning,
inte på barnet. Kortet tillhör spelaren.</p></div>
</section>

<section id="feedback"><div class="shead"><span class="num">10</span><h2>Utvärdera och vidareutveckla</h2></div>
<p class="lede">Planen är ett utkast som ska mötas av verkligheten. Allt är numrerat så att
återkoppling kan bli exakt: övningar har kod (A3, B2, MV1, T3), pass har nummer (P1–P26).
Skriv i marginalen, ta upp det på ledarträffen, och låt nästa säsongs plan bli bättre.</p>
<div class="two">
<div class="call"><h4>Håller karusellen ihop?</h4>
<p>Sju minuter per station, tre rotationer, cirka 22 minuter totalt. Om övergångarna
äter tid — testa nio minuter och två rotationer istället. Färre byten, längre på varje
station. Utvärdera efter de två första passen.</p></div>
<div class="call"><h4>Stämmer spelformaten mot truppen?</h4>
<p>Tre banor à 3 mot 3 förutsätter arton närvarande. Blir det femton en tisdag är det
två banor plus en 4 mot 3, eller två banor och en jokergrupp. Notera hur det faktiskt
ser ut — det styr nästa säsongs upplägg.</p></div>
<div class="call"><h4>Är målvaktsstationen rätt doserad?</h4>
<p>Nu ligger den på ungefär varannan tisdag. Är intresset stort kan den ligga varje tisdag,
men då försvinner en fältstation. Laget avgör.</p></div>
<div class="call"><h4>Är övningsbanken begriplig?</h4>
<p>Planen körs av flera ledare. Om en ruta i övningsbanken är otydlig för någon som inte
varit med och skrivit den är det ett fel i texten, inte hos ledaren. Notera vilken kod
det gäller så kan rutan skrivas om inför nästa säsong.</p></div>
</div>
<div class="call" style="margin-top:20px"><h4>Vad som lämnas vidare</h4>
<p>Efter säsongen lämnas tre saker till fotbollsutvecklaren: vilka övningskoder som
fungerade och vilka som inte gjorde det, hur närvaron såg ut, och truppstorleken i
augusti jämfört med oktober. Det är underlaget för nästa årskull — och det är så
övningsbanken blir bättre från år till år i stället för att skrivas om varje säsong.</p></div>
</section>

<footer>
<p><b>Kopparspelet · Träningsplan höst 2026 · P9 · Åtvidabergs FF</b><br>
P9 · höst 2026 · lagpärmen. Bygger på 01-sa-spelar-vi.md och 02-sa-tranar-vi.md.<br>
Bygger på Svenska Fotbollförbundets spelarutbildningsplan och Fotbollens spela, lek och lär,
FIFA 11+ Kids, samt klubbens spelidé. Systerdokument: 01-sa-spelar-vi.md, 02-sa-tranar-vi.md, 05-matning-och-utveckling.md.</p>
<p style="margin-top:14px">I barnfotbollen räknas ingen tabell. Alla spelar ungefär lika mycket.
Alla provar alla positioner. Ett dribblingsförsök är aldrig ett misstag.</p><p style="margin-top:14px;padding-top:12px;border-top:1px solid var(--line)"><b>Skrivet av Albin Sidås</b>, tränare för P9 i Åtvidabergs FF. Materialet är hans eget och är <b>inte Åtvidabergs FF:s officiella träningsmaterial</b> — det uttalar sig inte för föreningen, och andra lag i ÅFF arbetar på sina sätt. Frågor eller något som behöver lyftas: <span class="mono">albinsidas@gmail.com</span></p>
</footer>

</div></body></html>'''

with open('../04-sasongsplan-host-2026.html', 'w', encoding='utf-8') as f:
    f.write(HTML)

print("written", len(HTML), "chars |", len(S), "sessions |", len(EX), "exercises")
