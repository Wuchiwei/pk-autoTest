# -*- coding: utf-8 -*-
import unittest
import os
from random import randint
from appium import webdriver
from time import sleep

def load_for2(self):    #開啟appium，載入app，2層
    try:
        app = os.path.abspath('../../app/PKLive-Demo_1_0_1_14.ipa')
        self.driver = webdriver.Remote(
                command_executor='http://127.0.0.1:4723/wd/hub',
                desired_capabilities={
                    'automationName': 'XCUITest',
                    'platformName': 'iOS',
                    'deviceName': 'Z2z',
                    'app': app,
                    'xcodeOrgId': '79V8F6N3Z8',
                    'xcodeSigningId': 'iPhone Developer',
                    'udid': '4a7c6e6b430ba83671a5c1fdc8f8f97de1f0954e'
                    })
    except:
        app = os.path.abspath('../../app/PKLive-InHouse.app')
        self.driver = webdriver.Remote(
                command_executor='http://127.0.0.1:4723/wd/hub',
                desired_capabilities={
                    'app': app,
                    'platformName': 'iOS',
                    'platformVersion': '10.3',
                    'deviceName': 'iPhone 6',
                    })
    sleep(1)
    try:
        Confirm_butten = self.driver.find_element_by_accessibility_id('確定')
        Confirm_butten.click()
        massage_allow = self.driver.find_element_by_xpath('//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[6]/XCUIElementTypeOther[2]/XCUIElementTypeAlert[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]')
        massage_allow.click()
        sleep(1)
    except:
        pass

def load_for3(self):    #開啟appium，載入app，3層
    try:
        app = os.path.abspath('../../../app/PKLive-Demo_1_0_1_14.ipa')
        self.driver = webdriver.Remote(
                command_executor='http://127.0.0.1:4723/wd/hub',
                desired_capabilities={
                    'automationName': 'XCUITest',
                    'platformName': 'iOS',
                    'deviceName': 'Z2z',
                    'app': app,
                    'xcodeOrgId': '79V8F6N3Z8',
                    'xcodeSigningId': 'iPhone Developer',
                    'udid': '4a7c6e6b430ba83671a5c1fdc8f8f97de1f0954e'
                    })
    except:
        app = os.path.abspath('../../../app/PKLive-InHouse.app')
        self.driver = webdriver.Remote(
                command_executor='http://127.0.0.1:4723/wd/hub',
                desired_capabilities={
                    'app': app,
                    'platformName': 'iOS',
                    'platformVersion': '10.3',
                    'deviceName': 'iPhone 6',
                    })
    sleep(1)
    try:
        Confirm_butten = self.driver.find_element_by_accessibility_id('確定')
        Confirm_butten.click()
        massage_allow = self.driver.find_element_by_xpath('//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[6]/XCUIElementTypeOther[2]/XCUIElementTypeAlert[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]')
        massage_allow.click()
        sleep(1)
    except:
        pass

def load_for4(self):    #開啟appium，載入app，4層
    try:
        app = os.path.abspath('../../../../app/PKLive-Demo_1_0_1_14.ipa')
        self.driver = webdriver.Remote(
                command_executor='http://127.0.0.1:4723/wd/hub',
                desired_capabilities={
                    'automationName': 'XCUITest',
                    'platformName': 'iOS',
                    'deviceName': 'Z2z',
                    'app': app,
                    'xcodeOrgId': '79V8F6N3Z8',
                    'xcodeSigningId': 'iPhone Developer',
                    'udid': '4a7c6e6b430ba83671a5c1fdc8f8f97de1f0954e'
                    })
    except:
        app = os.path.abspath('../../../../app/PKLive-InHouse.app')
        self.driver = webdriver.Remote(
                command_executor='http://127.0.0.1:4723/wd/hub',
                desired_capabilities={
                    'app': app,
                    'platformName': 'iOS',
                    'platformVersion': '10.3',
                    'deviceName': 'iPhone 6',
                    })
    sleep(1)
    try:
        Confirm_butten = self.driver.find_element_by_accessibility_id('確定')
        Confirm_butten.click()
        massage_allow = self.driver.find_element_by_xpath('//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[6]/XCUIElementTypeOther[2]/XCUIElementTypeAlert[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]')
        massage_allow.click()
        sleep(1)
    except:
        pass

def load_for5(self):    #開啟appium，載入app，5層
    try:
        app = os.path.abspath('../../../../../app/PKLive-Demo_1_0_1_14.ipa')
        self.driver = webdriver.Remote(
                command_executor='http://127.0.0.1:4723/wd/hub',
                desired_capabilities={
                    'automationName': 'XCUITest',
                    'platformName': 'iOS',
                    'deviceName': 'Z2z',
                    'app': app,
                    'xcodeOrgId': '79V8F6N3Z8',
                    'xcodeSigningId': 'iPhone Developer',
                    'udid': '4a7c6e6b430ba83671a5c1fdc8f8f97de1f0954e'
                    })
    except:
        app = os.path.abspath('../../../../../app/PKLive-InHouse.app')
        self.driver = webdriver.Remote(
                command_executor='http://127.0.0.1:4723/wd/hub',
                desired_capabilities={
                    'app': app,
                    'platformName': 'iOS',
                    'platformVersion': '10.3',
                    'deviceName': 'iPhone 6',
                    })
    sleep(1)
    try:
        Confirm_butten = self.driver.find_element_by_accessibility_id('確定')
        Confirm_butten.click()
        massage_allow = self.driver.find_element_by_xpath('//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[6]/XCUIElementTypeOther[2]/XCUIElementTypeAlert[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]')
        massage_allow.click()
        sleep(1)
    except:
        pass

def load_for6(self):    #開啟appium，載入app，6層
    try:
        app = os.path.abspath('../../../../../../app/PKLive-Demo_1_0_1_14.ipa')
        self.driver = webdriver.Remote(
                command_executor='http://127.0.0.1:4723/wd/hub',
                desired_capabilities={
                    'automationName': 'XCUITest',
                    'platformName': 'iOS',
                    'deviceName': 'Z2z',
                    'app': app,
                    'xcodeOrgId': '79V8F6N3Z8',
                    'xcodeSigningId': 'iPhone Developer',
                    'udid': '4a7c6e6b430ba83671a5c1fdc8f8f97de1f0954e'
                    })
    except:
        app = os.path.abspath('../../../../../../app/PKLive-InHouse.app')
        self.driver = webdriver.Remote(
                command_executor='http://127.0.0.1:4723/wd/hub',
                desired_capabilities={
                    'app': app,
                    'platformName': 'iOS',
                    'platformVersion': '10.3',
                    'deviceName': 'iPhone 6',
                    })
    sleep(1)
    try:
        Confirm_butten = self.driver.find_element_by_accessibility_id('確定')
        Confirm_butten.click()
        massage_allow = self.driver.find_element_by_xpath('//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[6]/XCUIElementTypeOther[2]/XCUIElementTypeAlert[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]')
        massage_allow.click()
        sleep(1)
    except:
        pass

def ck_login_ordinary(self):   #檢查是否已經登入-普通帳號
    try:
        icon_phone_butten = self.driver.find_element_by_accessibility_id('icon phone')
        icon_phone_butten.click()
    except:
        pass
    sleep(2)
    try:
        self.user_id_test = self.driver.find_element_by_xpath('//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTextField[1]')
        self.user_passwd_test = self.driver.find_element_by_xpath('//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeSecureTextField[1]')
        self.login_butten = self.driver.find_element_by_accessibility_id('登入')
        self.user_id = 'amTeddy'
        self.user_passwd = '42691667'
        self.user_id_test.send_keys(self.user_id)
        self.user_passwd_test.send_keys(self.user_passwd)
        self.login_butten.click()
        sleep(1)
    except:
        pass

def ck_login_anchor(self):   #檢查是否已經登入-主播帳號
    try:
        icon_phone_butten = self.driver.find_element_by_accessibility_id('icon phone')
        icon_phone_butten.click()
    except:
        pass
    sleep(2)
    try:
        self.user_id_test = self.driver.find_element_by_xpath('//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTextField[1]')
        self.user_passwd_test = self.driver.find_element_by_xpath('//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeSecureTextField[1]')
        self.login_butten = self.driver.find_element_by_accessibility_id('登入')
        self.user_id = 'amanchor04'
        self.user_passwd = '11111111'
        self.user_id_test.send_keys(self.user_id)
        self.user_passwd_test.send_keys(self.user_passwd)
        self.login_butten.click()
        sleep(1)
    except:
        pass
