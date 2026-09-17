# HKUST coursework

Kod, anteckningar och kursmaterial för kurserna jag läser på HKUST.

## Struktur

Varje kurs har en egen mapp. Inuti den ligger:

- `code/` – notebooks, skript och data som hör till koden
- `pdf/` – slides, problem sets och lösningar
- `CHEATSHEET.md` – formelsamling per kurs med sidhänvisningar till föreläsningsanteckningarna

```
FINA 2203/
  code/
MATH 4423/
  code/MATH-4432-Statistical-Machine-Learning/   (submodul: kursens officiella tutorial-repo)
MATH 4511/
  code/   MATH 4511.ipynb, MATH_4511_functions.py
  pdf/    föreläsningsanteckningar, problem sets, lösningar
MATH 4515/
  code/   MATH_4515.ipynb, aktiedata (xlsx)
  pdf/    föreläsningsanteckningar, problem sets, lösningar
misc/     småtester
```

## Submodul

MATH 4423 använder kursens repo som submodul. Efter en ny klon:

```
git submodule update --init
```
