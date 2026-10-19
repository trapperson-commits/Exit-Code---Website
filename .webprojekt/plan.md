# Exit Code – három kezdőoldal-koncepció terve

Állapot: a felhasználó jóváhagyta; mindhárom prototípus elkészült.

## Közös alap

Berlini nu metal duó: Ádám gitáros, Zsolt dobos. A korlátokon túllépés, a remény, a természet tisztelete és a közösség ereje a márka alapja. Angol nyelvű kezdőoldal-prototípusok készülnek; a végleges oldal német és magyar változatra is felkészítendő. A koncepciókhoz javasolt elsődleges CTA: Listen; másodlagos: Upcoming shows. Ez prototípus-döntés, nem korábban megerősített prioritás.

Mindhárom monokróm, alapvetően világosabb kő- vagy márványhatású felületet kap. A különbség a kompozíció, a képi ritmus és a tipográfia, nem színes témaváltás. Kizárólag a külön portrékból választott 3 Ádám- és 3 Zsolt-fotó, valamint a jóváhagyott kész logó használható. Minden fotó fekete-fehér CSS-megjelenítést kap, az eredetik megőrzésével. A pontos válogatást vizuális ellenőrzés előzi meg.

## 1. Kőbe vésett

Világos, finoman erezett kőfelület előtt két nagy, függőleges portré alkot osztott nyitókompozíciót. Széles térközök, éles képkeretek, erős méretkontraszt és közvetlenül elérhető zenék. A nyitóképen a két jelenlegi tag jelenléte dominál.

- Paletta: primary #000000; secondary #454545; accent #B8B8B8; bg #ECECEC; surface #FFFFFF; text #181818; muted #595959.
- Betűterv: Oswald címsor, Source Sans 3 törzsszöveg; a fontelérhetőség és ékezetkészlet ellenőrzendő a megvalósításkor.
- Elrendezés: osztott hero, balra igazított szöveg; lent tágas zenei rész, váltakozó fotók és bemutatkozás.
- Emlékezetes elem: a két portré monumentális, páros kompozíciója.
- Márkakapcsolat: két alkotó, két hangszer, közös irány; közvetlen, ütős bemutatkozás.

## 2. Törésvonal

Tipográfiára épülő, aszimmetrikus nyitó rész: a korlátokon túllépő üzenet nagy, sűrített betűkkel, mellette és részben mögötte eltolt portrók. Grafitszürke hangsúlyos blokkok váltakoznak világos betonhatású felületekkel. Feszesebb ritmus, egymásra rétegzett képek, koncentrált energia; az oldal összességében világos marad.

- Paletta: primary #000000; secondary #333333; accent #949494; bg #DADADA; surface #F5F5F5; text #101010; muted #505050.
- Betűterv: Barlow Condensed címsor, IBM Plex Sans törzsszöveg; ellenőrzendő fontelérhetőség és ékezetkészlet.
- Elrendezés: tipografikus hero, eltolt fotók; tömör, horizontális zenelista és aszimmetrikus galéria.
- Emlékezetes elem: a megszakadó képi tengely és a nagy, kereteken túlnyúló üzenet.
- Márkakapcsolat: a név jelentését kompozícióval fejezi ki, villogás és káosz nélkül.

## 3. Szabad tér

Fotóvezérelt, nyugodtabb nyitó rész: széles képi sávban két külön portró, sok világos térrel és finom szürke kőtextúrával. Könnyedebb címbetűk, visszafogott méretkontraszt és hosszabb vizuális szünetek. A zenék után a közös gondolat és az alapítók személyes bemutatása kap nagyobb hangsúlyt.

- Paletta: primary #202020; secondary #646464; accent #CDCDCD; bg #F4F4F4; surface #E7E7E7; text #202020; muted #5A5A5A.
- Betűterv: Manrope címsor, Lora törzsszöveg; ellenőrzendő fontelérhetőség és ékezetkészlet.
- Elrendezés: széles fotós hero, középre rendezett rövid nyitóüzenet; lent tágas, váltakozó kép–szöveg szakaszok, finoman lekerekített képablakok.
- Emlékezetes elem: levegős portrépanoráma és a közösségi üzenet személyes közelsége.
- Márkakapcsolat: az erős zene mögötti reményt, emberséget és kapcsolódást emeli ki.

## Mi készül a jóváhagyás után

- Három önálló, mobilon is megtekinthető statikus HTML-kezdőoldal Tailwind CSS-sel és irányspecifikus stílusokkal.
- Gyökérszintű `index.html` koncepcióválasztó, ahonnan mindhárom oldal megnyitható.
- Fájlok: `koncepcio-1-kobe-vesett.html`, `koncepcio-2-toresvonal.html`, `koncepcio-3-szabad-ter.html`.
- A helyi Insane és Perfect zenékhez kézi indítású lejátszás és letöltési lehetőség a helyi előnézetben. Ez nem nyilvános publikálás.
- Rövid About, a legfeljebb hat kiválasztott portré galériája, valódi e-mail és Facebook-link.
- Koncertadat nélkül rövid, tényszerű üres állapot; klipadat nélkül nincs kitalált videó vagy megjelenési időpont.
- Nincs működés nélküli nyelvváltó. E körben angol koncepciók készülnek; a teljes fordítás külön tartalmi lépés.
- Helyi Git-verziókövetés a skill projektfelállítási előírása szerint, forrásmédia tömeges verziózásának elkerülésével.
- Asztali és mobil megjelenítés, navigáció, képek és hivatkozások ellenőrzése.

## Megtekintés

A megépítés után az `index.html` a belépési pont. A felhasználó kiválaszthat egy irányt, vagy megjelölheti az egyes változatokból megtartandó elemeket.
