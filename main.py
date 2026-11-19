import requests
import json
import src.db as db
jobkind_requests = ["Fachinformatiker für Systemintegration", "Fachinformatiker Anwendungsentwicklung", "Fachinformatiker für Daten- und Prozessanalyse"]
headers = {"X-API-Key": "jobboerse-jobsuche"}
params = {"wo": "Bremen", "page": 1, "size": 10}


response = requests.request('GET', 'https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v6/jobs', headers=headers, params=params)
data = []
for jobkind in jobkind_requests:
    params["was"] = jobkind
    response = requests.request('GET', 'https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v6/jobs', params=params,headers=headers)
    data.append({f"{jobkind}": response.json()})

# print(data[0]["Fachinformatiker für Systemintegration"]["ergebnisliste"][0]["externeURL"])
# with open('data.json', 'w') as f:
#     json.dump(data, f, indent=4)

def poshla_dota(data)-> dict:
    for stelle in data["ergebnisliste"]:
        jobdata ={}
        jobdata["referenznummer"] = stelle["referenznummer"]
        jobdata["type"] = stelle["hauptberuf"]
        jobdata["title"] = stelle["stellenangebotsTitel"]
        jobdata["company"] = stelle["firma"]
        if stelle["stellenlokationen"][0]["adresse"]["plz"]:
            jobdata["location"] = stelle["stellenlokationen"][0]["adresse"]["plz"]
        else:
            jobdata["location"] = None
        jobdata["date_posted"] = stelle["date_posted"]
        if stelle["externeURL"]:
            jobdata["url"] = stelle["externeURL"]
        else:
            jobdata["url"] = None


if __name__ == "__main__":
    db.Database()
    data = []
    for jobkind in jobkind_requests:
        params["was"] = jobkind
        response = requests.request('GET', 'https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v6/jobs', params=params,headers=headers)
        poshla_dota(response.json())