import pandas as pd

"""
Data is from https://www.kaggle.com/sunnysai12345/news-summary/data
Kondalarao Vonteru
"""

class csvReader(object):
    """
    Returning value in dictionary format
    """
    def __init__(datadir):
        data = {"topic": [],
                "summarized": [],
                "text": [],
                "date": [],
                "author": []}
        csvData             = pd.read_csv(datadir)
        data["summarized"]  = csvData["summarized"]
        data["text"]        = csvData["text"]
        data["topic"]       = csvData["headlines"]
        data["date"]        = csvData["date"]
        data["author"]      = csvData["author"]

    def getData(self):
        return self.data

