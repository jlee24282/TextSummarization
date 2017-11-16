# import modules & set up logging
# import modules & set up logging
import gensim, logging
import reader

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
training_data = []
for i in range(300):
    training_data.append(reader.csvReader('data/news_summary.csv').getData()[i]["text_words"])
sentences = training_data
print len(sentences), sentences
# train word2vec on the two sentences
model = gensim.models.Word2Vec(sentences, min_count=5, size=100)

modeldir = 'models/newsarticle_300_100'
model.save(modeldir)
new_model = gensim.models.Word2Vec.load(modeldir)

print model.wv['Wednesday']