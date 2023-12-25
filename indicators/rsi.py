from pandas_ta.overlap import ema
from pandas_ta.momentum import rsi


def get_rsi(close, precision):
    rsi_val = rsi(close, 14)
    rsi_28 = rsi(rsi_val, 28)
    rsi_42 = rsi(rsi_val, 42)
    rsi_50 = rsi(close, 50)
    rsi_100 = rsi(rsi_val, 100)
    rsi_200 = rsi(close, 200)
    rsi_ma14 = ema(rsi_val, 14)

    if len(close) > 200:
        rsi_final_val = round(float(rsi_val[len(rsi_val) - 1]), precision)
        rsi_bef_val = round(float(rsi_val[len(rsi_val) - 2]), precision)

        rsi_28_final = round(float(rsi_28[len(rsi_28) - 1]), precision)
        rsi_28_bef_final = round(float(rsi_28[len(rsi_28) - 2]), precision)

        rsi_42_final = round(float(rsi_42[len(rsi_42) - 1]), precision)
        rsi_42_bef_final = round(float(rsi_42[len(rsi_42) - 2]), precision)

        rsi_100_final = round(float(rsi_100[len(rsi_100) - 1]), precision)
        rsi_100_bef_final = round(float(rsi_100[len(rsi_100) - 2]), precision)

        rsi_50_final = round(float(rsi_50[len(rsi_50) - 1]), precision)
        rsi_50_bef_final = round(float(rsi_50[len(rsi_50) - 2]), precision)

        rsi_200_final = round(float(rsi_200[len(rsi_200) - 1]), precision)
        rsi_200_bef_final = round(float(rsi_200[len(rsi_200) - 2]), precision)

        rsi_ma_14_final = round(float(rsi_ma14[len(rsi_ma14) - 1]), precision)
        rsi_ma_14_bef_final = round(float(rsi_ma14[len(rsi_ma14) - 2]), precision)
    else:
        rsi_final_val = 0
        rsi_bef_val = 0

        rsi_28_final = 0
        rsi_28_bef_final = 0

        rsi_42_final = 0
        rsi_42_bef_final = 0

        rsi_100_final = 0
        rsi_100_bef_final = 0

        rsi_50_final = 0
        rsi_50_bef_final = 0

        rsi_200_final = 0
        rsi_200_bef_final = 0

        rsi_ma_14_final = 0
        rsi_ma_14_bef_final = 0
    return [
        rsi_final_val,  # 0
        rsi_bef_val,  # 1
        rsi_28_final,  # 2
        rsi_28_bef_final,  # 3
        rsi_42_final,  # 4
        rsi_42_bef_final,  # 5
        rsi_50_final,  # 6
        rsi_50_bef_final,  # 7
        rsi_100_final,  # 8
        rsi_100_bef_final,  # 9
        rsi_200_final,  # 10
        rsi_200_bef_final,  # 11
        rsi_ma_14_final,  # 12
        rsi_ma_14_bef_final,  # 13
    ]
