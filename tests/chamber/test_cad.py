import sys
import unittest
from pint import UnitRegistry
from lib.chamber import PressureVessel
from . import PressureVesselTestCaseDataset

class TestHelloWorldChamber(unittest.TestCase):
    """
    Handles running tests on the geometry of the 3D models that were created from our pre-defined dataset of
    sample dimensions.
    """

    # Allows us to skip this test if the version of Python isn't compatible
    reqd_version = (2, 100, 100)
    cur_version = sys.version_info
    version_msg = "Requires Python <= 2.7.x"

    def __init__(self, *args, **kwargs):
        super(TestHelloWorldChamber, self).__init__(*args, **kwargs)

        # Our datasets that drive the creation of the geometry
        self.test_case_dataset = PressureVesselTestCaseDataset()

    # We don't want to run this test case if it's run with Python 3
    @unittest.skipIf(cur_version > reqd_version, version_msg)
    def test_pv1(self):
        self._test_dataset_item(0)

    @unittest.skipIf(cur_version > reqd_version, version_msg)
    def test_pv2(self):
        self._test_dataset_item(1)

    @unittest.skipIf(cur_version > reqd_version, version_msg)
    def test_pv3(self):
        self._test_dataset_item(2)

    @unittest.skipIf(cur_version > reqd_version, version_msg)
    def test_pv4(self):
        self._test_dataset_item(3)

    @unittest.skipIf(cur_version > reqd_version, version_msg)
    def test_pv5(self):
        self._test_dataset_item(4)

    @unittest.skipIf(cur_version > reqd_version, version_msg)
    def test_pv6(self):
        self._test_dataset_item(5)

    @unittest.skipIf(cur_version > reqd_version, version_msg)
    def test_pv7(self):
        self._test_dataset_item(6)

    @unittest.skipIf(cur_version > reqd_version, version_msg)
    def test_pv8(self):
        self._test_dataset_item(7)

    @unittest.skipIf(cur_version > reqd_version, version_msg)
    def test_pv9(self):
        self._test_dataset_item(8)

    def _test_dataset_item(self, item_number):
        """
        Handles constructing and testing the geometry of the HelloWorldChamber based on test a selected test dataset.
        :param item_number: The index of the dataset to use
        :return: None
        """
        from lib.chamber.hello_world_chamber import HelloWorldChamber

        # We've compartmentalized our test case data so that it can be used to test both the math and the geometry
        tc_data = self.test_case_dataset[item_number]

        # TODO: Pull the pressure vessel calculation values out of the HelloWorldChamber
        # TODO: class and have the values passed in.
        # TODO: Instantiate the HelloWorldChamber instance with the current test case data

        # The solid that we need to test the dimensions of
        chamber = HelloWorldChamber().build(tc_data.ri, tc_data.t_guess, tc_data.p_c, tc_data.p_amb,
                                            tc_data.material_strength, tc_data.fs, tc_data.step_size)
       
        self.assertEqual(1, 1)
