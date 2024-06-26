
from bs4 import BeautifulSoup
import requests

resp = requests.get("https://www.tiobe.com/tiobe-index/")
contents = resp.text

bs = BeautifulSoup(contents, 'html.parser')

table = bs.find(id="top20")

rows = table.tbody.find_all("tr")

for row in rows[:10]:
    cols = row.find_all("td")
    print(f"{cols[4].text:20}    {cols[5].text:5}")



