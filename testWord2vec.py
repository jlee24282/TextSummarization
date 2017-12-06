# import modules & set up logging
# import modules & set up logging
import gensim, logging
import reader

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
# modeldir = 'models/newsarticle_300_50'
# model = gensim.models.Word2Vec.load(modeldir)
# print (model.wv['Wednesday'] + model.wv['today'])/2
#
#
#


#
import gensim, logging
import reader

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
training_data = []
for i in range(600):
    training_data.append(reader.csvReader('data/news_summary.csv').getData()[i]["text_wordsL"])
sentences = training_data
print len(sentences), sentences
# train word2vec on the two sentences
model = gensim.models.Word2Vec(sentences, min_count=5, size=50)

modeldir = 'models/newsarticle_600_50'
model.save(modeldir)
# new_model = gensim.models.Word2Vec.load(modeldir)
#
# print new_model.wv['Wednesday']