import subprocess
import sys

subprocess.run(
    [sys.executable, "scraper.py"],
    check=True
)

subprocess.run(
    [sys.executable, "urejanje.py"],
    check=True
)

print("scraping in obdelava podatkov sta koncana")