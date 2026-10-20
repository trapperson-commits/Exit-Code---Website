# Netlify-kiadás

A `netlify.toml` a `node scripts/build-site.mjs` paranccsal készíti el a `dist/` kiadási mappát. Nem igényel npm-függőségeket.

- A kiadási kezdőlap a jóváhagyott `koncepcio-3-szabad-ter.html` másolata, előnézeti navigáció nélkül.
- A koncepcióválasztó, elvetett koncepciók, fel nem használt képek és belső projektjegyzetek nem kerülnek a kiadási mappába.
- A helyi források és képváltozatok megmaradnak.
- A kézi Netlify-feltöltéshez a `dist/` mappa tartalma használható; GitHub-integrációnál a Netlify a konfiguráció alapján buildel.
- A Google Fonts külső betöltésű marad. A prototípus Tailwind Play CDN-je eltávolítva a kiadásból, mivel az oldal teljes stílusát saját CSS adja.
- Az Insane és Perfect zenék publikált, letölthető WAV-fájlként kerülnek a kiadásba. A koncertekhez továbbra sincs megadott dátum. Az oldal jelenleg angol nyelvű.
- A kiadási csomag előkészítése nem jelent automatikus közzétételt.
