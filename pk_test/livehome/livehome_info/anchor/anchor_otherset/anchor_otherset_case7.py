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

    def test_otherset_case7(self):
        element.livehome_element(self)
        self.info.click()
        sleep(1)
        element.anchor_info(self)
        self.anchor_info_otherset.click()
        sleep(1)
        element.anchor_info_otherset(self)
        self.login_value1 = int (self.anchor_info_otherset_morelogin.get_attribute('value')) +1
        if self.login_value1 > 1 :
            self.login_value1 = 0
        self.anchor_info_otherset_morelogin.click()
        sleep(1)
        self.driver.tap([(16, 45)])
        sleep(1)
        element.anchor_info(self)
        self.anchor_info_otherset.click()
        sleep(1)
        self.login_value2 = self.anchor_info_otherset_morelogin.get_attribute('value')
        self.assertEqual(self.login_value1,self.login_value2)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
