# -*- coding: utf-8 -*-
"""
Simple iOS tests, showing accessing elements and getting/setting text from them.
"""
import unittest
import os
import sys
sys.path.append("../../../import")
import setup
import element
from random import randint
from appium import webdriver
from time import sleep

class SimpleIOSTests(unittest.TestCase):

    def setUp(self):
        # set up appium
        setup.setUp(self)

    def test_sign_out(self):
        try:
            element.livehome_element(self)
            self.info.click()
            sleep(1)
            element.livehome_info(self)
            self.sign_out_butten.click()
            sleep(1)
        except:
            pass

        element.login_mode_element(self)
        self.assertEqual('icon phone', self.icon_phone_butten.get_attribute('name'))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
