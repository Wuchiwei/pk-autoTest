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

    def test_live_anchor_case6(self):
        element.livehome_element(self)
        self.live.click()
        sleep(1)
        element.anchor_live(self)
        self.anchor_live_rank.click()
        self.driver.swipe(start_x=191, start_y=593, end_x=191, end_y=541, duration=1000) #上下滑動有問題
        self.driver.find_element_by_accessibility_id('Toolbar Done Button').click()
        self.assertEqual(u'金牌(2) ▼',(self.anchor_live_rank.get_attribute('value')))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
