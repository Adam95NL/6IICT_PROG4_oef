import requests , json

antwoord = requests.get("Thttps://api.covid19api.com/dayone/country/belgium/status/confirmed").text
andwoord_dict = json.loads(antwoord)
print(antwoord)