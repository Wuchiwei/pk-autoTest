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
        setup.ck_login_anchor(self)
        sleep(1)

    def test_ch_introducte_case(self):#原先密碼與新密碼皆未輸入
        element.livehome_element(self)
        self.info.click()
        sleep(1)
        element.anchor_info(self)
        self.anchor_info_page.click()
        sleep(1)
        element.edit_anchor_info(self)
        self.data = self.edit_anchor_info_introducte.get_attribute(u'value')
        self.edit_anchor_info_introducte.send_keys(u'哈囉我是柚子')
        self.edit_anchor_info_set.click()
        sleep(2)
        element.anchor_info(self)
        self.anchor_info_page.click()
        sleep(1)
        self.assertEqual((u'哈囉我是柚子'+self.data),self.edit_anchor_info_introducte.get_attribute(u'value'))
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
