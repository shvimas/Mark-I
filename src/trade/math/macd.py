import pandas as pd


def macd(prices: pd.DataFrame,
         long_per: int,
         short_per: int,
         **kwargs) -> pd.DataFrame:
    ema_short = prices.ewm(span=short_per, **kwargs).mean()
    ema_long = prices.ewm(span=long_per, **kwargs).mean()
    return ema_short - ema_long


def macd_signal(prices: pd.DataFrame,
                long_per: int,
                short_per: int,
                smooth_per: int,
                **kwargs) -> pd.DataFrame:
    return macd(prices=prices, long_per=long_per, short_per=short_per, **kwargs).ewm(span=smooth_per).mean()
