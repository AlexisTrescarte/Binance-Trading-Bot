from Python.first_algo_RSI import RSI_Algo
from Python.second_algo_MACD import MACD_Algo
from Python.third_algo_EWO import EWO_Algo


class BotManager():
    def __init__(self):
        self.candelsticks = []
        self.algo_RSI = RSI_Algo()
        self.algo_MACD = MACD_Algo()
        self.algo_EWO = EWO_Algo()

    def update(self,new_candelstick):
        self.candelsticks.append(new_candelstick)
        self.algo_RSI.update(new_candelstick['c'])
        self.algo_MACD.update(new_candelstick['c'])
        self.algo_EWO.update(new_candelstick['c'])

