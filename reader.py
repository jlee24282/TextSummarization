import pandas as pd

"""
Data is from https://www.kaggle.com/sunnysai12345/news-summary/data
Kondalarao Vonteru
"""

class csvReader(object):
    """
    Returning value in dictionary format
    """
    def __init__(self, datadir):
        csvData             = pd.read_csv(datadir)
        self.stopwords      = open('data/stopwords.txt').readlines()
        self.data           = []

        for i in range(len(self.stopwords)):
            self.stopwords[i] = self.stopwords[i].replace('\n', '')

        for row in csvData.iterrows():
            article = {
                "topic": row[1]["headlines"],
                "summarized": row[1]["text"],
                "summarizedL": str(row[1]["text"]).lower(),
                "text_sentences": str(row[1]["ctext"]).split("."),
                "text_sentencesL": str(row[1]["ctext"]).lower().split("."),
                "text_words": str(row[1]["ctext"]).split(" "),
                "text_wordsL": str(row[1]["ctext"]).lower().split(" "),
                "date": row[1]["date"],
                "author": row[1]["author"]}

            self.data.append(article)

    def getData(self):
        return self.data

    def getStopwords(self):
        return self.stopwords


if __name__ == '__main__':
    cr = csvReader('data/news_summary.csv')
    print cr.getData()[0]