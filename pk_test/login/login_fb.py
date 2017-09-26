# -*- coding: utf-8 -*-
"""
Simple iOS tests, showing accessing elements and getting/setting text from them.
"""
import unittest
import os
import sys
sys.path.append("../../import")
import setup
import element
from random import randint
from appium import webdriver
from time import sleep

class SimpleIOSTests(unittest.TestCase):

    def setUp(self):
        setup.setUp1(self)
        element.login_mode_element(self)

    def test_login_fb(self):
        self.icon_fb_butten.click()
        sleep(8)
        self.contiue_butten = self.driver.find_element_by_accessibility_id('繼續')
        self.contiue_butten.click()
        sleep(5)
        element.livehome_element(self)
        self.assertEqual(u'PK直播', self.pk_title.get_attribute(u'name'))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
