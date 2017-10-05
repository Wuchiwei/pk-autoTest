# -*- coding: utf-8 -*-
"""
Simple iOS tests, showing accessing elements and getting/setting text from them.
"""
import unittest
import os
import sys
sys.path.append("../../import")
import setup
import element
from random import randint
from appium import webdriver
from time import sleep

class SimpleIOSTests(unittest.TestCase):

    def setUp(self):
        # set up appium
        setup.load_for2(self)
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
