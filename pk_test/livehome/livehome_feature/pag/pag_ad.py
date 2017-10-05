# -*- coding: utf-8 -*-
"""
Simple iOS tests, showing accessing elements and getting/setting text from them.
"""
import unittest
import os
import sys
sys.path.append("../../../../import")
import setup
import element
from random import randint
from appium import webdriver
from time import sleep

class SimpleIOSTests(unittest.TestCase):

    def setUp(self):
        setup.load_for4(self)
        setup.ck_login_ordinary(self)
        element.livehome_element(self)
    def test_page_ad_case3(self):  #進入廣告
        self.driver.tap([(160, 130)])
        self.back = self.driver.find_element_by_accessibility_id('Back')
        self.back.click()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
