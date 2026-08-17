# P9 — Åtvidabergs FF
## Lagpärmen

*För lagets tränare. Läs den här sidan först.*

---

## Vad det här är

Materialet för vårt lag. Inte för klubben, inte för framtida årskullar — för de pojkar vi har, den här säsongen och nästa.

Det är skrivet så att tränarna ska kunna dela på jobbet utan att någon behöver ha allt i huvudet. Den som håller station två på tisdag behöver läsa en ruta i övningsbanken, inget mer.

**Åtta dokument. Inget av dem längre än det behöver vara.**

Behöver du bara *ett* — läs `LAGPARMEN.html`. Där ligger allt nedanstående i en enda fil, byggd för att skrivas ut eller sparas som PDF.

---

## Vad som finns var

| Fil | Vad | När du läser den |
|---|---|---|
| **01-sa-spelar-vi.md** | BOLL · MOD · PRESS. Spelarprofil, numren, formationstrappan. | En gång, i början. Sen som repetition. |
| **02-sa-tranar-vi.md** | Passets uppbyggnad, karusellen, bemanning, blicken, vad vi lär ut. | Innan säsongsstart, och när något känns fel. |
| **03-ovningsbank.html** | 42 övningar med bild, uppställning och coachpunkter. | Före varje pass — bara din egen station. |
| **04-sasongsplan-host-2026.html** | 26 pass, augusti till oktober, med tidslinje. | Varje vecka. |
| **05-matning-och-utveckling.md** | Hur vi vet om träningen fungerar. Test, observationer, tysta matchen. | Innan första testdagen. Viktig. |
| **06-spelarna-och-vuxna.md** | Nivåanpassning, stök, eget barn, mat, gränser. | En gång ordentligt. Sen vid behov. |
| **07-matguide.html** | Infografik till vårdnadshavare: cup, träning, match, dryck. | Skickas ut inför cupen. |
| **08-arshjul.md** | Träningsperioder, temablock, aktiviteter, deadlines. | I augusti och i februari. |
| **09-positionsspel.md** | Hur laget står och varför, från 7 mot 7 och uppåt. Utbildning för oss. | Inför steget till 7 mot 7. Egen PDF. |
| **10-till-er-hemma.md** | Till vårdnadshavare: vad vi lovar, vad vi behöver. | Skickas ut inför varje säsong. Egen PDF. |
| **11-metoden.md** | Varför planen ser ut som den gör. Periodiseringen, vägen uppåt, tre pass i veckan. | När du ska planera en säsong — eller är oense med planen. Egen PDF. |

**MALL-sasongsplan.md** används när vi lägger vårens plan.

**LAGPARMEN.html** är allt ovanstående i en fil, för utskrift och PDF. Byggs av `_bygg/parm.py` — redigera aldrig den, redigera källorna.

---

## Att dela ut materialet

**Fyra filer, inte tio.**

| Till vem | Fil | Omfång | När |
|---|---|---|---|
| **Oss tränare** | `Lagparmen.pdf` | ca 95 sidor A4, ca 1,7 MB | Vid säsongsstart |
| **Oss tränare** | `Positionsspel.pdf` | 24 sidor, ca 430 kB | **Nu** — 7 mot 7 spelas i höst |
| **Vårdnadshavare** | `Till-er-hemma.pdf` | 7 sidor, ca 140 kB | Inför varje säsong |
| **Oss tränare** | `Metoden.pdf` | 15 sidor, ca 300 kB | Inför planering av en ny säsong |
| **Vårdnadshavare** | `Matguide.pdf` | 8 sidor, ca 250 kB | Inför cup |

Alla fyra går att mejla eller lägga i lagchatten som de är. Ingen behöver ladda ner en mapp, öppna flera filer eller ha rätt program — en PDF öppnas på vilken telefon som helst.

Nya PDF:er görs om från HTML-filerna när något ändrats:

```
cd _bygg
python bygg-allt.py
```

Ett kommando bygger alla html-filer, skriver ut alla fyra PDF:erna och kontrollerar
resultatet. **Skicka inget förrän det står ALLT OK.**

**Behöver någon bara en sida:** `01-sa-spelar-vi.md` slutar med en ettsida som är gjord för att skrivas ut och sättas upp i omklädningsrummet.

---

## Så delar vi upp det

**Passvärd** är huvudtränaren, varje pass. Passvärden sätter koner innan någon kommer, håller tiden, ropar rotation, avgör när något bryts och tar hand om den som behöver två minuters paus. Rollen roterar inte — ramarna ska se likadana ut varje vecka, och övriga ledare ska kunna komma direkt till sin station.

**Station** — var och en tar en station per pass och behöver bara kunna den. Det är hela poängen med karusellen: ingen behöver förbereda fem övningar.

**Observation** — en av oss kliver ur coachrollen två minuter per pass och tittar på en enda spelare. Se `05-matning-och-utveckling.md`.

Med tre tränare och en trupp på femton till tjugo spelare går det ihop utan att någon jobbar mer än en timme i veckan utanför planen.

---

## De fyra sakerna som betyder mest

Om allt annat faller bort, håll fast vid dessa.

**1. Bollkontakter.** Ingen kö, någonsin. Fler än två som väntar betyder att övningen är fel upplagd. Fyra små banor slår en stor, varje gång.

**2. Blicken.** Gruppens tydligaste svaghet och den största vinsten. Men den kommer inte av tillsägelser — den kommer av frågor, och av att touchen blir säkrare. Se `02-sa-tranar-vi.md`.

**3. Mod.** Ett dribblingsförsök är aldrig ett misstag. Det vi rättar är den säkra bakåtpassningen, inte den misslyckade dribblingen.

**4. Att de blir bättre.** Träningen finns för att spelarna ska utvecklas som fotbollsspelare — inte för att fylla en tisdagskväll. Ett pass som inte utvecklade någon är ett misslyckat pass, även om alla hade kul. Frågan efter varje pass är: *vad kan någon nu som hen inte kunde innan?* Se `02-sa-tranar-vi.md`.

Att de stannar kvar är fortfarande viktigt, och vi räknar truppen i mars mot oktober. Men det är en **följd** av bra träning, inte något vi köper genom att sänka kraven. Barn slutar lika ofta för att det är kravlöst och rörigt som för att det är hårt.

---

## Genererade filer

Fem filer byggs av skript och ska **inte** redigeras för hand:

| Fil | Byggs av |
|---|---|
| `03-ovningsbank.html` | `_bygg/bank.py` |
| `04-sasongsplan-host-2026.html` | `_bygg/build.py` |
| `07-matguide.html` | `_bygg/matguide.py` |
| `09-positionsspel.html` · `10-till-er-hemma.html` | `_bygg/doc.py` |
| `LAGPARMEN.html` | `_bygg/parm.py` |

Kör aldrig dem en och en — kör `python bygg-allt.py`, som gör allt och kontrollerar det.

Övningar och pass redigeras i `_bygg/build.py`, diagram i `_bygg/svgs.json`. Se `CLAUDE.md`.

**Övnings-ID är fasta.** A3 är Grindar, alltid, i alla dokument. Förbättras en övning skrivs rutan om — koden ändras aldrig. Säsongsplanen hänvisar till övningar med kod och skriver aldrig av dem.

---

## _parkerat

Här ligger materialet vi tog fram för klubben som helhet: organisationsförslag, akademibakgrund, årshjul för samordning mellan lag, och hela taxonomin över träningsområden.

**Det ligger parkerat, inte borttaget.** Vi har mer än nog att göra med vårt eget lag den här säsongen. Om det visar sig fungera hos oss, och om någon i klubben frågar, finns det där.

Det är också rätt ordning. Ett arbetssätt som bevisligen fungerar med en grupp nioåringar är ett argument. Ett dokument är det inte.

---

## Nästa år

**7 mot 7 kommer redan i höst.** Träningsmatch 26 september, cup 10–11 oktober. Numren är desamma, formationen blir 2-3-1, och det enda verkligt nya är att sjuan och elvan ska hålla bredden.

Därför spelar vi tio till femton minuter på hel plan i slutet av varje pass, och den slotten följer en trappa fram till matcherna. Se `09-positionsspel.md` och säsongsplanen. Steget ska kännas som mer av samma sak.

Däremellan ligger vintern, och i år tränar vi ute på konstgräs — ett pass i veckan, med kallelse, november till februari. Det är en riktig träningsperiod och ingen paus. Se `08-arshjul.md`.

Vårens plan skrivs i februari med `MALL-sasongsplan.md`.

---

## Vem som står bakom det här

Materialet är skrivet och ägs av **Albin Sidås**, tränare för laget. Det är **inte
Åtvidabergs FF:s officiella träningsmaterial** och uttalar sig inte för föreningen — andra
lag i ÅFF arbetar på sina sätt. Det beskriver hur det här laget har valt att arbeta.

Frågor eller något som behöver lyftas: albinsidas@gmail.com

---

*Version 3.2 · augusti 2026 · lagnivå*
