import talib, numpy

SIGNAL_PERIOD=9
FAST_PERIOD=12
SLOW_PERIOD=26
MACD_PERIOD=34

class MACD_Algo:
    def __init__(self):
        self.closes_data_list = []
        self.macd_list = []
        self.in_position = False

    def update(self, new_close_data):
        self.closes_data_list.append(float(new_close_data))

        print(self.closes_data_list)

        if(len(self.closes_data_list) > MACD_PERIOD):
            self.process_macd()

    def process_macd(self):
        self.closes_data_array = numpy.array(self.closes_data_list)
        macd, macdsignal, macdhist = talib.MACD(self.closes_data_array, fastperiod=FAST_PERIOD, slowperiod=SLOW_PERIOD, signalperiod=SIGNAL_PERIOD)
        self.macd_list = [macd, macdsignal]

        if(macd[-1]-macdsignal[-1]>0 and macd[-2]-macdsignal[-2]<0 and self.in_position):
            self.sell()

        if(macd[-1]-macdsignal[-1]<0 and macd[-2]-macdsignal[-2]>0 and not self.in_position):
            self.buy()

        
    def get_macd_list(self):
        return self.macd_list

    def get_last_macd(self):
        return self.macd_list[-1]

    def buy(self):
        self.in_position = True
        print("It's time to buy")

    def sell(self):
        self.in_position = False
        print("It's time to sell")