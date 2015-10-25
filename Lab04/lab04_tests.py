import sys
import unittest
from analyzeActivity import *

class Lab04TestSuite(unittest.TestCase):

    def test_checkPythonVersion(self):

        currentVersion = sys.version_info

        self.assertGreaterEqual(currentVersion, (3, 4))

    def test_getUserPermissions(self):

        userMap = getUserPermissions()

        with self.subTest(key="bhall"):
            key = "bhall"
            expectedValue = {'Internal', 'Proceedings', 'Activity'}

            actualValue = userMap[key]
            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="hwilson"):
            key = "hwilson"
            expectedValue =  {'Journals', 'Reports', 'Magazines', 'Proceedings', 'Internal'}

            actualValue = userMap[key]
            self.assertEqual(expectedValue, actualValue)

    def test_getControllerPermissions(self):

        controllerMap = getControllerPermissions()

        with self.subTest(key="Wiki"):
            key = "Wiki"
            expectedValue = {'Bennett, Nancy', 'Carter, Sarah', 'Cook, Margaret', 'Gonzalez, Kimberly', 'Harris, Anne',
                             'Jackson, Doris', 'Kelly, Joyce', 'Miller, Aaron', 'Richardson, George',
                             'Rogers, Elizabeth', 'Sanchez, Deborah', 'Ward, Sandra', 'Watson, Martin'}

            actualValue = controllerMap[key]
            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Reports"):
            key = "Reports"
            expectedValue = {'Cook, Margaret', 'Harris, Anne', 'Kelly, Joyce', 'Miller, Aaron', 'Murphy, Donna',
                             'Phillips, Brenda', 'Richardson, George', 'Ward, Sandra', 'Wilson, Howard'}

            actualValue = controllerMap[key]
            self.assertEqual(expectedValue, actualValue)

    def test_getControllerActions(self):

        controllerMap = getControllerActions()

        with self.subTest(key="Journals"):
            key = "Journals"
            expectedValue = {'Page1', 'Page4', 'Page5', 'Page3', 'Page2'}
            actualValue = controllerMap[key]

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Proceedings"):
            key = "Proceedings"
            expectedValue =  {'Page4', 'Page1', 'Page5', 'Page3', 'Page2'}
            actualValue = controllerMap[key]

            self.assertEqual(expectedValue, actualValue)

    def test_parseLogFile(self):

        logEntries = parseLogFile()

        with self.subTest(line=3):
            expectedValue = 'bphillips', 'http://www.purdue.com/Forums/Page1', 'Forums', 'Page1', True
            actualValue = logEntries[3]
            self.assertEqual(expectedValue, actualValue)

        with self.subTest(line=195):
            expectedValue = 'mwatson', 'http://www.purdue.com/Wiki/Page2', 'Wiki', 'Page2', True
            actualValue = logEntries[195]
            self.assertEqual(expectedValue, actualValue)

    def test_grantAccess(self):

        with self.subTest(userID="mcook"):
            userID = "mcook"
            url = "http://www.purdue.com/Magazines/Page2"

            actualValue = canGrantAccess(userID, url)
            self.assertTrue(actualValue)

        with self.subTest(userID="kgonzalez"):
            userID = "kgonzalez"
            url = "http://www.purdue.com/Internal/Page3"

            actualValue = canGrantAccess(userID, url)
            self.assertFalse(actualValue)

        with self.subTest(userID="scooby"):
            userID = "scooby"
            url = "http://www.purdue.com/Videos/Page11"

            actualValue = canGrantAccess(userID, url)
            self.assertFalse(actualValue)

    def test_checkUserActivity(self):

        with self.subTest(userID="jevans"):
            expectedValue = [('http://www.purdue.com/Admin/Page3', True), ('http://www.purdue.com/Comments/Page2', False),
                             ('http://www.purdue.com/Forums/Page1', True), ('http://www.purdue.com/Forums/Page2', True),
                             ('http://www.purdue.com/Forums/Page3', True), ('http://www.purdue.com/Internal/Page2', True),
                             ('http://www.purdue.com/Magazines/Page2', False), ('http://www.purdue.com/Magazines/Page5', False),
                             ('http://www.purdue.com/Proceedings/Page2', True), ('http://www.purdue.com/Proceedings/Page4', True),
                             ('http://www.purdue.com/Reports/Page1', False), ('http://www.purdue.com/Reports/Page2', False),
                             ('http://www.purdue.com/Wiki/Page2', False), ('http://www.purdue.com/Wiki/Page3', False)]
            actualValue = checkUserActivity("jevans")
            actualValue.sort()

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(userID="sward"):
            expectedValue = [('http://www.purdue.com/Activity/Page4', False), ('http://www.purdue.com/Admin/Page5', True),
                             ('http://www.purdue.com/Forums/Page1', False), ('http://www.purdue.com/Forums/Page4', False),
                             ('http://www.purdue.com/Internal/Page2', False), ('http://www.purdue.com/Internal/Page4', False),
                             ('http://www.purdue.com/Journals/Page5', True), ('http://www.purdue.com/Reports/Page1', True)]
            actualValue = checkUserActivity("sward")
            actualValue.sort()

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(userID="Scooby"):
            expectedValue = []
            actualValue = checkUserActivity("scooby")

            self.assertEqual(expectedValue, actualValue)

    def test_getActivityByUser(self):

        activityMap = getActivityByUser()

        with self.subTest(key="Miller, Aaron"):
            key = "Miller, Aaron"
            expectedValue = (10, 3)
            actualValue = activityMap[key]

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Phillips, Brenda"):
            key = "Phillips, Brenda"
            expectedValue = (7, 4)
            actualValue = activityMap[key]

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="*"):
            expectedValue = sum([p + n for p, n in activityMap.values()])
            actualValue = 200

            self.assertEqual(expectedValue, actualValue)

    def test_getActivityByController(self):

        activityMap = getActivityByController()

        with self.subTest(key="Internal"):
            key = "Internal"
            expectedValue = (19, 7)
            actualValue = activityMap[key]

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Magazines"):
            key = "Magazines"
            expectedValue = (11, 6)
            actualValue = activityMap[key]

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="*"):
            expectedValue = sum([p + n for p, n in activityMap.values()])
            actualValue = 200

            self.assertEqual(expectedValue, actualValue)

if __name__ == '__main__' :
    unittest.main()
