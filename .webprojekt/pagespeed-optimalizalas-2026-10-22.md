# Mobilos PageSpeed-optimalizálás — csak helyben

Forrás: https://pagespeed.web.dev/analysis/https-exitcode-band-hu/8b6xa1t8jy?form_factor=mobile
Jelentés: 2026-10-22 17:12 CEST. Teljesítmény 86, accessibility 96, best practices 100, SEO 100. FCP 2,6 s; LCP 3,5 s; TBT 10 ms; CLS 0; Speed Index 3,6 s.

Jelzett fő problémák: renderblokkolás (1650 ms becslés, Google Fonts CSS 780 ms), túlméretes képek (273 KiB becsült megtakarítás), kontraszt (brand-origin, hero-heading), rövid cache-élettartam (11 KiB), kényszerített újraszámítás.

Elvégzett helyi változtatások:
- Az eredeti Manrope és Lora fontok megmaradtak. A Google Fonts CSS preload után aszinkron stylesheetre vált; JavaScript nélkül noscript fallback. Nem akadályozza az első kirajzolást.
- Tailwind CDN eltávolítva a munkaforrásból is; a kiadásban eddig sem volt rá szükség.
- 22 új szürkeárnyalatos WebP-másolat, srcset és sizes a 7 img elemen, az eredetiek megőrzésével. A szólogó SVG-koordinátái változatlanok.
- Build módosítva: az összes srcset fájlt másolja a dist-be.
- A from Berlin és a főmondat világosabb szürke, finom árnyékkal. A skip link sötét szöveget kapott a fehér felületén.
- ResizeObserver borderBoxSize alapján méri a fejlécet, nem végez szinkron getBoundingClientRect olvasást az observerben.
- Netlify images cache 1 hét, újraellenőrzéssel; nincs immutable, mert az URL-ek nem hash-eltek. Ez csak későbbi közzétételkor lép hatályba.

Ellenőrzés: build sikeres; 7 srcset összes fájlja létezik a dist-ben. Mobil 412×915 nézetben nincs vízszintes túlcsordulás, mindkét nyitófotó 480w változatát tölti. Galéria késleltetett betöltése és mobilmenü működik, törött képet nem találtunk. A betűstíluslap sikeresen stylesheetre vált.

Az öt 480px fotó összesen 79 562 bájt a korábbi 330 502 bájthoz képest (75,9% csökkenés). Ez fájlméret-összehasonlítás, nem minden eszközre vonatkozó hálózati mérés: nagyobb pixelsűrűségen a böngésző nagyobb változatot választ.

Új Lighthouse/PageSpeed pontszám nincs: az éles oldal változatlan, nem publikáltuk. A korábban jóváhagyott 3,45 s belépőanimáció és SVG sziklaháttér megmaradt; ezek is befolyásolhatják a későbbi mérést. Pontszámjavulás nem garantált. Nincs commit, push, vagy Netlify feltöltés.

## Véglegesítési emlékeztető

A felhasználó külön kéri, hogy a véglegesítéskor jelezzük az új teljesítménytesztet és optimalizálást. Élesítés előtt helyi ellenőrzés; PageSpeed az aktuális változat elérhető előnézetén, vagy ha nincs ilyen, élesítés utáni ellenőrzés. Publikálás és commit kizárólag külön jóváhagyással.
