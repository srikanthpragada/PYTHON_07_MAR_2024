import requests

user = input("Enter github username :")
resp = requests.get(f"https://api.github.com/users/{user}")
if resp.status_code == 404:   # Not Found
    print("Sorry! Could not get details of user")
    exit(1)


details = resp.json()  # Convert JSON to dict
print(f"Name       {details['name']}")
print(f"Company    {details['company']}")
print(f"Location   {details['location']}")
print(f"Repos      {details['public_repos']}")


