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
        setup.ck_login_anchor(self)
        sleep(2)

    def test_live_anchor_case3(self):
        element.livehome_element(self)
        self.live.click()
        sleep(1)
        element.anchor_live(self)
        self.anchor_live_title.send_keys('test')
        self.anchor_live_money.send_keys('1000')
        self.driver.find_element_by_accessibility_id('Toolbar Done Button').click()
        self.anchor_live_open.click()
        sleep(8)
        element.anchor_live_open(self)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
