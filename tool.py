import requests
user = input("GitHub username daal: ")
r = requests.get(f"https://api.github.com/users/{user}")
if r.status_code == 200:
    data = r.json()
    print(f"Naam: {data['name']}")
    print(f"Followers: {data['followers']}")
    print(f"Repos: {data['public_repos']}")
else:
    print("User nahi mila!")
