from reader import csvReader
import summarize
import logging
import argparse

def main():
    training = True
    fileDir = "data/news_summary.csv"
    data = csvReader.getData(fileDir)


    logging.basicConfig(format='%(asctime)s: %(message)s',
                        level=logging.DEBUG,
                        datefmt='%m/%d/%Y %I:%M:%S %p')
    # Parse input
    parser = argparse.ArgumentParser(
        description='TextSummarization: temporal information extraction')
    parser.add_argument('mode', choices=['train', 'test'],
                        help='Train or Test mode?')
    parser.add_argument('input_folder', help='Input data folder path')
    parser.add_argument('model',
                        help='Name of the model to use (case sensitive)')
    parser.add_argument('modeCorenlp', choices=['m', 'c'],
                        help='corenlp only or mantime?')
    parser.add_argument('-v', '--version', help='show the version and exit',
                        action='store_true')
    parser.add_argument('-ppp', '--post_processing_pipeline',
                        action='store_true',
                        help='it uses the post processing pipeline.')



    result = summarize(data, training)

if __name__ == "__main__":
    main()