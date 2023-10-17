# %% 
from sklearn.decomposition import PCA
from read_data import read_dataset
from definitions import FRACTIES
import matplotlib.pyplot as plt

X, party_index = read_dataset()

# %% do PCA
pca = PCA(n_components=2)
pca.fit(X)
X_pca = pca.transform(X)
pca.explained_variance_ratio_

# %% plot
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)
ax.scatter(X_pca[:,0], X_pca[:,1])
parties = list(party_index.keys())
for txt in parties:
    ax.annotate(FRACTIES[txt]['Afkorting'], (X_pca[party_index[txt],0], X_pca[party_index[txt],1]), alpha=0.5)

# Move left y-axis and bottom x-axis to centre, passing through (0,0)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
# Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
# Show ticks in the left and lower axes only
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

print("dataset", X.shape)
plt.show()
# %%
