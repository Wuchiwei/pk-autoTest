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
        sleep(1)

    def test_anchor_chpasswd_reset(self):#原先密碼輸入錯誤與新密碼空白
        try:
            icon_phone_butten = self.driver.find_element_by_accessibility_id('icon phone')
            icon_phone_butten.click()
        except:
            pass
        sleep(2)
        try:
            self.user_id_test = self.driver.find_element_by_xpath('//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTextField[1]')
            self.user_passwd_test = self.driver.find_element_by_xpath('//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeSecureTextField[1]')
            self.login_butten = self.driver.find_element_by_accessibility_id('Login')
            self.user_id = 'amanchor04'
            self.user_passwd = '111111111'
            self.user_id_test.send_keys(self.user_id)
            self.user_passwd_test.send_keys(self.user_passwd)
            self.login_butten.click()
            sleep(1)
        except:
            pass
        sleep(2)
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
        self.edit_anchor_info_chpasswd_page_passwd.send_keys('111111111')
        self.edit_anchor_info_chpasswd_page_newpasswd.send_keys('11111111')
        self.edit_anchor_info_chpasswd_page_define.click()
        self.driver.find_element_by_accessibility_id('Done').click()
        sleep(1)
        element.login_mode_element(self)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
