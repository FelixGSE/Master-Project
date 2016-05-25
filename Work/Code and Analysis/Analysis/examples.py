labels_true = [1,2,3,1]
labels_pred = [1,4,3,1]

classes, class_idx = np.unique(labels_true, return_inverse=True)
n_classes = classes.shape[0]
clusters, cluster_idx = np.unique(labels_pred, return_inverse=True)
n_clusters = clusters.shape[0]

contingency = coo_matrix((np.ones(class_idx.shape[0]),
    (class_idx, cluster_idx)),
    shape=(n_classes, n_clusters),
    dtype=np.int).toarray()

print labels_true
print labels_pred
print contingency