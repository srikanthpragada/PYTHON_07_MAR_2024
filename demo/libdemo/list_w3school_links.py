import requests
from bs4 import BeautifulSoup

website = "https://www.w3schools.com"
resp = requests.get(website)
html_contents = resp.text

bs = BeautifulSoup(html_contents, 'html.parser')

links = set()
for a in bs.find_all("a"):
    if 'href' not in a.attrs:
        continue

    href = a['href']
    if href == '#':
        continue

    if not href.startswith("http"):
        if not href.startswith("/"):
            href = "/" + href

        href = website + href

    links.add(href)

for link in links:
    print(link)

print(f"Count = {len(links)}")
