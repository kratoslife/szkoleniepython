import requests
url = 'https://api-v3.mojepanstwo.pl/dane/krs_podmioty.json'
params = {'conditions[q]':'Dragon Corporation Mateusz Pelczarski'}
r = requests.get(url, params=params)
print(r.url)
r.json()['Dataobject'][0]['data']['krs_podmioty.adres']