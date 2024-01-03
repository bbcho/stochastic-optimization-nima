from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    tradingview_widget = """
    <!-- TradingView Widget BEGIN -->
    <div class="tradingview-widget-container">
      <div id="tradingview_06b20"></div>
      <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
      <script type="text/javascript">
      new TradingView.widget(
      {
      "width": 980,
      "height": 610,
      "symbol": "NASDAQ:AAPL",
      "interval": "D",
      "timezone": "Etc/UTC",
      "theme": "light",
      "style": "1",
      "locale": "en",
      "toolbar_bg": "#f1f3f6",
      "enable_publishing": false,
      "allow_symbol_change": true,
      "container_id": "tradingview_06b20"
    }
      );
      </script>
    </div>
    <!-- TradingView Widget END -->
    """
    return render_template_string("""
    <html>
        <head>
            <title>TradingView Chart</title>
        </head>
        <body>
            {{ tradingview_widget | safe }}
        </body>
    </html>
    """, tradingview_widget=tradingview_widget)

if __name__ == '__main__':
    app.run(debug=True,port=6000)