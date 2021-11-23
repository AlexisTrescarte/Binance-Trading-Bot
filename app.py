from flask import Flask, render_template, jsonify, request
from binance.client import Client
from binance.enums import *
import config
from datetime import datetime, timedelta

client = Client(config.API_KEY, config.SECRET_KEY)
cmd = 'python ./Python/bot.py'

app = Flask(__name__)

@app.route("/")
def index():
    # Get client account
    account = client.get_account()
    # Get blanace for all crypto
    balances = account['balances']
    user_balances = []
    for balance in balances:
        if(float(balance['free'])>0):
            user_balances.append(balance)

    # Get all the symbols
    exchange_infos = client.get_exchange_info()
    symbols = exchange_infos['symbols']

    return render_template('index.html', user_balances=user_balances, symbols=symbols)

@app.route('/bot')
def bot():
    return render_template('bot.html')


@app.route('/settings')
def settings():
    return 'settings'

@app.route('/pass_val',methods=['POST'])
def pass_val():
    candelstick = request.get_json()
    print(candelstick)
    return jsonify({'reply':'success'})

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