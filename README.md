# Crypto RSI Heatmap Viewer for Binance Futures

Welcome to the Crypto RSI Heatmap Viewer, a Streamlit app for visualizing Relative Strength Index (RSI) data for coins on Binance Futures.

## How to Run the App

1. Create a virtual environment (optional):

    ```bash
    python -m venv env
    ```

    Activate the virtual environment:

    ```bash
    source env/bin/activate  # On Windows: .\env\Scripts\activate
    ```

2. Install requirements:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the app:

    ```bash
    streamlit run app.py
    ```

![RSI Heatmap](https://github.com/rishikesh2003/crypto-rsi-heatmap/assets/58881733/496515a9-bd1f-4683-9b6a-9d317e981019)

## Todo (Help Wanted)

1. **Dynamic Coin Fetching:**
    - Update `data.py` to dynamically fetch coin data from Binance.
  
2. **Enhance Scatter Chart:**
    - Add colors for oversold and overbought regions.
    - Split the chart into smaller ones based on RSI ranges (0-20, 20-40, 40-60, 60-80, 80-100).
    - Fix the issue of chart reload when switching timeframes.

## Contributions Welcome

Contributions and suggestions are welcome! If you have ideas for improvement or want to help with the todos, feel free to submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

🚀 Happy trading! 📈💹
