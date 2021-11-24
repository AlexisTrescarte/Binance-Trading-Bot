import backtrader as bt

class EWOStrategy(bt.Strategy):
    def __init__(self):
        self.ewo = bt.talib.SMA(self.data, timeperiod=5) - bt.talib.SMA(self.data, timeperiod=34)

    def next(self):
        if self.ewo > 0 and not self.position:
            self.buy(size=1)

        if self.ewo < 0 and self.position:
            self.close()



cerebro = bt.Cerebro()

data = bt.feeds.GenericCSVData(dataname='Backtests\Etherium_daily_2017_2021.csv', dtformat=2)

cerebro.adddata(data)
cerebro.addstrategy(EWOStrategy)
cerebro.run()

cerebro.plot()