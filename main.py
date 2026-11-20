import requests
import json
from src.filter import Filters
from src.db import Database
jobkind_requests = ["Fachinformatiker für Systemintegration", "Fachinformatiker Anwendungsentwicklung", "Fachinformatiker für Daten- und Prozessanalyse"]
headers = {"X-API-Key": "jobboerse-jobsuche"}
params = {"wo": "Bremen", "page": 1, "size": 150}
def poshla_dota(responsedata)-> list:
    data = []
    for stelle in responsedata["ergebnisliste"]:
        jobdata ={}
        jobdata["referenznummer"] = stelle["referenznummer"]
        jobdata["type"] = stelle["hauptberuf"]
        if stelle.get("eintrittszeitraum"):
            jobdata["date_begins"] = stelle["eintrittszeitraum"]["von"]
        else:
            jobdata["date_begins"] = None
        if stelle.get("stellenangebotsTitel"):
            jobdata["title"] = stelle["stellenangebotsTitel"]
        else:
            jobdata["title"] = None
        jobdata["company"] = stelle["firma"]
        if stelle["stellenlokationen"][0]["adresse"].get("plz"):
            jobdata["location"] = stelle["stellenlokationen"][0]["adresse"]["plz"]
        else:
            jobdata["location"] = None
        jobdata["date_posted"] = stelle["datumErsteVeroeffentlichung"]
        if stelle.get("externeURL"):
            jobdata["url"] = stelle["externeURL"]
        else:
            jobdata["url"] = None
        data.append(jobdata)

    return data

if __name__ == "__main__":
    db = Database()
    data = []
    for jobkind in jobkind_requests:
        params["was"] = jobkind
        response = requests.request('GET', 'https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v6/jobs', params=params,headers=headers)
        data.extend(poshla_dota(response.json()))
    data = Filters.filter_jobs(data)
    db.insert_job(data)