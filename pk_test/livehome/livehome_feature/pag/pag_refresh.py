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
        setup.setUp2(self)
        setup.ck_login(self)
        element.livehome_element(self)

    def test_page_refresh_case2(self): #刷新頁面
        self.driver.swipe(start_x=45, start_y=240, end_x=45, end_y=400, duration=800)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
