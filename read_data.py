# %%
import json
import os
import numpy as np

VOTE_TO_NUMERIC = {"Tegen" : -1, "Niet deelgenomen": 0, "Voor" : 1}

def read_dataset(fp="./data/"):

    # all motions
    moties = os.listdir(fp)
    with open(f"{fp}2023-09-26_Aangehouden motie ingediend bij het tweeminutendebat Vergunningverlening, toezicht en handhaving (VTH-stelsel).json", "r") as f:
        data = json.load(f)

    # all parties
    party_index = {party : i for i, party in enumerate(data['stemgedrag'].keys())}
    X =  np.zeros((len(data["stemgedrag"]), len(moties)))

    # load vectors for each 
    for i, motie in enumerate(moties):
        with open(f"./data/{motie}", "r") as f:
            data = json.load(f)
            if len(data['stemgedrag']) > 1:
                for party, vote in data['stemgedrag'].items():
                    X[party_index[party], i] = VOTE_TO_NUMERIC[vote]

    return X, party_index

# %%
