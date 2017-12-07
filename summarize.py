import gensim
import reader
from sentence2vector import sentence2vec
from cluster import clustering
import pandas as pd

class summary(object):
    """
    Returning value in dictionary format
    """
    def __init__(self, mode, article,stopwords, modelDir, docsize):
        self.mode = mode
        self.modelDir = modelDir
        self.stopwords = stopwords
        self.model = None
        self.docsize = docsize
        self.data = article[-int(docsize):]
        self.vecSize = modelDir.split('_')[1]

    def run(self):

        if self.mode == 'test':
            '''
            test
            '''
            modeldir = self.modelDir
            self.model = gensim.models.Word2Vec.load(modeldir)

            #initialize classes
            sentencesVec = sentence2vec(self.data, self.model, self.stopwords, self.vecSize)
            clusteringSentences = clustering(self.data)

            #run process
            data = sentencesVec.convert()
            result = clusteringSentences.getresult(data)

            pd.DataFrame(result).to_csv('data/output/output.csv', index=False)
            return result

        else:
            # train
            sentences = [['first', 'this is testing sentence'], ['second', 'is this training sentence']]
            model = gensim.models.Word2Vec(sentences, size=100, window=5, min_count=5, workers=4)

            return ''

if __name__ == '__main__':
    data = reader.csvReader('data/news_summary.csv').getData()
    result = summary('test', data[301:302], 'models/newsarticle_300_').run('50')
