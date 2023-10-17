# %%
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

from typing import List

from read_data import read_dataset
from definitions import FRACTIES


# Create KMeans object
def cluster(X, index, n, excluded_parties : List = [], weighted=True):
    assert len(X)==len(index)
    assert isinstance(excluded_parties, list)

    # weight by votes
    weights = np.ones(len(X))
    for party, i in index.items():
        if party in excluded_parties or FRACTIES[party]['Afkorting'] in excluded_parties:
            weights[i] = 0
        else:
            if weighted:
                weights[i] = FRACTIES[party]['Zetels']

    kmeans = KMeans(n_clusters=n, random_state=0)

    kmeans.fit(X, sample_weight=weights)

    # get strings of fusies
    fusies = ["" for i in range(n)]
    for party, i in index.items():
        if party in excluded_parties or FRACTIES[party]['Afkorting'] in excluded_parties:
            continue
        fusies[kmeans.labels_[i]] += FRACTIES[party]['Afkorting'] + ' '
    
    # for party in excluded_parties:
    #     if party in FRACTIES:
    #         fusies.append(FRACTIES[party]['Afkorting'])
    #     else:
    #         fusies.append(party)

    # copy X with no reference
    distance_from_cluster = sum([np.min(n) for n in kmeans.transform(X)])

    return fusies, distance_from_cluster

# %%
# Read data
X, y = read_dataset()
coalition = []
# exclude coalition (votes together often)
coalition += ['VVD', 'D66', 'CDA', 'CU']
# add parties that are not going for re-election
coalition += ['Den Haan', 'Ephraim', 'Gündoğan']
fusies, score = [], []
for i in range(5, 21-len(coalition)):
    f, s = cluster(X, y, i, excluded_parties=coalition)
    fusies.append(f)
    score.append(s)
# plot
plt.plot(range(5, 21-len(coalition)), score)
plt.ylabel('Afstand tot stemgedrag fusie (lager is beter)')
plt.xlabel('Hoeveelheid fracties na fusies')
plt.show()

# 1 fusie scenario
print(f"1-fusies scenario, {cluster(X, y, 13, excluded_parties=coalition)[0]}")
# 2 fusie scenario
print(f"2-fusies scenario, {cluster(X, y, 12, excluded_parties=coalition)[0]}")
# 3 fusie scenario
print(f"3-fusies scenario, {cluster(X, y, 11, excluded_parties=coalition)[0]}")
# 4 fusie scenario
print(f"4-fusies scenario, {cluster(X, y, 10, excluded_parties=coalition)[0]}")
# %%
