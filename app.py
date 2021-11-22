from flask import Flask, render_template, jsonify
from binance.client import Client
from binance.enums import *
import config
from datetime import datetime, timedelta

client = Client(config.API_KEY, config.SECRET_KEY)

app = Flask(__name__)

@app.route("/")
def index():

    # Get client account
    account = client.get_account()
    # Get blanace for all crypto
    balances = account['balances']
    # Get all the symbols
    exchange_infos = client.get_exchange_info()
    symbols = exchange_infos['symbols']

    return render_template('index.html', user_balances=balances, symbols=symbols)

@app.route('/buy')
def buy():
    return 'buy'

@app.route('/sell')
def sell():
    return 'sell'

@app.route('/settings')
def settings():
    return 'settings'

@app.route('/history')
def history():

    now = datetime.now()
    first_date = now - timedelta(days = 30)
    candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_15MINUTE, first_date.strftime("%d %b, %Y"), now.strftime("%d %b, %Y"))
    
    processed_candlesticks = []
    for data in candlesticks:
        candlesticks = {
            "time": data[0]/1000 ,
            "open": data[1],
            "high": data[2],
            "low": data[3],
            "close": data[4],
        }
        processed_candlesticks.append(candlesticks)

    return jsonify(processed_candlesticks)


if __name__ == "__main__":
    app.run(debug=True)