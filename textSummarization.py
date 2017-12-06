from reader import csvReader
from summarize import summary
import logging
import argparse

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

    summary(args.mode, data, stopwords, args.modelDir).run()

if __name__ == "__main__":
    main()