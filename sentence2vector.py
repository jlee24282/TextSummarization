import pandas as pd

"""
Data is from https://www.kaggle.com/sunnysai12345/news-summary/data
Kondalarao Vonteru
"""

class sentence2vec(object):
    """
    Returning value in dictionary format
    """
    def __init__(self, data, model):
        self.data = data
        self.model = model

    def convert(self):
        return self.data


if __name__ == '__main__':
    print ''