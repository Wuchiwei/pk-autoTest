# -*- coding: utf-8 -*-
"""
Simple iOS tests, showing accessing elements and getting/setting text from them.
"""
import unittest
import os
from random import randint
from appium import webdriver
from time import sleep

class SimpleIOSTests(unittest.TestCase):

    def setUp(self):
        # set up appium
        app = os.path.abspath('../../app/PKLive-InHouse.app')
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': app,
                'platformName': 'iOS',
                'platformVersion': '10.3',
                'deviceName': 'iPhone 6',
            })
        try:
            Confirm_butten = self.driver.find_element_by_accessibility_id('Confirm')
            Confirm_butten.click()
            massage_allow = self.driver.find_element_by_xpath('//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[6]/XCUIElementTypeOther[2]/XCUIElementTypeAlert[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]')
            massage_allow.click()
            sleep(1)
        except:
            pass
        sleep(1)

        try:
            self.info_butten = self.driver.find_element_by_xpath('//XCUIElementTypeOther[1]/XCUIElementTypeTabBar[1]/XCUIElementTypeButton[4]')
            self.info_butten.click()
            sleep(2)
            self.sign_out_butten = self.driver.find_element_by_accessibility_id('登出')
            self.sign_out_butten.click()
            sleep(2)
        except:
            pass

    def test_sign_out(self):
        self.icon_phone_butten = self.driver.find_element_by_accessibility_id('icon phone')
        self.assertEqual('icon phone', self.icon_phone_butten.get_attribute('name'))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
