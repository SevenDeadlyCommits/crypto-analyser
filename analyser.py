from matplotlib import pyplot as plt
import argparse

import coin_data
import simple_result_data
import processor
import data_importer
import constants

def process_args():
    parser = argparse.ArgumentParser(description='Analyse historic crytpo data')
    parser.add_argument('coin', metavar='COIN', type=str, choices=constants.COIN_SELECTION,
                        help='The cryptocurrency to analyse')

    parser.add_argument('-t', '--type', type=str, choices=constants.PLOT_TYPES,
                        help='The plot type requested')
    parser.add_argument('-s', '--show', required=False, action='store_true',
                        help='Whether to show the plot once created ')
    parser.add_argument('-n', '--no-save', required=False, action='store_true',
                        help='Whether to save the plot to disk as a png')

    parser.add_argument('-i', '--info-type', required=False, type=str, choices=constants.INFO_TYPES,
                        help='The type of information to get out of the analyser')

    return parser.parse_args()

def run():
    args = process_args()

    importer = data_importer.DataImporter()
    data_frame = importer.get_data(args.coin)
    data_processor = processor.Processor()

    if args.type:
        lows = data_processor.get_column(data_frame, 'Low')
        highs = data_processor.get_column(data_frame, 'High')
        
        plt.title('Highs/Lows (all time)')
        plt.plot(highs, label='Highs')
        plt.plot(lows, label='Lows')
        plt.ylabel('Coin Value')
        plt.xlabel('Index')
        plt.legend()
        if args.no_save == False:
            plt.savefig('output/ETHUSD_HI_LO.png')
        if args.show:
            plt.show()

    if args.info_type:
        result = data_processor.process_simple(data_frame)
        print('Simple Results:\n' + str(result))

def main():
    run()
    
if __name__ == "__main__":
    main()
