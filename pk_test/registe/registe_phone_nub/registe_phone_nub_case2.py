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
        setup.setUp(self)
        element.login_mode_element(self)
        self.icon_phone_butten.click()
        sleep(1)
        element.login_phone_element(self)
        self.go_registe_butten.click()
        sleep(1)

    def test_userid_case2(self):
        element.registe_element(self)
        self.user_id = 'dfgfhymjk'
        self.passwd = 'asdfgh'
        self.agn_passwd = 'asdfgh'
        self.phone_nub = '09111'

        self.user_id_test.send_keys(self.user_id)
        self.passwd_test.send_keys(self.passwd)
        self.agn_passwd_test.send_keys(self.agn_passwd)
        self.phone_nub_test.send_keys(self.phone_nub)

        self.done_butten = self.driver.find_element_by_accessibility_id('Toolbar Done Button')
        self.done_butten.click()
        self.registe_butten.click()
        sleep(1)
        self.assertEqual(u'註冊', self.registe_butten.get_attribute(u'name'))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
