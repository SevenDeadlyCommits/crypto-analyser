from matplotlib import pyplot as plt
import matplotlib.dates as mdates
import os
import datetime 

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
            coins_name = ''
            for coin in self.options.coins:
                coins_name += coin
            plt.savefig('output/' + coins_name + '_USD_' + self.options.mode.upper() + '.png')
        if self.options.show:
            plt.show()

    def __get_plot_date_range_str_(self):
        return self.options.date_from.strftime('%Y-%m-%d') + ' to ' + self.options.date_to.strftime('%Y-%m-%d')

    def __get_oldest_date__(self):
        oldest_date = None
        for data_frame in self.data_frames:
             oldest_date_str = data_frame.iloc[[-1]].Date.values[0]
             oldest_date_str = oldest_date_str.split()[0]
             current_oldest = datetime.datetime.strptime(oldest_date_str,'%Y-%m-%d')
             if oldest_date == None or current_oldest < oldest_date:
                 oldest_date = current_oldest
        return oldest_date
    
    def __get_newest_date__(self):
        newest_date = None
        for data_frame in self.data_frames:
             newest_date_str = data_frame.iloc[[0]].Date.values[0]
             newest_date_str = newest_date_str.split()[0]
             current_newest = datetime.datetime.strptime(newest_date_str,'%Y-%m-%d')
             if newest_date == None or current_newest < newest_date:
                 newest_date = current_newest
        return newest_date

    def _filter_by_dates(self):
        self.options.date_from = self.options.date_from if (self.options.date_from != None) else self.__get_oldest_date__()
        self.options.date_to = self.options.date_to if (self.options.date_to != None) else self.__get_newest_date__() 
        data_frames = []
        for data_frame in self.data_frames:
             data_frames.append(data_frame.query('Unix_Timestamp > ' + str(self.options.date_from.timestamp()) + 'and Unix_Timestamp < ' + str(self.options.date_to.timestamp())))
        return data_frames

    def __plot_highs__(self):
        # filter
        self.data_frames = self._filter_by_dates()
        # get data for plot
        highs = []
        date_strs = []
        for data_frame in self.data_frames:
            highs.append(self.data_processor.get_column(data_frame, 'High'))
            date_strs.append(self.data_processor.get_column(data_frame, 'Date'))
        dates_list = []
        for date_array in date_strs:
            dates = []
            for date in date_array:
                date_str = date.split()[0]
                dates.append(datetime.datetime.strptime(date_str,"%Y-%m-%d").date())
            dates_list.append(dates)
        # create plot
        plt.title('Highs ' + self.__get_plot_date_range_str_())
        for i in range(0,len(self.options.coins)):
            plt.plot(dates_list[i], highs[i], label=self.options.coins[i])
        ax = plt.gca()
        
        time_diff = self.options.date_to - self.options.date_from
        if time_diff.days >= 365:
            locator = mdates.YearLocator()
        elif time_diff.days >= 27:
            locator = mdates.MonthLocator()
        else:
            locator = mdates.DayLocator()
        ax.xaxis.set_major_locator(locator)
        fig = plt.gcf()
        fig.set_size_inches(16, 8)
        fig.autofmt_xdate()
        plt.ylabel('USD')
        plt.xlabel('Date')
        plt.legend()
        # handle generic options
        self.__handle_generic_options__()
        

