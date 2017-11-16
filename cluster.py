import pandas as pd

"""
Data is from https://www.kaggle.com/sunnysai12345/news-summary/data
Kondalarao Vonteru
"""

class clustering(object):
    """
    Returning value in dictionary format
    """
    def __init__(self, datadir):
        csvData   = pd.read_csv(datadir)
        self.data = []

        for row in csvData.iterrows():
            article = {
                "topic": row[1]["headlines"],
                "summarized": row[1]["text"],
                "text_sentences": str(row[1]["ctext"]).split("."),
                "text_words": str(row[1]["ctext"]).split(" "),
                "date": row[1]["date"],
                "author": row[1]["author"]}

            self.data.append(article)

    def getData(self):
        return self.data


if __name__ == '__main__':
    cr = csvReader('data/news_summary.csv')
    print cr.getData()[0]