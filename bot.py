import websocket, json

SOCKET = "wss://stream.binance.com:9443/ws/btcusdt@kline_1m"
closes = []


def on_open(ws):
    print("open")

def on_close(ws):
    print("close")

def on_message(ws, message):
    global closes
    json_message = json.loads(message)
    
    candle = json_message['k']
    is_candle_closed = candle['x']
    close = candle['c']

    if is_candle_closed:
        closes.append(close)
        print("candle closed at {}".format(close))
        

ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
ws.run_forever()