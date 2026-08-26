import os
import re
import csv
from bs4 import BeautifulSoup

VHODNA_MAPA = "cele_strani"
IZHODNI_CSV = "prenosniki.csv"

# funkcija, ki iz vsakega prenosnika naredi seznam slovarjev z lastnostmi le-tega
def obdelaj_datoteko(pot):
    with open(pot, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    izdelki = []

    for izdelek in soup.select(".products > .product-small"):

        naslov_tag = izdelek.select_one(".product-title a")
        cena_tag = izdelek.select_one(".price .amount")

        if not naslov_tag:
            continue

        naslov = naslov_tag.get_text(strip=True)
        url = naslov_tag.get("href")

        # ime naprave = vse pred velikostjo zaslona
        ime_match = re.search(r'^(.*?)\s+\d+[.,]?\d*\s*[″"]', naslov)
        ime = ime_match.group(1) if ime_match else naslov

        # procesor
        procesor_match = re.search(r'Intel\s+i7-[A-Za-z0-9]+', naslov)
        procesor = procesor_match.group(0) if procesor_match else "Intel Core i7"

        # RAM
        ram_match = re.search(r'(\d+)\s*GB RAM', naslov)
        ram = ram_match.group(1) + " GB" if ram_match else None

        # SSD
        ssd_match = re.search(r'(\d+)\s*(GB|TB)\s*SSD', naslov)
        ssd = (
            ssd_match.group(1) + " " + ssd_match.group(2)
            if ssd_match
            else None
        )

        # velikost zaslona
        zaslon_match = re.search(r'(\d+[.,]?\d*)\s*[″"]', naslov)
        zaslon = (
            zaslon_match.group(1).replace(",", ".") + '"'
            if zaslon_match
            else None
        )

        # grafična
        graficna_match = re.search(
            r'(RTX\s+[A-Za-z0-9]+|Quadro\s+[A-Za-z0-9]+)',
            naslov
        )
        graficna = graficna_match.group(1) if graficna_match else None

        # operacijski sistem
        os_match = re.search(r'Win\s+\d+\s*(?:Pro|Home)?', naslov)
        operacijski_sistem = os_match.group(0) if os_match else None

        # cena
        cena = cena_tag.get_text(" ", strip=True) if cena_tag else None

        izdelki.append({
            "ime": ime,
            "procesor": procesor,
            "ram": ram,
            "ssd": ssd,
            "zaslon": zaslon,
            "graficna": graficna,
            "operacijski_sistem": operacijski_sistem,
            "cena": cena,
            "url": url
        })

    return izdelki

# v vsaki html datoteki poklice funkcijo obdelaj_datoteko in jih zdruzi ter zapise v .csv datoteko
def main():

    vsi_izdelki = []

    for datoteka in os.listdir(VHODNA_MAPA):

        if not datoteka.endswith(".html"):
            continue

        pot = os.path.join(VHODNA_MAPA, datoteka)

        izdelki = obdelaj_datoteko(pot)
        vsi_izdelki.extend(izdelki)

        print(datoteka, "-", len(izdelki), "izdelkov")

    with open(IZHODNI_CSV, "w", encoding="utf-8", newline="") as f:

        stolpci = [
            "ime",
            "procesor",
            "ram",
            "ssd",
            "zaslon",
            "graficna",
            "operacijski_sistem",
            "cena",
            "url"
        ]

        writer = csv.DictWriter(f, fieldnames=stolpci)
        writer.writeheader()
        writer.writerows(vsi_izdelki)

    print("Skupaj:", len(vsi_izdelki))


if __name__ == "__main__":
    main()