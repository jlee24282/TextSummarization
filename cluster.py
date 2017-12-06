
from sklearn.cluster import KMeans
import numpy as np
from sklearn.metrics import pairwise_distances_argmin_min

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

        for i in range(len(data)):
            X = np.array(data[i]['sentences_score'])
            kmeans = KMeans(n_clusters=5, random_state=0).fit(X)
            closest, _ = pairwise_distances_argmin_min(kmeans.cluster_centers_, X)
            print closest

            print len(data[i]['sentences_score']), len(data[i]['text_sentencesL'])
            for k in closest:
                print k
                print data[i]['text_sentencesL'][k]
        return self.data


if __name__ == '__main__':
    print ''