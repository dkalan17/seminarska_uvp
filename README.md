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

## Pogon kode
1. Kloniranje repozitorija
- Odpri command prompt/terminal.
- S cd funkcijo navigiraj v mapo kamor želiš shraniti projekt.
- Poženi ukaz "git clone https://github.com/dkalan17/seminarska_uvp.git".

2. Namestitev virtualnega okolja (virtual enviroment)
- V VS Code-u odpri terminal v mapi s projektom.
- Ustvari virtualno okolje na Windows z ukazom "python -m venv venv" ali na Mac/Linux z "python3 -m venv venv"
- Aktiviraj virtualno okolje na Windows z ukazom "venv\Scripts\activate" ali na Mac/Linux z "source venv/bin/activate" (ko je aktivno, bo v terminalu vidno (venv) na začetku vrstice)

3. Namestitev knjižnic
+ Potrebne knjižnice namestite z ukazom: "pip install pandas matplotlib beautifulsoup4 requests jupyter numpy".

4. Zagon programa
+ Poženite datoteko main.py

## Težave, ki sem jih imel
+ Podatki niso bili standardizirani, na primer nekje ni bil podan ssd ali pa grafična kartica, zato je bilo težko izluščiti prave dele html kode.

## Zaključek
+ Z izdelavo tega projekta sem se naučil veliko novih stvari o anilizi podatkov in "web scrapanju". Znanje, ki sem ga pridobil se mi zdi koristno in ga bom še uporabil.
