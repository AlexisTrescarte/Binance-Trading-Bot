var chart = LightweightCharts.createChart(document.getElementById("chart"), {
	width: screen.width-32,
  	height: screen.height/2,
	layout: {
		backgroundColor: '#000000',
		textColor: 'rgba(255, 255, 255, 0.9)',
	},
	grid: {
		vertLines: {
			color: 'rgba(197, 203, 206, 0.5)',
		},
		horzLines: {
			color: 'rgba(197, 203, 206, 0.5)',
		},
	},
	crosshair: {
		mode: LightweightCharts.CrosshairMode.Normal,
	},
	rightPriceScale: {
		borderColor: 'rgba(197, 203, 206, 0.8)',
	},
	timeScale: {
		borderColor: 'rgba(197, 203, 206, 0.8)',
	},
});

var candleSeries = chart.addCandlestickSeries({
  upColor: '#00ff00',
  downColor: '#ff0000',
  borderDownColor: 'rgba(255, 144, 0, 1)',
  borderUpColor: 'rgba(255, 144, 0, 1)',
  wickDownColor: 'rgba(255, 144, 0, 1)',
  wickUpColor: 'rgba(255, 144, 0, 1)',
});

fetch('http://127.0.0.1:5000//history')
	.then((r) => r.json())
	.then((response)=> {
		candleSeries.setData(response);
	})

var binanceSocket = new WebSocket("wss://stream.binance.com:9443/ws/btcusdt@kline_1d");
binanceSocket.onmessage = function (event) {
	var candlestick = (JSON.parse(event.data)).k;
	candleSeries.update({
		time: candlestick.t / 1000,
		open: candlestick.o,
		high: candlestick.h,
		low: candlestick.l,
		close: candlestick.c
	});

	if(candlestick.x){
		$.ajax(
				{
					type:'POST',
					contentType:'application/json',
					dataType:'json',
					url:'/pass_val',
					data: event.data,
					success:function (data) {
						var reply=data.reply;
						if (reply=="success")
						{
							return;
						}
						else
						{
						alert("some error ocured in session agent")
						}
		
				}
			}
		);
	}
	 
}