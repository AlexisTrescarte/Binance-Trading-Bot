import backtrader as bt


class RSIStrategy(bt.Strategy):
    def __init__(self):
        self.rsi = bt.talib.RSI(self.data, period=14)
        self.macdindicator = bt.talib.MACDFIX(self.data, signalperiod=9)
        self.ewo = bt.talib.SMA(self.data, timeperiod=5) - bt.talib.SMA(self.data, timeperiod=34)
        self.trigger_indicator = None

    def next(self):
         if self.rsi < 30 and self.macdindicator.macd > self.macdindicator.macdsignal and not self.position:
             self.trigger_indicator="MACD"
             self.buy(price=self.broker.getcash())
   
         if self.rsi <30 and self.ewo > 0:
             self.trigger_indicator="EWO"
             self.buy(size=1/7)

         if self.rsi > 70 and self.macdindicator.macd < self.macdindicator.macdsignal and self.position and self.trigger_indicator=="MACD":
             self.close()

         if self.rsi > 70 and self.ewo < 0 and self.position and self.trigger_indicator=="EWO":
             self.close()


cerebro = bt.Cerebro()

data = bt.feeds.GenericCSVData(dataname='Backtests\BTC_hour_2021.csv', dtformat=2, timeframe=bt.TimeFrame.Minutes, compression=60)
# 
cerebro.broker.setcash(100000.0)
cerebro.adddata(data)
cerebro.addstrategy(RSIStrategy)
cerebro.run()

cerebro.plot()