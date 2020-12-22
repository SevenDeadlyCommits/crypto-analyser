from dataclasses import dataclass

@dataclass
class CoinData():
    timestamp: int
    date: str
    symbol: str
    val_open: float
    val_high: float
    val_low: float
    val_close: float
    vol_coin: float
    vol_usd: float 
