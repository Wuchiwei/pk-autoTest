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
        setup.setUp4(self)
        sleep(1)

    def test_anchor_chpasswd_case4(self):#原先密碼輸入錯誤與新密碼空白
        element.livehome_element(self)
        self.info.click()
        sleep(1)
        element.anchor_info(self)
        self.anchor_info_page.click()
        sleep(1)
        element.edit_anchor_info(self)
        self.edit_anchor_info_chpasswd.click()
        sleep(1)
        element.edit_anchor_info_chpasswd_page(self)
        self.edit_anchor_info_chpasswd_page_passwd.send_keys('22222222')
        self.edit_anchor_info_chpasswd_page_newpasswd.send_keys('')
        self.edit_anchor_info_chpasswd_page_define.click()
        element.edit_anchor_info_chpasswd_page(self)
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
