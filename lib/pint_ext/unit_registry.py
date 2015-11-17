from lib.util import Singleton

from pint import UnitRegistry

class PintExtUnitRegistry(Singleton, UnitRegistry):
    pass
