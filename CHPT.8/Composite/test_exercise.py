import unittest
from Composite.Exercise import SingleValue, ManyValues

class FirstTestSuite(unittest.TestCase):
    def test_creation(self):
        single_value = SingleValue(11)
        other_values = ManyValues()
        other_values.append(22)
        other_values.append(33)

        all_values = ManyValues()
        all_values.append(single_value)
        all_values.append(other_values)
        self.assertEqual(all_values.sum(), 66)
