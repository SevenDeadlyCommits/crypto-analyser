from matplotlib import pyplot as plt

import coin_data
import simple_result_data
import processor
import data_importer

def main():
    importer = data_importer.DataImporter()
    data_frame = importer.ImportToDataFrameFromCSV('data/Bittrex_ETHUSD_1h.csv')
    data_processor = processor.Processor()
    result = data_processor.ProcessSimple(data_frame)

    print('Simple Results:\n' + str(result))
    
    lows = data_processor.GetColumn(data_frame, 'Low')
    highs = data_processor.GetColumn(data_frame, 'High')
    
    plt.title('Highs/Lows (all time)')
    plt.plot(highs, label='Highs')
    plt.plot(lows, label='Lows')
    plt.ylabel('Coin Value')
    plt.xlabel('Index')
    plt.legend()
    plt.savefig('output/ETHUSD_HI_LO.png')
    plt.show()

if __name__ == "__main__":
    main()
