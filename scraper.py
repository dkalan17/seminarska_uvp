import bs4
import os
import requests

# povezava do spletne strani, brez stevilke strani (pagination), za uporabo v zanki
povezava_url = "https://refurb.si/kategorija-izdelka/laptops/page/2/?lang=en&processor=core-i7-en#038;processor=core-i7-en"
povezava_1_del = "https://refurb.si/kategorija-izdelka/laptops/page/"
povezava_2_del = "/?lang=en&processor=core-i7-en#038;processor=core-i7-en"

#nastavljen user agent, ker refurb pogosto blokira python-requests
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                   "AppleWebKit/537.36 (KHTML, like Gecko) "
                   "Chrome/124.0 Safari/537.36"
}

# s pomocjo zanke for shranimo vsako stran v svojo html datoteko. le-te shranimo v mapo cele_strani
#uporabimo try except in javimo če pri branju pride do napake
for i in range(1, 13):
    try:
        response = requests.get(povezava_1_del + str(i) + povezava_2_del, headers=headers,timeout=10)
        juha = bs4.BeautifulSoup(response.text, "html.parser")
        if not os.path.exists("cele_strani"):
            os.makedirs("cele_strani")
        with open("cele_strani/stran" + str(i) + ".html", "w", encoding="utf-8") as f: #html stran shranimo v mapo cele_strani
            f.write(str(juha))
    except Exception as e:
        print("Prislo je do napake pri branju strani " + str(i))
        continue