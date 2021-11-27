from Python.first_algo_RSI import RSI_Algo
from Python.second_algo_MACD import MACD_Algo
from Python.third_algo_EWO import EWO_Algo


class BotManager():
    def __init__(self):
        self.candelsticks = []
        self.algo_RSI = RSI_Algo()
        self.algo_MACD = MACD_Algo()
        self.algo_EWO = EWO_Algo()
        self.in_position = [False, None]
        self.performance = 0
        self.profit = 0


    def update_with_history(self, history):
        turn = 0
        for candelstick in history:
            self.candelsticks.append(candelstick)
            RSI_want_to_buy, RSI_want_to_sell = self.algo_RSI.update(candelstick['close'])
            MACD_want_to_buy, MACD_want_to_sell = self.algo_MACD.update(candelstick['close'])
            EWO_want_to_buy, EWO_want_to_sell = self.algo_EWO.update(candelstick['close'])

            if (RSI_want_to_buy or MACD_want_to_buy or EWO_want_to_buy) and not self.in_position[0] and turn>100:
                self.launch_jugment_aggregation_buy(RSI_want_to_buy, MACD_want_to_buy )

            if (RSI_want_to_sell or MACD_want_to_sell or EWO_want_to_sell) and self.in_position[0] and turn>100:
                self.launch_jugment_aggregation_sell(RSI_want_to_sell, MACD_want_to_sell)
            turn+=1

    def update(self,new_candelstick):
        self.candelsticks.append(new_candelstick)
        RSI_want_to_buy, RSI_want_to_sell = self.algo_RSI.update(new_candelstick['c'])
        MACD_want_to_buy, MACD_want_to_sell = self.algo_MACD.update(new_candelstick['c'])
        EWO_want_to_buy, EWO_want_to_sell = self.algo_EWO.update(new_candelstick['c'])

        if (RSI_want_to_buy or MACD_want_to_buy or EWO_want_to_buy) and not self.in_position[0]:
            self.launch_jugment_aggregation_buy()

        if (RSI_want_to_sell or MACD_want_to_sell or EWO_want_to_sell) and self.in_position[0]:
            self.launch_jugment_aggregation_sell()

    

    def launch_jugment_aggregation_buy(self, RSI_want_to_buy, MACD_want_to_buy):

        # Est-tu performant ?
        rsi_performance = self.algo_RSI.get_performance()
        macd_performance = self.algo_MACD.get_performance()
        ewo_performance = self.algo_EWO.get_performance()

        if RSI_want_to_buy:
            # Pense-tu que le prix va monter ?
            rsi_increase_rate = 1
            macd_increase_rate = self.algo_MACD.get_increase_rate()
            ewo_increase_rate = self.algo_EWO.get_increase_rate()

            # Veux-tu acheter ? 
            score = rsi_performance*rsi_increase_rate+macd_performance*macd_increase_rate+ewo_performance*ewo_increase_rate
            if score > 100:
                print("____________ACHAT____________")
                print("Achat à {}".format(self.candelsticks[-1]['close']))
                print("Performances | {} %| {} %| {} %".format(rsi_performance, macd_performance, ewo_performance))
                print("Score : {}".format(score))
                self.in_position=[True, float(self.candelsticks[-1]['close'])]
                print("_____________________________")

        elif MACD_want_to_buy:
            # Pense-tu que le prix va monter ?
            rsi_increase_rate = self.algo_RSI.get_increase_rate()
            macd_increase_rate = 1
            ewo_increase_rate = self.algo_EWO.get_increase_rate()

            # Veux-tu acheter ? 
            score = rsi_performance*rsi_increase_rate+macd_performance*macd_increase_rate+ewo_performance*ewo_increase_rate
            if score > 100:
                print("____________ACHAT____________")
                print("Achat à {}".format(self.candelsticks[-1]['close']))
                print("Performances | {} %| {} %| {} %".format(rsi_performance, macd_performance, ewo_performance))
                print("Score : {}".format(score))
                self.in_position=[True, float(self.candelsticks[-1]['close'])]
                print("_____________________________")


        else:
            # Pense-tu que le prix va monter ?
            rsi_increase_rate = self.algo_RSI.get_increase_rate()
            macd_increase_rate = self.algo_MACD.get_increase_rate()
            ewo_increase_rate = 1

            # Veux-tu acheter ? 
            score = rsi_performance*rsi_increase_rate+macd_performance*macd_increase_rate+ewo_performance*ewo_increase_rate
            if score > 100:
                print("____________ACHAT____________")
                print("Achat à {}".format(self.candelsticks[-1]['close']))
                print("Performances | {} %| {} %| {} %".format(rsi_performance, macd_performance, ewo_performance))
                print("Score : {}".format(score))
                self.in_position=[True, float(self.candelsticks[-1]['close'])]
                print("_____________________________")
        

    def launch_jugment_aggregation_sell(self, RSI_want_to_sell, MACD_want_to_sell):
        # Est-tu performant ?
        rsi_performance = self.algo_RSI.get_performance()
        macd_performance = self.algo_MACD.get_performance()
        ewo_performance = self.algo_EWO.get_performance()

        if RSI_want_to_sell:
            # Pense-tu que le prix va monter ?
            rsi_increase_rate = 1
            macd_increase_rate = self.algo_MACD.get_decrease_rate()
            ewo_increase_rate = self.algo_EWO.get_decrease_rate()

            # Veux-tu acheter ? 
            score = rsi_performance*rsi_increase_rate+macd_performance*macd_increase_rate+ewo_performance*ewo_increase_rate
            if score > 100:
                print("____________VENTE________________________________________{}_________________".format(self.profit))
                print("Vente à {}".format(self.candelsticks[-1]['close']))
                print("Performances | {} %| {} %| {} %".format(rsi_performance, macd_performance, ewo_performance))
                print("Score : {}".format(score))
                profit = float(self.candelsticks[-1]['close']) - self.in_position[1]
                print("Profit : {}".format(profit))
                self.in_position=[False, None]
                self.profit+=profit
                print("____________________________________________________________________________")

        elif MACD_want_to_sell:
            # Pense-tu que le prix va monter ?
            rsi_increase_rate = self.algo_RSI.get_decrease_rate()
            macd_increase_rate = 1
            ewo_increase_rate = self.algo_EWO.get_decrease_rate()

            # Veux-tu acheter ? 
            score = rsi_performance*rsi_increase_rate+macd_performance*macd_increase_rate+ewo_performance*ewo_increase_rate
            if score > 100:
                print("____________VENTE________________________________________{}_________________".format(self.profit))
                print("Vente à {}".format(self.candelsticks[-1]['close']))
                print("Performances | {} %| {} %| {} %".format(rsi_performance, macd_performance, ewo_performance))
                print("Score : {}".format(score))
                profit = float(self.candelsticks[-1]['close']) - self.in_position[1]
                print("Profit : {}".format(profit))
                self.in_position=[False, None]
                self.profit+=profit
                print("____________________________________________________________________________")

        else:
            # Pense-tu que le prix va monter ?
            rsi_increase_rate = self.algo_RSI.get_decrease_rate()
            macd_increase_rate = self.algo_MACD.get_decrease_rate()
            ewo_increase_rate = 1

            # Veux-tu acheter ? 
            score = rsi_performance*rsi_increase_rate+macd_performance*macd_increase_rate+ewo_performance*ewo_increase_rate
            if score > 100:
                print("____________VENTE________________________________________{}_________________".format(self.profit))
                print("Vente à {}".format(self.candelsticks[-1]['close']))
                print("Performances | {} %| {} %| {} %".format(rsi_performance, macd_performance, ewo_performance))
                print("Score : {}".format(score))
                profit = float(self.candelsticks[-1]['close']) - self.in_position[1]
                print("Profit : {}".format(profit))
                self.in_position=[False, None]
                self.profit+=profit
                print("____________________________________________________________________________")