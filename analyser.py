from matplotlib import pyplot as plt
import argparse

import coin_data
import simple_result_data
import processor
import data_importer

running = True

def process_args():
    parser = argparse.ArgumentParser(description='Analyse historic crytpo data')
    parser.add_argument('coin', metavar='-c', type=str,
                        help='The cryptocurrency to analyse')

    return parser.parse_args()

def run():
    args = process_args()

    importer = data_importer.DataImporter()
    data_frame = importer.get_data(args.coin)
    data_processor = processor.Processor()
    result = data_processor.process_simple(data_frame)

    print('Simple Results:\n' + str(result))

def main():
    run()
    
    # lows = data_processor.GetColumn(data_frame, 'Low')
    # highs = data_processor.GetColumn(data_frame, 'High')
    
    # plt.title('Highs/Lows (all time)')
    # plt.plot(highs, label='Highs')
    # plt.plot(lows, label='Lows')
    # plt.ylabel('Coin Value')
    # plt.xlabel('Index')
    # plt.legend()
    # plt.savefig('output/ETHUSD_HI_LO.png')
    # plt.show()

if __name__ == "__main__":
    main()
