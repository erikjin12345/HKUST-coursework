# HKUST coursework

Kod, anteckningar och kursmaterial för kurserna jag läser på HKUST.

## Struktur

Varje kurs har en egen mapp. Inuti den ligger:

- `code/` – notebooks, skript och data som hör till koden
- `pdf/` – slides, problem sets och lösningar
- `html/` – fristående HTML-sidor med härledningar; öppna `index.html` i en webbläsare
- `CHEATSHEET.md` – formelsamling per kurs med sidhänvisningar till föreläsningsanteckningarna

```
FINA 2203/
  code/
MATH 4432/
  code/MATH-4432-Statistical-Machine-Learning/   (submodul: kursens officiella tutorial-repo)
MATH 4511/
  code/   MATH 4511.ipynb, MATH_4511_functions.py
  pdf/    föreläsningsanteckningar, problem sets, lösningar
MATH 4515/
  code/   MATH_4515.ipynb, aktiedata (xlsx)
  pdf/    föreläsningsanteckningar, problem sets, lösningar
misc/     småtester
web/      Vite + React-app som renderar repots markdown med LaTeX (KaTeX)
```

## Markdown- och LaTeX-visare

```
cd web && npm install && npm run dev
```

Öppnar `http://localhost:8010`. Menyn listar alla `.md`-filer i repot per kurs samt scratch-sidor i `web/content/`. Se `CLAUDE.md` för hur den används.

## Submodul

MATH 4432 använder kursens repo som submodul. Efter en ny klon:

```
git submodule update --init
```
