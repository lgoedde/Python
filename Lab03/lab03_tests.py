import sys
import unittest
from myOperations import *

class Lab03TestSuite(unittest.TestCase):

    def test_checkPythonVersion(self):

        currentVersion = sys.version_info

        self.assertGreaterEqual(currentVersion, (3, 4))

    def test_checkTypes_normal(self):

        l = [3.14, -11.9, "Today", 121, "Tomorrow", 2.71]

        expectedValue = [1, 3, 2]
        actualValue = checkTypes(l)
        self.assertEqual(expectedValue, actualValue)

    def test_checkTypes_emptyInput(self):

        actualValue = checkTypes([])
        self.assertIsNone(actualValue)

    def test_checkTypes_wrongInput(self):

        actualValue = checkTypes("Hello")
        self.assertIsNone(actualValue)

    def test_normalizeVector_normal(self):

        l = [0, 1, 2, 3, 4, 10]

        expectedValue = [0.0, 0.05, 0.1, 0.15, 0.2, 0.5]
        actualValue = normalizeVector(l)
        self.assertEqual(expectedValue, actualValue)

    def test_normalizeVector_emptyInput(self):

        actualValue = normalizeVector([])
        self.assertIsNone(actualValue)

    def test_normalizeVector_wrongInput(self):

        actualValue = normalizeVector("Hello")
        self.assertIsNone(actualValue)

    def test_findMedian_normal(self):

        l = [6, 3.3, 13, 2, 9, 4]
        expectedValue = 5.0
        actualValue = findMedian(l)
        self.assertEqual(expectedValue, actualValue)

    def test_findMedian_emptyInput(self):

        actualValue = findMedian([])
        self.assertIsNone(actualValue)

    def test_findMedian_wrongInput(self):

        actualValue = findMedian([0, 0, 2, "Hello"])
        self.assertIsNone(actualValue)

    def test_rectifySignal_normal(self):

        l = [1.0, 0.81, 0.31, -0.31, -0.81, -1.0, -0.81, -0.31, 0.31, 0.81]
        expectedValue = [1.0, 0.81, 0.31, 0, 0, 0, 0, 0, 0.31, 0.81]
        actualValue = rectifySignal(l)
        self.assertEqual(expectedValue, actualValue)

    def test_rectifySignal_emptyInput(self):

        actualValue = rectifySignal([])
        self.assertIsNone(actualValue)

    def test_rectifySignal_wrongInput(self):

        actualValue = rectifySignal("Hello")
        self.assertIsNone(actualValue)

    def test_convertToBoolean_normal(self):

        l = 135
        expectedValue = [True, False, False, False, False, True, True, True]
        actualValue = convertToBoolean(l)
        self.assertEqual(expectedValue, actualValue)

    def test_convertToBoolean_wrongInput(self):

        actualValue = convertToBoolean(512)
        self.assertIsNone(actualValue)

    def test_convertToInteger_normal(self):

        l = [True, False, False, False, False, True, True, True]
        expectedValue = 135
        actualValue = convertToInteger(l)
        self.assertEqual(expectedValue, actualValue)

    def test_convertToInteger_wrongInput(self):

        actualValue = convertToInteger([True, 0, 1, False])
        self.assertIsNone(actualValue)

    def test_convertToInteger_emptyInput(self):

        actualValue = convertToInteger([])
        self.assertIsNone(actualValue)

    def test_switchNames_normal(self):

        l = ["Jackson, Michael M", "Trump, Donald", "Bush, George W"]
        expectedValue = ["Michael Jackson", "Donald Trump", "George Bush"]
        actualValue = switchNames(l)
        self.assertEqual(expectedValue, actualValue)

    def test_switchNames_wrongInput(self):

        actualValue = switchNames(124)
        self.assertIsNone(actualValue)

    def test_switchNames_emptyInput(self):

        actualValue = switchNames([])
        self.assertIsNone(actualValue)

    def test_getWeightAverage_normal(self):

        l = ["Michael Jackson: 195.5 lb", "Donald Trump: 211.7 lb",
            "George Bush: 207.3 lb", "Sherlock Holmes: 221.9 lb"]
        expectedValue = 209.1
        actualValue = getWeightAverage(l)
        self.assertEqual(expectedValue, actualValue)

    def test_getWeightAverage_wrongInput(self):

        actualValue = getWeightAverage(124)
        self.assertIsNone(actualValue)

    def test_getWeightAverage_emptyInput(self):

        actualValue = getWeightAverage([])
        self.assertIsNone(actualValue)

if __name__ == '__main__':
    unittest.main()
