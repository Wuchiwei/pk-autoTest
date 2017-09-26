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
        self.icon_phone_butten.click()
        sleep(1)
        element.login_phone_element(self)

    def test_login_case3(self):
        self.user_id = 'amTeddy'
        self.user_passwd = '42691667'

        self.user_id_test.send_keys(self.user_id)
        self.user_passwd_test.send_keys(self.user_passwd)
        self.login_butten.click()
        sleep(3)
        element.livehome_element(self)
        self.assertEqual(u'PK直播', self.pk_title.get_attribute(u'name'))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
