import pandas
import requests

class DataImporter:
    url = 'https://www.cryptodatadownload.com/cdd/'
    file_prefix = 'Bittrex_'
    end = 'USD_1h.csv'

    def ImportToDataFrameFromCSV(self, path):
        return pandas.read_csv(path)

    def GetData(self, coin):
        filename = self.file_prefix + coin + self.end
        endpoint = self.url + filename
        data_file = requests.get(endpoint, 'data/' + filename, verify=False)
        open('data/' + filename, 'wb').write(data_file.content)
        
        with open('data/' + filename, 'r') as fin:
            data = fin.read().splitlines(True)
        with open('data/' + filename, 'w') as fout:
            fout.writelines(data[1:])
        
        return self.ImportToDataFrameFromCSV('data/' + filename)
