from matplotlib import pyplot as plt
import os

import processor
import plot_options

class Plotter:
    
    def __init__(self, data_frames, options):
        self.options = options
        self.data_frames = data_frames
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
            if os.path.exists('output') == False:
                os.mkdir('output')
            plt.savefig('output/' + self.options.coins + 'USD_' + self.options.mode.upper() + '.png')
        if self.options.show:
            plt.show()

    def __plot_highs__(self):
        # get data for plot
        highs = []
        for data_frame in self.data_frames:
            highs.append(self.data_processor.get_column(data_frame, 'High'))
        # create plot
        plt.title('Highs (all time)')
        for i in range(0,len(self.options.coins)):
            plt.plot(highs[i], label=self.options.coins[i])
        plt.ylabel('USD')
        plt.xlabel('Index')
        plt.legend()
        # handle generic options
        self.__handle_generic_options__()
        

