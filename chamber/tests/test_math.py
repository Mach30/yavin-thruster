import unittest
from pint import UnitRegistry
from pressure_vessel_calcs import *


class TestPressureVesselCalcs(unittest.TestCase):
    def test_pv1(self):
        """
        The first test case of the pressure vessel calculations. Based on J. Simmons' dissertation.
        """
        # test 1: INCONEL 718, run 63

        units = UnitRegistry()

        fs = 1.5
        step_size = 0.001 * units.inch

        # The thickness that we expect
        t1 = 0.067 * units.inch

        pv1 = PressureVessel(5.2399 * units.inch,
                             0.1 * units.inch,
                             1333.29 * units.psi,
                             0.001 * units.psi,
                             156e3 * units.psi,
                             fs,
                             step_size)

        pv1.calculate_wall_thickness()

        self.assertAlmostEqual(t1.magnitude, round(pv1.t.magnitude, 3), delta=0.001001)

    def test_pv2(self):
        """
        The second test case of the pressure vessel calculations. Based on J. Simmons' dissertation.
        """
        # test 2: INCONEL 718, run 57

        units = UnitRegistry()

        fs = 1.5
        step_size = 0.001 * units.inch

        # The thickness that we expect
        t2 = 0.218 * units.inch

        pv2 = PressureVessel(5.2399 * units.inch,
                             0.1 * units.inch,
                             4236.04 * units.psi,
                             0.001 * units.psi,
                             156e3 * units.psi,
                             fs,
                             step_size)

        pv2.calculate_wall_thickness()

        self.assertAlmostEqual(t2.magnitude, round(pv2.t.magnitude, 3), delta=0.001001)

    def test_pv3(self):
        """
        The third test case of the pressure vessel calculations. Based on J. Simmons' dissertation.
        """
        # test 3: INCONEL 718, run 55

        units = UnitRegistry()

        fs = 1.5
        step_size = 0.001 * units.inch

        # The thickness that we expect
        t3 = 0.387*units.inch

        pv3 = PressureVessel(9.5433 * units.inch,
                             0.1 * units.inch,
                             4125.37 * units.psi,
                             0.001 * units.psi,
                             156e3 * units.psi,
                             fs,
                             step_size)

        pv3.calculate_wall_thickness()

        self.assertAlmostEqual(t3.magnitude, round(pv3.t.magnitude, 3), delta=0.001001)