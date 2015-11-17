import unittest
from lib.pint_ext import PintExtUnitRegistry
from lib.chamber import PressureVessel
from . import PressureVesselTestCaseDataset

class TestPressureVesselCalcs(unittest.TestCase):
    test_case_dataset = PressureVesselTestCaseDataset()

    def test_step_size_validation(self):
        units = PintExtUnitRegistry()

        try:
            pv = PressureVessel(5.2399 * units.inch,
                                0.1 * units.inch,
                                4236.04 * units.psi,
                                0.001 * units.psi,
                                156e3 * units.psi,
                                1.5,
                                0)
            self.fail('Expected a ValueError to be thrown due to step size being 0')
        except ValueError:
            pass

        try:
            pv = PressureVessel(5.2399 * units.inch,
                                0.1 * units.inch,
                                4236.04 * units.psi,
                                0.001 * units.psi,
                                156e3 * units.psi,
                                1.5,
                                None)
            self.fail('Expected a ValueError to be thrown due to step size being None')
        except ValueError:
            pass

    def test_pv1(self):
        self._test_dataset_item(0)

    def test_pv2(self):
        self._test_dataset_item(1)

    def test_pv3(self):
        self._test_dataset_item(2)

    def test_pv4(self):
        self._test_dataset_item(3)

    def test_pv5(self):
        self._test_dataset_item(4)

    def test_pv6(self):
        self._test_dataset_item(5)

    def test_pv7(self):
        self._test_dataset_item(6)

    def test_pv8(self):
        self._test_dataset_item(7)

    def test_pv9(self):
        self._test_dataset_item(8)

    def _test_dataset_item(self, item_number):
        tc_data = self.test_case_dataset[item_number]
        self.assertAlmostEqual(tc_data.t_expected.magnitude, round(tc_data.t_calc.magnitude, 3), delta=0.001001)
