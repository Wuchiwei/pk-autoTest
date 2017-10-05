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
        sleep(2)

    def test_cleanall_follow(self):
        self.info_button = self.driver.find_element_by_xpath('//XCUIElementTypeOther[1]/XCUIElementTypeTabBar[1]/XCUIElementTypeButton[4]')
        self.info_button.click()
        sleep(1)
        self.my_follow = self.driver.find_element_by_accessibility_id('我的追蹤')
        self.my_follow.click()
        sleep(1)

        while True:
                try:
                    self.has_follow = self.driver.find_element_by_accessibility_id('已追蹤')
                except:
                    break
                self.has_follow = self.driver.find_element_by_accessibility_id('已追蹤')
                self.has_follow.click()
                sleep(1)
                self.clean_done = self.driver.find_element_by_xpath('//XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]')
                self.clean_done.click()
                sleep(1)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
