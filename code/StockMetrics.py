
import statistics as stats

from code.StockData import StockData


class StockMetrics(StockData):
    def __init__(self, path):
        # call the parent method's constructor
        super(StockMetrics, self).__init__(path)

        # now that we've ran self.load(), we can interact with "self.data" as a
        # list of lists
        self.load()

    def average01(self):
        
        
        averages = []
        for row in self.data:
            print("old row", row)
            new_row=[float(val) for val in row[1:] if val !="" and val !=" "]
            x=stats.mean(new_row)
            averages.append(round(x,3))
        return averages


    def median02(self):
        medians = []
        for row in self.data:
            new_row=[float(val) for val in row[1:] if val !="" and val !=" "]
            x=stats.median(new_row)
            medians.append(x)
        return medians

    def stddev03(self):
        stddev = []
        for row in self.data:
            new_row=[float(val) for val in row[1:] if val !="" and val !=" "]
            x=stats.stdev(new_row)
            stddev.append(round(x,3))
        return stddev
