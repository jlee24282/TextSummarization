import json
import gensim, logging
from sklearn.cluster import KMeans
import numpy as np
from scipy.cluster.vq import kmeans, vq
from sklearn.metrics import pairwise_distances_argmin_min
from reader import csvReader
import pandas as pd

"""
Data is from https://www.kaggle.com/sunnysai12345/news-summary/data
Kondalarao Vonteru
"""

class sentence2vec(object):
    """
    Returning value in dictionary format
    """
    def __init__(self, data, model, stopwords, vecsize):
        self.data = data
        self.model = model
        self.stopwords = stopwords
        self.vecsize = vecsize

    def convert(self):
        data = self.data

        for i in range(len(data)):
            data[i]['sentences_score'] = []
            for k in range(len(data[i])):
                sentence = str(data[i]['text_sentencesL'][0]).split(' ')
                sentenceScore = 0
                wordTotal = 0
                for word in sentence:
                    try:
                        if word not in self.stopwords:
                            score = model.wv[word]
                            wordTotal += 1
                            sentenceScore += score
                    except:
                        pass
                # print sentenceScore
                try:
                    sentenceScore = sentenceScore / wordTotal
                except:
                    sentenceScore = [0] * int(self.vecsize)
                data[i]['sentences_score'].append(sentenceScore)

        return self.data



if __name__ == '__main__':
    print ''

    fileDir = "data/news_summary.csv"
    data = csvReader(fileDir).getData()
    stopwords = csvReader(fileDir).getStopwords()

    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    modeldir = 'models/newsarticle600_100'
    model = gensim.models.Word2Vec.load(modeldir)
    data[0]['text_wordsL'][0]
    print (model.wv[data[0]['text_wordsL'][0]] + model.wv[data[0]['text_wordsL'][0]]) / 2

    print data[0]['text_wordsL'][0]
    data = data[0:100]
    for i in range(len(data)):
        data[i]['sentences_score'] = []
        for sentence in data[i]['text_sentencesL']:
            sentenceScore = 0
            wordTotal = 0
            for word in sentence:
                try:
                    if word not in stopwords:
                        score = model.wv[word]
                        wordTotal += 1
                        sentenceScore += score
                except:
                    pass
            # print sentenceScore
            try:
                sentenceScore = sentenceScore / wordTotal
            except:
                sentenceScore = [0]*100
            data[i]['sentences_score'].append(sentenceScore)

    for i in range(len(data)):
        X = np.array(data[i]['sentences_score'])
        kmeans = KMeans(n_clusters=5, random_state=0).fit(X)
        closest, _ = pairwise_distances_argmin_min(kmeans.cluster_centers_, X)
        print closest

        print len(data[i]['sentences_score']), len(data[i]['text_sentencesL'])
        result = ''
        for k in closest:
            s = str(data[i]['text_sentencesL'][k])
            print s
            if len(s) > 0:
                s = s.strip()
                s = s.capitalize()
                result = result + s
                result = result + '. '
        print result
        data[i]['result'] = result
        del data[i]['sentences_score']

    pd.DataFrame(data).to_csv('data/output/output.csv', index=False)
