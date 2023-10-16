# %%
import json
import os
import numpy as np

VOTE_TO_NUMERIC = {"Tegen" : -1, "Niet deelgenomen": 0, "Voor" : 1}

def read_dataset(fp="./data/"):

    # all motions
    moties = os.listdir(fp)
    with open(f"{fp}{moties[0]}", "r") as f:
        data = json.load(f)

    # all parties
    party_index = {party : i for i, party in enumerate(data['stemgedrag'].keys())}
    X =  np.zeros((len(data["stemgedrag"]), len(moties)))

    # load vectors for each 
    for i, motie in enumerate(moties):
        with open(f"./data/{motie}", "r") as f:
            data = json.load(f)
            for party, vote in data['stemgedrag'].items():
                X[party_index[party], i] = VOTE_TO_NUMERIC[vote]

    return X, party_index
