import talib, numpy

RSI_PERIOD = 14
RSI_OVERBOUGHT = 69
RSI_OVERSOLD = 29

class MACD_Algo:
    def __init__(self):
        self.in_position = False

    def update(self, new_close_data):
        self.closes_data_list.append(new_close_data)
        print(self.closes_data_list)
        if(len(self.closes_data_list) > 14):
            self.process_rsi()

    def process_macd(self):
        self.closes_data_array = numpy.array(self.closes_data_list)
        rsi = talib.RSI(self.closes_data_array, RSI_PERIOD)

        
    def get_macd_list(self):
        return "macd list"

    def get_last_macd(self):
        return "last macd"

    def buy(self):
        self.in_position = True
        print("It's time to buy")

    def sell(self):
        self.in_position = False
        print("It's time to sell")