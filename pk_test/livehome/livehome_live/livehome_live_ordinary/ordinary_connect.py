# -*- coding: utf-8 -*-

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
        # set up appium
        setup.load_for4(self)
        setup.ck_login_ordinary(self)
        sleep(2)

    def test_ordinary_connect_case(self):
        element.livehome_element(self)
        self.live.click()
        sleep(1)
        element.livehome_live(self)
        self.live_connect.click()
        sleep(5)
        self.driver.find_element_by_accessibility_id('聯絡我們')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
