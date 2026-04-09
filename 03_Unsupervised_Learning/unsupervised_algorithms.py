# Unsupervised Learning Algorithms
# Used for unlabeled data to discover hidden patterns, groupings, and structures.

# 1. Imports
# Need sklearn.cluster for clustering algorithms, 
# sklearn.decomposition for PCA.

# 2. Clustering: Finding groups of similar instances.
#   a) K-Means (*)
#      Logic: Iteratively assigns points to K distinct clusters based on nearest mean.
#      Watch out for choosing 'K' correctly using the Elbow Method or Silhouette Score.
#      Implementation: from sklearn.cluster import KMeans

#   b) Hierarchical Clustering
#      Logic: Builds tree-like hierarchy of clusters (Dendrogram). 
#      Agglomerative (bottom-up) is the most common.
#      Implementation: from sklearn.cluster import AgglomerativeClustering, scipy cluster hierarchy for dendrograms.

# 3. Dimensionality Reduction: "Kya hai?"
#    Logic: Used to reduce the number of features/dimensions in a dataset 
#           while preserving as much information (variance) as possible.
#           Useful to visualize data and speed up model training.

#   a) Principal Component Analysis (PCA) (*)
#      Logic: Orthogonal transformation converting correlated variables to linearly uncorrelated ones (principal components).
#      Implementation: from sklearn.decomposition import PCA

# 4. Association Rule Learning: "upar upar se dekh le bas"
#    Logic: Used mainly in market basket analysis to track buying patterns.
#      Apriori Algorithm (finding frequent itemsets).
#      Eclat Algorithm (similar but uses depth-first search).
#      Implementation libraries: 'mlxtend' provides easy to use Apriori.

# Write actual implementations below:
