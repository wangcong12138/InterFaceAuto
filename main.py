import unittest
from testcase.test_ddt import test_material
from BeautifulReport import BeautifulReport


def allTest():
    testsuit = unittest.TestSuite()
    testloader = unittest.TestLoader()
    alltestcase = testloader.discover(start_dir="testcase")
    testsuit.addTest(alltestcase)
    return alltestcase


def smokeTest():
    testSuit = unittest.TestSuite()
    testLoader = unittest.TestLoader()
    allDdtTestcase = testLoader.loadTestsFromTestCase(test_material)
    testSuit.addTest(allDdtTestcase)
    return testSuit


if __name__ == '__main__':
    runner = BeautifulReport(allTest())
    runner.report(description="微信公众平台接口测试", report_dir="reports")




