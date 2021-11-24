import talib, numpy

FAST_PERIOD=5
SLOW_PERIOD=34

class EWO_Algo:
    def __init__(self):
        self.closes_data_list = []
        self.ewo_list = []
        self.in_position = False

    def update(self, new_close_data):
        self.closes_data_list.append(float(new_close_data))
        print(len(self.closes_data_list))
        if(len(self.closes_data_list) > SLOW_PERIOD):
            self.process_ewo()

    def process_ewo(self):
        self.closes_data_array = numpy.array(self.closes_data_list)
        self.ewo_list = talib.SMA(self.closes_data_array, timeperiod=FAST_PERIOD) - talib.SMA(self.closes_data_array, timeperiod=SLOW_PERIOD)

        print("_________________________________________\n{}".format(self.ewo_list))
        if(self.ewo_list[-1]<0 and self.ewo_list[-2]>0 and self.in_position):
            self.sell()

        if(self.ewo_list[-1]>0 and self.ewo_list[-2]<0 and not self.in_position):
            self.buy()

        
    def get_awo_list(self):
        return self.ewo_list

    def get_last_awo(self):
        return self.ewo_list[-1]

    def buy(self):
        self.in_position = True
        print("It's time to buy")

    def sell(self):
        self.in_position = False
        print("It's time to sell")