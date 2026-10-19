# Tervezési áttekintés – Exit Code

Dátum: 2026. október 19.
Fázis: meglévő brief átnézése és a nyitott tervezési döntések pontosítása. Végső jóváhagyás még nincs rögzítve.

## Átnézett anyagok

- Projektútmutató: `AGENTS.md`.
- Márkaüzenet, tartalom és vizuális megkötések: `.webprojekt/brief.md`.
- Fájllista és átnevezési jegyzék. A jegyzék történeti feljegyzés: a képek azóta a `Képek/` mappába kerültek, néhány arculati fájl neve is módosult. A tényleges fájlrendszer az aktuális útvonalak forrása.
- Nincs `state.json`, nincs meglévő weboldalkód és nincs megadott korábbi Exit Code-weboldal. A tervezés új honlapból indul.

## Aktuális anyagleltár

- 8 régi csoportkép: `Képek/Banda/Jók/`. A legújabb döntés szerint egyelőre nem használjuk őket. Később kizárólag Ádámot és Zsoltot mutató, megfelelő minőségű kivágás jöhet szóba; más korábbi tag nem látszódhat.
- 4 Ádám- és 4 Zsolt-portréjelölt: `Képek/Ádám/`, `Képek/Zsolt/`. Ezekből 3-3 jobb fotó választandó, összesen legfeljebb 6, fekete-fehér megjelenítéssel. A konkrét válogatás még hátravan.
- Jelenlegi felállás: Ádám – gitár; Zsolt – dob. A zenekar most kettőjükből áll.
- 3 jóváhagyott arculati kép: `Név_Logo_Weboldalhoz/Jók/`: `exit-code-arculat-jo-002.jpg`, `exit-code-arculat-jo-003.jpg`, `exit-code-LOGO_arculat-jo-001.jpg`. A végleges logó kiválasztásához vizuális ellenőrzés szükséges.
- 97 kizárt kép összesen: 92 a `Képek/Banda/Nem jók/`, további 5 a `Név_Logo_Weboldalhoz/Nem jók/` mappában. Az utóbbiba került a 006, 007 és 008 sorszámú arculati fájl, az erdőkép és a színes logó. Egyik sem kerülhet a honlapba, a fájlnévben megmaradt `jo` jelöléstől függetlenül.
- Két WAV-fájl: `Music - Zene/Insane - Exit Code.wav` és `Music - Zene/Perfect - Exit Code.wav`. A puszta fájllista nem hangminőség-ellenőrzés vagy publikálási jóváhagyás.
- Megadott kapcsolat: exitcode.theband@gmail.com és https://www.facebook.com/ExitCodeBerlin.
- Koncertlista, jegyhivatkozás és klip nincs a helyi fájlok között.

## Már rögzített irány

Berlinből induló nu metal, erőteljes hangzás és reményt adó, közösségi üzenet. Ádám és Zsolt közös alapítói gondolata: túllépni a korlátokon, önmagunkra találni, tisztelni egymást és a természetet. Monokróm, szellős felület; világosabb kő- vagy márványhatás; fekete-fehér fotók; angol alapnyelv, német és magyar változat lehetőségével.

## Döntési javaslatok – még nem jóváhagyottak

- Elsődleges művelet: Listen – azonnali továbblépés a zenékhez. Másodlagos: Upcoming shows; az e-mail és Facebook külön, jól látható kapcsolat.
- Első kiadás: egy áttekinthető oldal Home, Music, Live, About, Gallery és Contact navigációs pontokkal. A klipek tényleges tartalom érkezésekor a Music részben kapnak helyet.
- Koncertadat nélkül rövid tájékoztatás a Live részben, kitalált eseménykártyák nélkül. Megerősített klip nélkül külön üres videószekció ne készüljön.
- A többnyelvűség induláskori terjedelme még eldöntendő.

## Következő lépés

Először a látogatói fő célt pontosítjuk, utána az oldalstruktúrát és az induló tartalmakat. A kész brief összefoglalójának felhasználói jóváhagyása után menthető a `brief_complete` állapot. A prototípusépítés a generalas workflow külön lépése.
