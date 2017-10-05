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

    def test_popular_gift_stroe_center(self):  #進入儲值程序

        self.driver.tap([(160, 280)])
        sleep(1)
        self.gift_butten = self.driver.find_element_by_accessibility_id('icon gift')
        self.gift_butten.click()
        sleep(1)
        self.stroe_butten = self.driver.find_element_by_accessibility_id('儲值')
        self.stroe_butten.click()
        self.stroe_title = self.driver.find_element_by_accessibility_id('儲值中心')



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
