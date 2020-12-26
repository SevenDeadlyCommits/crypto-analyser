import pandas
import requests
import os.path
from os import path

class DataImporter:
    url = 'https://www.cryptodatadownload.com/cdd/'
    file_prefix = 'Bittrex_'
    end = 'USD_1h.csv'

    def __init__(self):
        if path.exists('data') == False:
            os.mkdir('data')

    def import_data_frame_from_csv(self, path):
        return pandas.read_csv(path)

    def get_data(self, coin):
        filename = self.file_prefix + coin + self.end
        endpoint = self.url + filename
        data_file = requests.get(endpoint, 'data/' + filename, verify=False)
        open('data/' + filename, 'wb').write(data_file.content)

        with open('data/' + filename, 'r') as fin:
            data = fin.read().splitlines(True)
        with open('data/' + filename, 'w') as fout:
            fout.writelines(data[1:])
        
        return self.import_data_frame_from_csv('data/' + filename)
