from tests import test_cad, test_math
import unittest

suite = unittest.TestSuite()

suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_math.TestPressureVesselCalcs))
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_cad.TestHelloWorldChamber))

unittest.TextTestRunner().run(suite)