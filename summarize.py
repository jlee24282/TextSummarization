import word2vec
import gensim
import reader
from sentence2vector import sentence2vec
from cluster import clustering

class summary(object):
    """
    Returning value in dictionary format
    """
    def __init__(self, mode, data, modelDir):
        self.mode = mode
        self.modelDir = modelDir
        self.data = data
        self.model = None

    def run(self, vectoerLength):

        if self.mode == 'test':
            # test
            modeldir = 'models/newsarticle_300_' + vectoerLength
            self.model = gensim.models.Word2Vec.load(modeldir)
            sentencesVec = sentence2vec(self.data, self.model)
            clusteringSentences = clustering(self.data)

            result = sentencesVec.convert()
            result = clusteringSentences.getresult(result)
            return result

        else:
            # train
            sentences = [['first', 'this is testing sentence'], ['second', 'is this training sentence']]
            model = gensim.models.Word2Vec(sentences, size=100, window=5, min_count=5, workers=4)

            return ''

if __name__ == '__main__':
    data = reader.csvReader('data/news_summary.csv').getData()
    result = summary('test', data[301:302], 'models/newsarticle_300_').run('50')
