# -*- coding: utf-8 -*-
"""
Simple iOS tests, showing accessing elements and getting/setting text from them.
"""
import unittest
import os
from random import randint
from appium import webdriver
from time import sleep

class SimpleIOSTests(unittest.TestCase):

    def setUp(self):
        # set up appium
        app = os.path.abspath('../../../../../app/PKLive-InHouse.app')
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
        except:
            pass
        sleep(2)
        try:
            self.user_id_test = self.driver.find_element_by_xpath('//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTextField[1]')
            self.user_passwd_test = self.driver.find_element_by_xpath('//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeSecureTextField[1]')
            self.login_butten = self.driver.find_element_by_accessibility_id('Login')
            self.user_id = 'amTeddy'
            self.user_passwd = '42691667'
            self.user_id_test.send_keys(self.user_id)
            self.user_passwd_test.send_keys(self.user_passwd)
            self.login_butten.click()
            sleep(1)
        except:
            pass

        self.pk_title = self.driver.find_element_by_accessibility_id('PK直播')

    def test_popular_imnofollow_case1(self):  #粉絲數量立即變化

        self.driver.tap([(160, 280)])
        self.fans_value1 = self.driver.find_element_by_xpath('//XCUIElementTypeTable[1]/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[4]')
        sum = int(self.fans_value1.get_attribute('value')) - 1
        self.icon_follow = self.driver.find_element_by_accessibility_id('icon follow')
        self.icon_follow.click()
        sleep(1)
        self.fans_value2 = self.driver.find_element_by_xpath('//XCUIElementTypeTable[1]/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[4]')
        self.assertEqual(int(sum), int(self.fans_value2.get_attribute('value')))




if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
