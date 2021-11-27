import backtrader as bt
from backtrader.utils.py3 import values
import datetime
class WILLStrategy(bt.Strategy):
    def __init__(self):
        self.ema_20 = bt.talib.EMA(self.data, timeperiod=20)
        self.ema_50 = bt.talib.EMA(self.data, timeperiod=50)



    def next(self):
        if self.get_bearish_fractal() and self.ema_20[-2]-self.ema_50[-2]<0 and self.ema_20[-1]-self.ema_50[-1]>0 and not self.position:
            self.buy(size=1)

        if self.get_bullish_fractal() and self.position:
            self.close()

    def get_bearish_fractal(self):
        if self.data.high[-3] > self.data.high[-5] and self.data.high[-3] > self.data.high[-4] and self.data.high[-3] > self.data.high[-2] and self.data.high[-3] >self.data.high[-1]:
            return True
        else :
            return False

    def get_bullish_fractal(self):
        if self.data.low[-3] < self.data.low[-5] and self.data.low[-3] < self.data.low[-4] and self.data.low[-3] < self.data.low[-2] and self.data.low[-3] < self.data.low[-1]:
            return True
        else: 
            return False

cerebro = bt.Cerebro()

data = bt.feeds.GenericCSVData(dataname='Backtests\BTC_5minutes_october_december.csv', dtformat=2, close=4, high=2, low=3, timeframe=bt.TimeFrame.Minutes, compression=5 )
#  fromdate=datetime.datetime(2020, 1, 1), todate=datetime.datetime(2021, 11, 22)
cerebro.broker.setcash(100000.0)
cerebro.adddata(data)
cerebro.addstrategy(WILLStrategy)
cerebro.run()

cerebro.plot()