import websocket, json
import config
import first_algo_RSI as algo_RSI


SOCKET = "wss://stream.binance.com:9443/ws/{}@kline_1m".format(config.SYMBOL)

closes = []
algo_RSI = algo_RSI.RSI_Algo()

def on_open(ws):
    print("open")

def on_close(ws):
    print("close")

def on_message(ws, message):
    global closes
    json_message = json.loads(message)
    
    candle = json_message['k']
    is_candle_closed = candle['x']
    close = float(candle['c'])
    
    if is_candle_closed:
        print("candle closed at {}".format(close))
        closes.append(close)
        algo_RSI.update(close)

    
ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
ws.run_forever()