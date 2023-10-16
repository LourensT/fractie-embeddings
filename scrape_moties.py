# %%
import tkapi
from tkapi.stemming import Stemming
from tkapi.zaak import ZaakMotie

import json
import datetime
from pprint import pprint

from requests.exceptions import ConnectionError

# %%
def get_stemmingen_per_fractie(fractie, max_items = 100):
    fractie_id = fractie.id
    filter = Stemming.create_filter()
    filter.filter_fractie(fractie_id)
    filter.filter_moties()
    return api.get_stemmingen(filter=filter, max_items=max_items)

def get_decisions_per_fractie_from_besluit(besluit):
    response = {}
    response['resultaat'] = besluit.tekst
    response['onderwerp'] = besluit.agendapunt.onderwerp
    response['besluit_id'] = besluit.id
    response['datum'] = besluit.gewijzigd_op.strftime("%Y-%m-%d %H:%M:%S")
    
    stemgedrag = {}
    stemmingen = besluit.stemmingen
    for stemming in stemmingen:
        stemgedrag[stemming.fractie.naam] = stemming.soort

    response['stemgedrag'] = stemgedrag

    # pprint(response)
    return response

def save_res(res):
    subject = res['onderwerp']
    subject = subject.replace("/", "")
    subject = subject.replace("\\", "")
    if len(subject) > 200:
        subject = subject[:200]
    
    fp = f"{OUTPUT_FP}{res['datum'][:10]}_{subject}.json"

    with open(fp, "w") as f:
        json.dump(res, f)

def get_moties():
    filter = ZaakMotie.create_filter()
    filter.filter_soort('Motie')
    filter.filter_date_range(START, END)
    zaken = api.get_zaken(filter=filter, max_items=1000)

    print("Starting...")
    i = 0
    errors = 0
    for zaak in zaken: 
        besluiten = zaak.besluiten
        for besluit in besluiten:
            i+=1
            if i%25 == 0:
                print(f"Handled {i}")

            try:
                res = get_decisions_per_fractie_from_besluit(besluit)
                save_res(res)
            except ConnectionError:
                errors += 1
                print("Connection Error")
        
        if errors > 50:
            break
# %%
if __name__ == "__main__":
    api = tkapi.TKApi()
    OUTPUT_FP = "./data2/"
    START = datetime.datetime(2022, 2, 11)
    END = datetime.datetime(2022, 9, 21)

    get_moties()
