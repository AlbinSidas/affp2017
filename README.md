# P9 — Åtvidabergs FF

**Träningsmaterialet för ett barnfotbollslag, öppet för vem som helst att läsa, använda och kopiera.**

Det här är hela arbetssättet för ett lag med arton pojkar födda 2017 i Åtvidabergs FF:
spelidén, hur passen byggs, 42 övningar med bild, en färdig säsongsplan, hur vi mäter om
träningen fungerar, och vad vi lovar spelarna och deras familjer.

Ingenting här är hemligt. Det är så vi vill arbeta, och det tål att läsas av vem som helst.

---

## Vem som står bakom materialet

Materialet är skrivet och ägs av **Albin Sidås**, tränare för P9 i Åtvidabergs FF.

> **Det här är inte Åtvidabergs FF:s officiella träningsmaterial.**
>
> Det uttalar sig inte för föreningen, för styrelsen eller för andra lag. Andra lag i ÅFF
> arbetar på sina sätt, och ingenting här ska läsas som att klubben tillämpar, har godkänt
> eller står bakom det som står här.

Det beskriver hur **ett** lag har valt att arbeta. Det är skrivet för att rymmas innanför
Svenska Fotbollförbundets riktlinjer för barnfotboll och innanför föreningens värdegrund —
men urvalet, tolkningarna och avvägningarna är mina egna, och jag svarar för dem.

Föreningens namn förekommer för att beskriva vilket lag materialet skrevs för, inte som
utgivare eller garant.

**Frågor, invändningar eller något som behöver lyftas — hör av dig direkt:**
[albinsidas@gmail.com](mailto:albinsidas@gmail.com)

**→ [Läs materialet](https://albinsidas.github.io/affp2017/)** 

---

## Vad du hittar var

### För tränare

| Dokument | Vad det är |
|---|---|
| [LASMIG.md](LASMIG.md) | **Börja här.** Kartan över allt annat. |
| [01-sa-spelar-vi.md](01-sa-spelar-vi.md) | Spelidén. Grunderna som aldrig ändras, och vårt uttryck av dem. |
| [02-sa-tranar-vi.md](02-sa-tranar-vi.md) | Vad träningen är till för, passets uppbyggnad, karusellen, förväntningar. |
| [03-ovningsbank.html](03-ovningsbank.html) | 42 övningar med diagram, uppställning och coachpunkter. |
| [04-sasongsplan-host-2026.html](04-sasongsplan-host-2026.html) | 26 färdiga pass med tidslinje. |
| [05-matning-och-utveckling.md](05-matning-och-utveckling.md) | Hur vi vet om träningen fungerar. |
| [06-spelarna-och-vuxna.md](06-spelarna-och-vuxna.md) | Nivåanpassning, stök, eget barn, mat, gränser. Utfästelserna i §5 styr allt annat. |
| [08-arshjul.md](08-arshjul.md) | Träningsperioder, temablock, aktiviteter, deadlines. |
| [09-positionsspel.md](09-positionsspel.md) | Positionsspel från 7 mot 7 och uppåt. |
| [11-metoden.md](11-metoden.md) | **Resonemanget bakom allt annat.** Varför övningarna och periodiseringen ser ut som de gör, hur en säsong planeras, och hur metoden bär upp i äldre åldrar. |

### För vårdnadshavare

| Dokument | Vad det är |
|---|---|
| [10-till-er-hemma.md](10-till-er-hemma.md) | Vad vi lovar, och vad vi behöver av er. |
| [07-matguide.html](07-matguide.html) | Mat och dryck runt träning, match och cup. |

### Att skriva ut

Fem PDF:er, byggda ur samma källor. Alla går att mejla som de är.

| Fil | Till vem | Omfång |
|---|---|---|
| [Lagparmen.pdf](Lagparmen.pdf) | Tränare | ~99 sidor |
| [Positionsspel.pdf](Positionsspel.pdf) | Tränare | ~27 sidor |
| [Metoden.pdf](Metoden.pdf) | Tränare | ~15 sidor |
| [Till-er-hemma.pdf](Till-er-hemma.pdf) | Vårdnadshavare | 7 sidor |
| [Matguide.pdf](Matguide.pdf) | Vårdnadshavare | 9 sidor |

---

## De fyra sakerna materialet vilar på

**1. Bollkontakter.** Ingen kö, någonsin. Fyra små banor slår en stor, varje gång.

**2. Blicken.** Att titta innan man får bollen. Gruppens tydligaste svaghet och den
största vinsten — och den kommer av frågor, aldrig av tillsägelser.

**3. Mod.** Ett dribblingsförsök är aldrig ett misstag. Det vi rättar är den säkra
bakåtpassningen, inte den misslyckade dribblingen.

**4. Att de blir bättre.** Träningen finns för att spelarna ska utvecklas som
fotbollsspelare. Ett pass som inte utvecklade någon är ett misslyckat pass, även om alla
hade kul.

---

## Vad materialet aldrig gör

Det här är bindande och står över allt annat i repot. Det följer svensk barnfotbolls
värdegrund och Svenska Fotbollförbundets riktlinjer för åldrarna 8–12.

- Ingen toppning, ingen tabellräkning — alla spelar ungefär lika mycket
- Ingen permanent nivåindelning, ingen selektering, inga fasta positioner
- Ingen fast målvakt före tolv år
- Inga test som rangordnar barn, inga resultatlistor
- Inga namn på enskilda spelare någonstans i materialet
- Aldrig kommentarer om ett barns kropp eller vikt

---

## Till andra lag i ÅFF — och alla andra

**Ta det. Forka det. Gör om det så att det passar er.**

Materialet är skrivet för ett lag, men nästan ingenting i det är unikt för just det laget.
Övningsbanken, årshjulet, mätningen och föräldrabrevet fungerar för vilken årskull som
helst — det är bara datum, spelform och truppstorlek som behöver bytas.

Om ni gör det bättre: hör gärna av er, eller skicka en pull request.

**Övnings-ID är avsiktligt fasta.** `A3` är Grindar, alltid, i varje dokument och varje år.
Ett ID återanvänds aldrig, så gamla säsongsplaner går att läsa. Behåll den regeln om ni
bygger vidare — det är den som gör att flera lag kan prata om samma övning.

---

## Bygga om filerna

De genererade filerna — `03`, `04`, `07`, `09`, `10`, `LAGPARMEN.html` och de fyra
PDF:erna — **redigeras aldrig för hand.** Ändra källan och bygg om:

```bash
cd _bygg
python bygg-allt.py
```

Ett kommando bygger allt, skriver ut PDF:erna och kontrollerar resultatet: samma
övnings-ID i alla filer, inga trasiga länkar, ingen kvarlämnad markdown, inga
hänvisningar till övningar som inte finns. Det avslutar med **ALLT OK** eller en lista
på problem.

Kräver Python 3 och en installerad Chrome eller Edge för PDF-utskriften. Inga andra
beroenden.

Övningar och pass redigeras i `_bygg/build.py`. Diagram ritas av `_bygg/nya_svgs.py`.
Se [CLAUDE.md](CLAUDE.md) för detaljerna.

---

## Katalogerna

```
/               dokumenten, PDF:erna och den byggda webbversionen
/_bygg          skripten som bygger allt
/_parkerat      material som ligger och väntar — se _parkerat/README.md
/_internt       arbetsdokument, följer inte med i repot
```

---

## Licens

[CC BY-SA 4.0](LICENSE) — använd, ändra och sprid fritt, även kommersiellt, så länge du
anger varifrån det kommer och delar vidare under samma licens.

Bygger på Svenska Fotbollförbundets spelarutbildningsplan och *Fotbollens spela, lek och
lär*, samt FIFA 11+ Kids.
