# -*- coding: utf-8 -*-

import unittest
import os
import sys
sys.path.append("../../../../../../import")
import setup
import element
from random import randint
from appium import webdriver
from time import sleep

class SimpleIOSTests(unittest.TestCase):

    def setUp(self):
        # set up appium
        setup.load_for6(self)
        setup.ck_login_ordinary(self)
        sleep(1)

    def test_ordinary_otherset_case7(self):#原先密碼與新密碼皆未輸入
        element.livehome_element(self)
        self.info.click()
        sleep(2)
        element.livehome_info(self)
        self.other_set.click()
        sleep(1)
        element.other_set(self)
        self.privacy_butten.click()
        sleep(1)
        self.driver.find_element_by_accessibility_id('隱私權保護政策')
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
