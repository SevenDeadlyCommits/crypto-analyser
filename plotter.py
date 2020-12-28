from matplotlib import pyplot as plt

import processor
import plot_options

class Plotter:
    
    def __init__(self, data_frame, options):
        self.options = options
        self.data_frame = data_frame
        self.data_processor = processor.Processor()
        # map plotting functions
        self.plot_functions = {
            plot_options.valid_modes['highs']: self.__plot_highs__ 
        }

    def plot_results(self):
        if self.options.mode not in plot_options.valid_modes:
            print("Invalid plot mode, valid modes are:\n")
            print(plot_options.valid_modes.keys())
        else:
            self.plot_functions[self.options.mode]()

    def __handle_generic_options__(self):
        if self.options.save:
            plt.savefig('output/' + self.options.coin + 'USD_' + self.options.mode.upper() + '.png')
        if self.options.show:
            plt.show()

    def __plot_highs__(self):
        # get data for plot
        highs = self.data_processor.get_column(self.data_frame, 'High')
        # create plot
        plt.title(self.options.coin + ' Highs (all time)')
        plt.plot(highs, label='Highs')
        plt.ylabel('Value')
        plt.xlabel('Index')
        plt.legend()
        # handle generic options
        self.__handle_generic_options__()
        
