from config.index import BINANCE_API_KEY
from config.index import BINANCE_SECRET_KEY
import ccxt


exchange = ccxt.binanceusdm(
    {
        "options": {
            "adjustForTimeDifference": True,
        },
        "apiKey": BINANCE_API_KEY,
        "secret": BINANCE_SECRET_KEY,
    }
)
