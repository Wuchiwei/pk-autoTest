# -*- coding: utf-8 -*-
import unittest
import os
from random import randint
from appium import webdriver
from time import sleep


def setUp(self):    #開啟appium，載入app，3層
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
        Confirm_butten = self.driver.find_element_by_accessibility_id('Confirm')
        Confirm_butten.click()
        massage_allow = self.driver.find_element_by_xpath('//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[6]/XCUIElementTypeOther[2]/XCUIElementTypeAlert[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]')
        massage_allow.click()
        sleep(1)
    except:
        pass


def setUp1(self):    #開啟appium，載入app，2層
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
        Confirm_butten = self.driver.find_element_by_accessibility_id('Confirm')
        Confirm_butten.click()
        massage_allow = self.driver.find_element_by_xpath('//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[6]/XCUIElementTypeOther[2]/XCUIElementTypeAlert[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]')
        massage_allow.click()
        sleep(1)
    except:
        pass


def setUp2(self):    #開啟appium，載入app，4層
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
        Confirm_butten = self.driver.find_element_by_accessibility_id('Confirm')
        Confirm_butten.click()
        massage_allow = self.driver.find_element_by_xpath('//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[6]/XCUIElementTypeOther[2]/XCUIElementTypeAlert[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]')
        massage_allow.click()
        sleep(1)
    except:
        pass


def setUp3(self):    #開啟appium，載入app，5層
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
        Confirm_butten = self.driver.find_element_by_accessibility_id('Confirm')
        Confirm_butten.click()
        massage_allow = self.driver.find_element_by_xpath('//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[6]/XCUIElementTypeOther[2]/XCUIElementTypeAlert[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]')
        massage_allow.click()
        sleep(1)
    except:
        pass

def setUp4(self):    #開啟appium，載入app，6層
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
        Confirm_butten = self.driver.find_element_by_accessibility_id('Confirm')
        Confirm_butten.click()
        massage_allow = self.driver.find_element_by_xpath('//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[6]/XCUIElementTypeOther[2]/XCUIElementTypeAlert[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]')
        massage_allow.click()
        sleep(1)
    except:
        pass


def ck_login(self):   #檢查是否已經登入-普通帳號
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


def ck_login_1(self):   #檢查是否已經登入-主播帳號
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
        self.user_passwd = '11111111'
        self.user_id_test.send_keys(self.user_id)
        self.user_passwd_test.send_keys(self.user_passwd)
        self.login_butten.click()
        sleep(1)
    except:
        pass
