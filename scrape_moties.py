# %%
import tkapi
from tkapi.stemming import Stemming
import json

from pprint import pprint
import datetime


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
    response['datum'] = besluit.gewijzigd_op.strftime("%d-%m-%Y %H:%M:%S")
    
    stemgedrag = {}
    stemmingen = besluit.stemmingen
    for stemming in stemmingen:
        stemgedrag[stemming.fractie.naam] = stemming.soort

    response['stemgedrag'] = stemgedrag

    # pprint(response)
    return response

def dump_moties():
    # get any active fractie
    all_fracties = api.get_fracties(max_items=100)
    fracties_met_zetels = []
    for fractie in all_fracties:
        if not fractie.zetels_aantal is None and fractie.zetels_aantal  > 0:
            fracties_met_zetels.append(fractie)

    # select an active fractie, VVD is biggest and coalition, so most likely to have decisions
    for fractie in fracties_met_zetels:
        if fractie.naam == "Volkspartij voor Vrijheid en Democratie":
            vvd = fractie
            break

    print(f"using as index the party {vvd.naam}")

    # scrape backwards in time to get all decisions
    stemmingen = get_stemmingen_per_fractie(vvd, max_items = 10000)
    for stemming in stemmingen:
        besluit = stemming.besluit
        res = get_decisions_per_fractie_from_besluit(besluit)
        fp = f"./data/{res['datum']}_{res['onderwerp']}.json"
        with open(fp, "w") as f:
            json.dump(res, f)
    
if __name__ == "__main__":
    api = tkapi.TKApi()
    OUTPUT_FP = "./data/"
    dump_moties()
# %%
