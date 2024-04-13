import requests

resp = requests.get("https://restcountries.com/v3.1/all")
countries = resp.json()

sorted_countries = sorted(countries, key=lambda c: c['population'], reverse=True)
for c in sorted_countries[:10]:
    print(f"{c['name']['common']:50}   {c['population']:10}  {c['area']:10}" )
