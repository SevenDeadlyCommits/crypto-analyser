from dataclasses import dataclass

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
