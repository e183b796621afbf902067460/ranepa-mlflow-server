from typing import TypeVar
from trad3er.interfaces.trader.interface import iTrad3r


Trad3r = TypeVar('Trad3r', bound=iTrad3r)
