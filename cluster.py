from sklearn.cluster import KMeans
from scipy.cluster.vq import kmeans, vq

"""
Data is from https://www.kaggle.com/sunnysai12345/news-summary/data
Kondalarao Vonteru
"""

class clustering(object):
    """
    Returning value in dictionary format
    """
    def __init__(self, data):
        self.data = data

    def getresult(self, data):
        self.data = data

        # kmeans = KMeans(n_clusters=2)

        codebook, _ = kmeans(y, 3)
        cluster_indices, _ = vq(y, codebook)

        return self.data


if __name__ == '__main__':
    print ''