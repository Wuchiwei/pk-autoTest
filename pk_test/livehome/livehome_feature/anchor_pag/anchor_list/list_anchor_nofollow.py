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
sys.path.append("../function")
import function
from random import randint
from appium import webdriver
from time import sleep

class SimpleIOSTests(unittest.TestCase):

    def setUp(self):
        # set up appium
        setup.load_for5(self)
        setup.ck_login_ordinary(self)

    def test_list_nofollow_case4(self):  #粉絲數量變化
        self.driver.swipe(190,590,0,-400)
        self.driver.tap([(300, 570)])
        self.fans_value1 = self.driver.find_element_by_xpath('//XCUIElementTypeTable[1]/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[4]')
        sum = int(self.fans_value1.get_attribute('value')) - 1
        self.icon_follow = self.driver.find_element_by_accessibility_id('icon follow')
        self.icon_follow.click()
        self.icon_close = self.driver.find_element_by_accessibility_id('icon close')
        self.icon_close.click()
        self.driver.swipe(190,100,0,600)
        sleep(1)
        self.driver.swipe(190,590,0,-400)
        self.driver.tap([(300, 570)])
        self.fans_value2 = self.driver.find_element_by_xpath('//XCUIElementTypeTable[1]/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[4]')
        self.assertEqual(int(sum), int(self.fans_value2.get_attribute('value')))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
