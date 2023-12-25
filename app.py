import traceback
from datetime import datetime
import sys
import streamlit as st
import pandas as pd
from data import coin_list
from indicators.rsi import get_rsi
import matplotlib.pyplot as plt
from config.exchange import exchange
import random

st.snow()
sb = st.sidebar

sb.markdown("Timeframes")
page_names = ["1hour", "4hour", "1day"]
page = sb.radio("", page_names, index=0)
st.title(f"Crypto market RSI Scanner {page}")
c = st.empty()
while True:
    try:
        df = pd.DataFrame()
        ind = 0
        for coin in coin_list:
            print(
                f"Fetching new bars for {datetime.now().isoformat()} {coin['coin'].upper()}"
            )
            timeframe = ""
            if page == "1hour":
                timeframe = "1h"
            elif page == "4hour":
                timeframe = "4h"
            elif page == "1day":
                timeframe = "1d"
            bars1h = exchange.fetch_ohlcv(
                coin["coin"].upper() + "/USDT", timeframe=timeframe, limit=210
            )

            df1h = pd.DataFrame(
                bars1h,
                columns=["timestamp", "open", "high", "low", "close", "volume"],
            )
            df1h["timestamp"] = pd.to_datetime(df1h["timestamp"], unit="ms")
            rsi_arr = get_rsi(df1h["close"], 2)
            df = pd.concat(
                [
                    df,
                    pd.DataFrame(
                        [
                            {
                                "Index": ind,
                                "Coin": coin["coin"].upper(),
                                "RSI": random.randint(0, 100),
                            }
                        ]
                    ),
                ],
                ignore_index=True,
            )
            ind += 1

        fig, ax = plt.subplots(figsize=(20, 20))
        scatter = ax.scatter(df["Index"], df["RSI"])

        # Add labels to each point
        for i, txt in enumerate(df["Coin"]):
            ax.annotate(txt, (df["Index"][i], df["RSI"][i]), fontsize=18)

        # Customize plot
        ax.set_xlabel("Ranges")
        ax.set_ylabel("RSI")
        ax.set_title("RSI Values")

        # Display the plot using Streamlit
        c.pyplot(fig)

    except Exception as e:
        print(e)
        traceback.print_exc(file=sys.stdout)
