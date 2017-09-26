# -*- coding: utf-8 -*-
"""
Simple iOS tests, showing accessing elements and getting/setting text from them.
"""
import unittest
import os
from random import randint
from appium import webdriver
from time import sleep
import random

class SimpleIOSTests(unittest.TestCase):

    def setUp(self):
        # set up appium
        app = os.path.abspath('../../app/PKLive-InHouse.app')
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': app,
                'platformName': 'iOS',
                'platformVersion': '10.3',
                'deviceName': 'iPhone 6',
            })
        try:
            Confirm_butten = self.driver.find_element_by_accessibility_id('Confirm')
            Confirm_butten.click()
            massage_allow = self.driver.find_element_by_xpath('//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[6]/XCUIElementTypeOther[2]/XCUIElementTypeAlert[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]')
            massage_allow.click()
            sleep(1)
        except:
            pass

        try:
            icon_phone_butten = self.driver.find_element_by_accessibility_id('icon phone')
            icon_phone_butten.click()
            sleep(1)
            go_registe_butten = self.driver.find_element_by_accessibility_id('前往註冊')
            go_registe_butten.click()
            sleep(1)
        except:
            pass

        self.user_id_test = self.driver.find_element_by_xpath('//XCUIElementTypeOther[1]/XCUIElementTypeTextField[1]')
        self.user_id = ''
        for i in range(8):
            rnd = random.choice('abcdefghijklmnopqr')
            self.user_id += rnd


        #self.user_id = 'trvsdfli'
        self.passwd_test = self.driver.find_element_by_xpath('//XCUIElementTypeOther[1]/XCUIElementTypeSecureTextField[1]')
        self.passwd = 'asdfgh'
        self.agn_passwd_test = self.driver.find_element_by_xpath('//XCUIElementTypeOther[1]/XCUIElementTypeSecureTextField[2]')
        self.agn_passwd = 'asdfgh'
        self.phone_nub_test = self.driver.find_element_by_xpath('//XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTextField[3]')
        self.phone_nub = '0911111111'
        self.registe_butten = self.driver.find_element_by_accessibility_id('註冊')

    def test_regist_seccs(self):
        self.assertEqual(u'註冊', self.registe_butten.get_attribute(u'name'))
        self.user_id_test.send_keys(self.user_id)
        self.passwd_test.send_keys(self.passwd)
        self.agn_passwd_test.send_keys(self.agn_passwd)
        self.phone_nub_test.send_keys(self.phone_nub)
        self.done_butten = self.driver.find_element_by_accessibility_id('Toolbar Done Button')
        self.done_butten.click()
        self.registe_butten.click()
        sleep(3)
        self.message = self.driver.find_element_by_accessibility_id('驗證簡訊')
        self.assertEqual(u'驗證簡訊', self.message.get_attribute(u'name'))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
