import backtrader as bt


class MACDStrategy(bt.Strategy):
    def __init__(self):
        self.macdindicator = bt.talib.MACDFIX(self.data, signalperiod=9)

    def next(self):
        if self.macdindicator.macd > self.macdindicator.macdsignal and not self.position:
            self.buy(size=1)

        if self.macdindicator.macdsignal > self.macdindicator.macd and self.position:
            self.close()










cerebro = bt.Cerebro()

data = bt.feeds.GenericCSVData(dataname='Backtests\Bitcoin_daily_2017_2021.csv', dtformat=2)

cerebro.adddata(data)
cerebro.addstrategy(MACDStrategy)
cerebro.run()

cerebro.plot()