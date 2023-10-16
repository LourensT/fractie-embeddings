# %% 
from sklearn.decomposition import PCA
from read_data import read_dataset

X, party_index = read_dataset()

# %% do PCA
pca = PCA(n_components=2)
pca.fit(X)
X_pca = pca.transform(X)

# %% plot
import matplotlib.pyplot as plt
plt.scatter(X_pca[:,0], X_pca[:,1])
parties = list(party_index.keys())
for i, txt in enumerate(parties):
    plt.annotate(txt, (X_pca[i,0], X_pca[i,1]))
plt.show()
# %%
party_index.keys()
# %%
