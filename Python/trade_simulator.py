import pickle


class User:
    # initial_balance | account initial balance ($)
    # actual_balance | account actual balance ($)
    # trading_history | [list of Trade object] Historic of trades
    # trading_in_progress | [list of Trade object] All not ended trades
    def __init__(self):    
        self.initial_balance=10000
        self.actual_balance=10000
        self.trading_history=[]
        self.trading_in_progress=[]

    def write_save(self):
        with open('data/trade_simulator', 'wb') as saving_file:
            pickle.dump(self, saving_file, pickle.HIGHEST_PROTOCOL)

    def read_save(self):
        with open('data/trade_simulator', 'rb') as saving_file:
            saves = pickle.load(saving_file)
            self.initial_balance=saves.initial_balance
            self.actual_balance=saves.actual_balance
            self.trading_history=saves.trading_history
            self.trading_in_progress=saves.trading_in_progress

    def create_trade(self, date, symbol, amount, purchasing_price,  in_progress=True, selling_price=None):
        new_trade_id = len(self.trading_history)+len(self.trading_in_progress)+1
        new_trade = Trade(new_trade_id, date, symbol, amount, purchasing_price,  in_progress, selling_price)
        
        if(in_progress):
            self.trading_in_progress.append(new_trade)
        else:
            self.trading_history.append(new_trade)

        self.actual_balance-=(new_trade.purchasing_price*new_trade.amount)
        self.write_save()

    def close_trade(self, trade_id, selling_price):
        for trade in self.trading_in_progress:
            if(trade.id == trade_id):
                self.trading_in_progress.remove(trade)
                trade.selling_price = selling_price
                trade.in_progress = False
                self.trading_history.append(trade)
                self.actual_balance+=(trade.selling_price-trade.purchasing_price)*trade.amount


        self.write_save()

class Trade:
    # id | trade id
    # date | trade positionning date
    # symbol | crypto symbol (ex:BTCUSD)
    # amount | Position amount (ex: 0.003 [crypto_amount])
    # purchasing_price | Position initial price
    # selling_price | Position final price ( null if not ended )
    # in_progress | Ended or not (True if ended, false otherwise)
    def __init__(self, id, date, symbol, amount, purchasing_price, selling_price, in_progress):
        self.id = id
        self.date=date
        self.symbol=symbol
        self.amount=amount
        self.purchasing_price=purchasing_price
        self.selling_price=selling_price
        self.in_progress=in_progress

    def to_string(self):
        return str(self.id)+" | "+ self.date+" | "+self.symbol+" | "+str(self.purchasing_price)+" | "

user = User()
#user.read_save()
