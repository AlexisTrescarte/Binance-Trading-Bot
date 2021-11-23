


from Python.first_algo_RSI import RSI_Algo


class BotManager():
    def __init__(self):
        self.candelsticks = []
        self.algo_RSI = RSI_Algo()

    def update(self,new_candelstick):
        self.candelsticks.append(new_candelstick)
        self.algo_RSI.update(new_candelstick['c'])


