import requests
import json
jobkind_requests = ["Fachinformatiker für Systemintegration", "Fachinformatiker Anwendungsentwicklung", "Fachinformatiker für Daten- und Prozessanalyse"]
headers = {"X-API-Key": "jobboerse-jobsuche"}
params = {"wo": "Bremen", "page": 1, "size": 10}


response = requests.request('GET', 'https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v6/jobs', headers=headers, params=params)
data = []
for jobkind in jobkind_requests:
    params["was"] = jobkind
    response = requests.request('GET', 'https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v6/jobs', params=params,headers=headers)
    data.append({f"{jobkind}": response.json()})

with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)