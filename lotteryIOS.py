import unittest
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class test(unittest.TestCase):
    reportDirectory = 'reports'
    reportFormat = 'xml'
    dc = {}
    testName = 'test'
    driver = None

    def setUp(self):
        self.dc['reportDirectory'] = self.reportDirectory
        self.dc['reportFormat'] = self.reportFormat
        self.dc['testName'] = self.testName
        self.dc['udid'] = '*******YOUR-IPHONE-UDID*******'
        self.dc['platformName'] = 'ios'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.dc)

    def testtest(self):
        self.driver.swipe(1012, 2053, 350, 2053, 265)
        self.driver.find_element_by_xpath("xpath=//*[@text='YOUR APP NAME']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='LOGIN']").click()
        self.driver.find_element_by_xpath("xpath=//*[@placeholder='USER']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='i']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='a']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='n']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='more, numbers']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='0']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='0']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='2']").click()
        self.driver.find_element_by_xpath("xpath=//*[@placeholder='PWD']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='q']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='q']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='q']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='more, numbers']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='1']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='1']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='1']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='LOGIN' and @class='UIAButton']").click()
        self.driver.find_element_by_xpath(
            "xpath=((((//*[@text='YOUR APP NAME']/*[@class='UIAWindow'])[1]/*[@class='UIAView'])[2]/*[@class='UIAView'])[2]/*[@class='UIAButton'])[1]").click()

    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()
