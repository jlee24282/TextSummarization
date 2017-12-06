from reader import csvReader
from summarize import summary
import logging
import argparse
import reader
import gensim

def main():
    training = True
    fileDir = "data/news_summary.csv"
    creader = csvReader(fileDir)
    data = creader.getData()
    stopwords = creader.getStopwords()

    logging.basicConfig(format='%(asctime)s: %(message)s',
                        level=logging.DEBUG,
                        datefmt='%m/%d/%Y %I:%M:%S %p')
    # Parse input
    parser = argparse.ArgumentParser(description='TextSummarization: Summarizing News Article')

    parser.add_argument('mode', choices=['train', 'test'], help='Train or Test mode?')

    parser.add_argument('modelDir', help='model directory')

    args = parser.parse_args()

    if args.mode == 'test':
        summary(args.mode, data, stopwords, args.modelDir).run()

    elif args.mode == 'train':
        training_data = []
        for i in range(600):
            training_data.append(reader.csvReader('data/news_summary.csv').getData()[i]["text_wordsL"])
        sentences = training_data
        print len(sentences), sentences
        # train word2vec on the two sentences
        model = gensim.models.Word2Vec(sentences, min_count=5, size=50)

        modeldir = 'models/newsarticle_600_50'
        model.save(modeldir)

if __name__ == "__main__":
    main()