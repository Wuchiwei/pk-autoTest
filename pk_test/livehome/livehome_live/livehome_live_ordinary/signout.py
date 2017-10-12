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
        sleep(1)

    def test_signout_case(self):
        element.livehome_element(self)
        self.info.click()
        sleep(1)
        try:
            element.livehome_info(self)
            self.sign_out_butten.click()
        except:
            element.anchor_info(self)
            self.anchor_info_out.click()

        sleep(2)
        element.login_mode_element(self)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
