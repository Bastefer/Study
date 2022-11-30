from lr4 import Hospital
import unittest

class TestHospital(unittest.TestCase):
    def setUp(self):
        self.b = Hospital(8, 'Баярщинов Владислав')

        
    def testproverka(self):
        test_chamber = 'Лечющий врач Баярщинов Владислав лечит 30 болных'
        self.a = self.b.chamber()
        self.assertEqual(self.a, test_chamber)
        
if __name__ == '__main__':
    unittest.main()