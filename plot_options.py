from dataclasses import dataclass
import datetime

valid_modes = {
    'highs':'highs', 
    'lows':'lows', 
    'hilo':'hilo'
    }


@dataclass
class PlotOptions():
    coins: list
    mode: str
    show: bool
    save: bool
    date_from: datetime
    date_to: datetime

