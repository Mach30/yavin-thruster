import sys
import unittest

class TestHelloWorldChamber(unittest.TestCase):
    req_version = (2,7)
    cur_version = sys.version_info

    @unittest.skipIf(cur_version > req_version, "Requires Python <= 2.7.x")   

    def test_wall_thickness(self):
        import cadquery

        self.assertEqual(1, 1)
