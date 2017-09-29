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

    def test_anchor_chpasswd(self):
        element.livehome_element(self)
        self.info.click()
        sleep(1)
        element.anchor_info(self)
        self.anchor_info_page.click()
        sleep(1)
        

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
