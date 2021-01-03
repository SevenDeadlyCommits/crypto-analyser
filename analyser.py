import argparse
import datetime

import coin_data
import simple_result_data
import processor
import data_importer
import constants
import plot_options
import plotter

def process_args():
    parser = argparse.ArgumentParser(description='Analyse historic crytpo data')
    parser.add_argument('-c', '--coins', nargs='+', type=str, choices=constants.COIN_SELECTION,
                        help='The cryptocurrency to analyse')

    parser.add_argument('-p', '--plot-type', type=str, choices=plot_options.valid_modes.keys(),
                        help='The plot type requested')
    parser.add_argument('-s', '--show', required=False, action='store_true',
                        help='Whether to show the plot once created ')
    parser.add_argument('-n', '--no-save', required=False, action='store_true',
                        help='Whether to save the plot to disk as a png')

    parser.add_argument('-i', '--info-type', required=False, type=str, choices=constants.INFO_TYPES,
                        help='The type of information to get out of the analyser')

    # date range
    parser.add_argument('-f', '--date-from', type=lambda s: datetime.datetime.strptime(s, '%Y-%m-%d'))
    parser.add_argument('-t', '--date-to', type=lambda s: datetime.datetime.strptime(s, '%Y-%m-%d'))

    return parser.parse_args()

def run():
    args = process_args()

    importer = data_importer.DataImporter()
    data_processor = processor.Processor()

    data_frames = []
    for coin in args.coins:
        data_frames.append(importer.get_data(coin))

    if args.info_type:
        results = data_processor.process_simple(data_frames)
        for i in range(0, len(args.coins)):
            print(args.coins[i], 'Info:\n' + str(results[i]))

    if args.plot_type:
        options = plot_options.PlotOptions(args.coins, args.plot_type, args.show, (args.no_save == False), args.date_from, args.date_to)
        plot = plotter.Plotter(data_frames, options)
        plot.plot_results()

def main():
    run()
    
if __name__ == "__main__":
    main()
