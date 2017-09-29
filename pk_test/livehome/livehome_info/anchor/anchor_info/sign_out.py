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
        setup.setUp3(self)
        sleep(1)

    def test_sign_out(self):
        try:
            element.livehome_element(self)
            self.info.click()
            sleep(2)
            element.livehome_info(self)
            self.sign_out_butten.click()
            sleep(2)
        except:
            pass
        element.login_mode_element(self)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
