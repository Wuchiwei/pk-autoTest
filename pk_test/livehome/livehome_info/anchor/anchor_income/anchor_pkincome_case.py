# -*- coding: utf-8 -*-

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
        setup.ck_login_anchor(self)
        sleep(1)

    def test_pkincome_case(self):
        element.livehome_element(self)
        self.info.click()
        sleep(1)
        element.anchor_info(self)
        self.anchor_info_report.click()
        sleep(1)
        element.anchor_info_report(self)
        sleep(1)
        self.anchor_info_report_pkincome.click()
        sleep(5)
        self.driver.find_element_by_accessibility_id('總計：')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
