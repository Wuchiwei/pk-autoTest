# -*- coding: utf-8 -*-
"""
Simple iOS tests, showing accessing elements and getting/setting text from them.
"""
import unittest
import os
import sys
sys.path.append("../../../../../import")
import setup
import element
from random import randint
from appium import webdriver
from time import sleep
class SimpleIOSTests(unittest.TestCase):

    def setUp(self):
        # set up appium
        setup.load_for5(self)
        setup.ck_login_ordinary(self)
        
    def test_popular_gift_diamond_enough(self):  #送禮時，正確扣除鑽石數量

        self.driver.tap([(160, 280)])
        sleep(1)
        self.gift_butten = self.driver.find_element_by_accessibility_id('icon gift')
        self.gift_butten.click()
        sleep(1)
        self.diamond_value = self.driver.find_element_by_xpath('//XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[2]')
        self.diamond1 = int(  self.diamond_value.get_attribute('value').replace(',','')   )   - 200
        self.applause_gift_butten = self.driver.find_element_by_accessibility_id('Bear')
        self.applause_gift_butten.click()
        self.gift_butten.click()
        sleep(1)
        self.diamond2 = int(  self.diamond_value.get_attribute('value').replace(',','') )
        self.assertEqual(self.diamond1, self.diamond2)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
