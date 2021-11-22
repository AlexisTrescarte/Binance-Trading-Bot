import talib, numpy

RSI_PERIOD = 14
RSI_OVERBOUGHT = 69
RSI_OVERSOLD = 29

class RSI_Algo:
    def __init__(self):
        self.closes_data_list = []
        self.rsi_list = []
        self.actual_rsi = None
        self.in_position = False

    def update(self, new_close_data):
        self.closes_data_list.append(new_close_data)

        if(len(self.closes_data_list) > 14):
            self.process_rsi()

    def process_rsi(self):
        self.closes_data_array = numpy.array(self.closes_data_list)
        rsi = talib.RSI(self.closes_data_array, RSI_PERIOD)
        print("rsi : {}".format(rsi))
        self.rsi_list.append(rsi)

        if(rsi > RSI_OVERBOUGHT and self.in_position):
            self.sell()

        if(rsi < RSI_OVERSOLD and not self.in_position):
            self.buy()
        
    def get_rsi_list(self):
        return self.rsi_list

    def get_last_rsi(self):
        return self.rsi_list[-1]

    def buy(self):
        self.in_position = True
        print("It's time to buy")

    def sell(self):
        self.in_position = False
        print("It's time to sell")