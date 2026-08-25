# Seminarska naloga - analiza podatkov

Za seminarsko nalogo sem se odločil analizirati podatke o prenosnikih na strani refurb.si. Za to temo sem se odlocil, ker sem zainteresiran v to marketinško nišo in me zanima nova tehnologija.

## Struktura projekta
- main.py: datoteka, ki najprej pozene scraper potem pa ostale procese
- scraper.py: datoteka, prenese html strani in jih da v mapo cele_strani
- cele_strani: mapa, ki vsebuje vse html strani, prenešene s pogonom scraperja
- urejanje.py: datoteka, ki z uporabo knjiznice BeautifulSoup uredi podatke in jih shrani v csv tabelo (prenosniki.csv)
- prenosniki.csv: tabela v kateri so podatki o razlicnih prenosnikih
- analiza_prenosnikov.ipynb: jupyter zvezek kjer so podatki analizirani in predstavljeni na razlicne nacine
- README.md: opis projekta in delovanja