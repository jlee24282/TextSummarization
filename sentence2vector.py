import json
import gensim, logging

from reader import csvReader

"""
Data is from https://www.kaggle.com/sunnysai12345/news-summary/data
Kondalarao Vonteru
"""

class sentence2vec(object):
    """
    Returning value in dictionary format
    """
    def __init__(self, data, model, stopwords):
        self.data = data
        self.model = model
        self.stopwords = stopwords

    def convert(self):
        data = self.data
        data['text_words']

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
                    sentenceScore = [0] * 100
                data[i]['sentences_score'].append(sentenceScore)

        return self.data


if __name__ == '__main__':
    print ''

    fileDir = "data/news_summary.csv"
    data = csvReader(fileDir).getData()
    stopwords = csvReader(fileDir).getStopwords()

    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    modeldir = 'models/newsarticle_300_100_'
    model = gensim.models.Word2Vec.load(modeldir)
    data[0]['text_wordsL'][0]
    print (model.wv[data[0]['text_wordsL'][0]] + model.wv[data[0]['text_wordsL'][0]]) / 2

    print data[0]['text_wordsL'][0]
    for i in range(len(data)):
        data[i]['sentences_score'] = []
        for k in range(len(data[i])):
            sentence = str(data[i]['text_sentencesL'][0]).split(' ')
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

    print data[0]['sentences_score'][0]