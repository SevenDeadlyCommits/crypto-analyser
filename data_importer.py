import pandas

class DataImporter:

    @staticmethod
    def ImportToDataFrameFromCSV(path):
        return pandas.read_csv(path)
