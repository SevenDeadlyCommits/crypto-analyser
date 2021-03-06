import pandas
import requests
import os.path
import time
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

    def file_out_of_date(self, filename):
        if os.path.isfile(filename):
            # valid for 24 hrs
            valid_time = time.time() - 86400
            valid = (os.path.getmtime(filename) <= valid_time)
            if valid:
                valid = (os.path.getctime(filename) <= valid_time)
            return valid
        return True

    def get_data(self, coin):
        filename = self.file_prefix + coin + self.end
        filename_with_path = 'data/' + filename

        if self.file_out_of_date(filename_with_path):
            print('Data out of date, requesting new dataset\n')
            endpoint = self.url + filename
            data_file = requests.get(endpoint, filename_with_path, verify=False)

            # now process file to remove comment
            open('data/' + filename, 'wb').write(data_file.content)

            with open(filename_with_path, 'r') as fin:
                data = fin.read().splitlines(True)
            with open(filename_with_path, 'w') as fout:
                # replace spaces to allow easy filtering as pandas does not 
                # support filtering with column names containing spaces
                data[1] = data[1].replace(' ', '_')
                fout.writelines(data[1:])

        return self.import_data_frame_from_csv(filename_with_path)
