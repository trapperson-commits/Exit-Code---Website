# Exit Code – folytatási jegyzet

## Legfrissebb módosítás – 2026. november 27.

A kiválasztott koncepcio-3-szabad-ter.html fejlécének háttere ismét áttetsző, 80%-os sötétszürke fedéssel (rgba(45,45,45,.8)) és 2 px háttérhomályosítással, a korábbinál kevésbé átlátszó megjelenéshez. A fejléc sticky marad. A szójel és a nyitófotók belépőanimációját, előzetes rejtését és a hozzájuk tartozó JavaScriptet eltávolítottuk. A képeken nincs hover-nagyítás. A fájlok helyben mentve; publikálás és commit külön engedélyhez kötött.

Az alábbi október 19-i feljegyzés korábbi állapotot rögzít, a későbbi döntések az AGENTS.md-ben és a PageSpeed-jegyzetben találhatók.

Utolsó munkanap: 2026. október 19.

- A felhasználó a mai munkát lezárta; az aktuális megjelenést megtartjuk.
- A kiválasztott, szerkesztett honlap: `koncepcio-3-szabad-ter.html`.
- Helyi előnézet: `http://127.0.0.1:8766/koncepcio-3-szabad-ter.html`.
- A fájl böngészőből közvetlenül is megnyitható; a helyi szerver újraindítás után szükség esetén újraindítandó. A Tailwind CDN és Google Fonts internetkapcsolatot használ.
- A honlap és a használt képek a projektmappán belül vannak. A nagy eredeti médiafájlok szintén megmaradnak a mappában, de a Git figyelmen kívül hagyja őket.
- A jóváhagyott elrendezés két hagyományos nyitófotót használ. Az utóbb kipróbált háttér nélküli kivágásokat és kibővített galériát visszavontuk. A kivágások és a színes változatok fájljai megmaradnak az `images/uj-kepvaltozatok/` mappában.
- A mai legutolsó változtatás a kompakt lábléc: kisebb térközök, közelebbi elválasztó, bal oldali, fejlécméretű körlogó, mellette „Exit Code Berlin”.
- Nyilvános publikálás nem történt. A koncertekhez még nincs megadott dátum, a honlap angol nyelvű helyi változat.
- A részletes döntések a `brief.md` és a gyökérben lévő `AGENTS.md` végén követhetők; az újabb döntések felülírják a korábbiakat.

## Jóváhagyott közzététel – 2026. november 27.

A felhasználó kifejezetten engedélyezte minden módosítás commitolását, GitHub-feltöltését és Netlify-élesítését. Megerősített cél: trapperson-commits/Exit-Code---Website, master ág; exit-code-band Netlify-projekt; exitcode-band.hu. A build sikeres (35 eszközfájl). Chromium-ellenőrzés 390 és 1440 px szélességen sikeres: sticky fejléc, 80%-os szürke fedés, statikus nyitóelemek, mobilmenü működik, nincs túlcsordulás vagy hibás betöltött kép. Helyi mobilos Lighthouse: teljesítmény 68, hozzáférhetőség 100, best practices 100, SEO 100; TBT 1590 ms, LCP 3,0 s. A teljesítmény további javításra szorulhat. Közzététel után az éles állapot ellenőrizendő. A későbbi commitok és publikálások továbbra is külön engedélyhez kötöttek.
