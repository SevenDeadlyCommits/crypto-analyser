import pandas

import coin_data
import simple_result_data
import constants

class Processor:
    
    def process_simple(self, data_frame):
        min_frame = data_frame.iloc[data_frame['Low'].idxmin()]
        max_frame = data_frame.iloc[data_frame['High'].idxmax()]
        return simple_result_data.SimpleResult(min_frame['Low'], min_frame['Date'], max_frame['Low'], max_frame['Date'])

    def get_column(self, data_frame, column):
        return data_frame[column].tolist()
