# -*- coding: utf-8 -*-
import unittest
import os
from random import randint
from appium import webdriver
from time import sleep

def login_mode_element(self): #選擇登入方式元件
    self.icon_fb_butten = self.driver.find_element_by_accessibility_id('icon facebook')
    self.icon_phone_butten = self.driver.find_element_by_accessibility_id('icon phone')

def login_phone_element(self): #普通登入頁面元件
    self.user_id_test = self.driver.find_element_by_xpath('//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTextField[1]')
    self.user_passwd_test = self.driver.find_element_by_xpath('//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeSecureTextField[1]')
    self.login_butten = self.driver.find_element_by_accessibility_id('Login')
    self.go_registe_butten = self.driver.find_element_by_accessibility_id('前往註冊')

def registe_element(self): #註冊頁面元件
    self.user_id_test = self.driver.find_element_by_xpath('//XCUIElementTypeOther[1]/XCUIElementTypeTextField[1]')
    self.passwd_test = self.driver.find_element_by_xpath('//XCUIElementTypeOther[1]/XCUIElementTypeSecureTextField[1]')
    self.agn_passwd_test = self.driver.find_element_by_xpath('//XCUIElementTypeOther[1]/XCUIElementTypeSecureTextField[2]')
    self.phone_nub_test = self.driver.find_element_by_xpath('//XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTextField[3]')
    self.registe_butten = self.driver.find_element_by_accessibility_id('註冊')

def livehome_element(self): #PK直播大廳元件
    self.pk_title = self.driver.find_element_by_accessibility_id('PK直播')
    self.game = self.driver.find_element_by_xpath('//XCUIElementTypeOther[1]/XCUIElementTypeTabBar[1]/XCUIElementTypeButton[1]')
    self.home = self.driver.find_element_by_xpath('//XCUIElementTypeOther[1]/XCUIElementTypeTabBar[1]/XCUIElementTypeButton[2]')
    self.live = self.driver.find_element_by_xpath('//XCUIElementTypeOther[1]/XCUIElementTypeTabBar[1]/XCUIElementTypeButton[3]')
    self.info = self.driver.find_element_by_xpath('//XCUIElementTypeOther[1]/XCUIElementTypeTabBar[1]/XCUIElementTypeButton[4]')

def livehome_info(self):  #個人資料頁面元件
    self.sign_out_butten = self.driver.find_element_by_accessibility_id('登出')
    self.profile_edit_butten = self.driver.find_element_by_accessibility_id('icon profile edit')
    self.nickname = self.driver.find_element_by_xpath('//XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeStaticText[2]')
    self.go_store = self.driver.find_element_by_accessibility_id('我要儲值')
    self.transac_record = self.driver.find_element_by_accessibility_id('交易紀錄')
    self.pk_record = self.driver.find_element_by_accessibility_id('PK紀錄')
    self.my_follow = self.driver.find_element_by_accessibility_id('我的追蹤')
    self.other_set = self.driver.find_element_by_accessibility_id('其他設定')

def edit_info(self): #編輯個人資料頁面元件
    self.edit_info_title = self.driver.find_element_by_accessibility_id('編輯個人資料')
    self.cencel_butten = self.driver.find_element_by_accessibility_id('取消')
    self.set_butten = self.driver.find_element_by_accessibility_id('儲存')
    self.ch_photo = self.driver.find_element_by_accessibility_id('更換大頭照')
    self.ch_passwd = self.driver.find_element_by_accessibility_id('變更密碼')
    self.ch_nickname = self.driver.find_element_by_xpath('//XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[3]/XCUIElementTypeTextField[1]')
    self.ch_birthday = self.driver.find_element_by_xpath('//XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[4]/XCUIElementTypeTextField[1]')
    self.ch_mail = self.driver.find_element_by_xpath('//XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[5]/XCUIElementTypeTextField[1]')
    self.ch_phone = self.driver.find_element_by_xpath('//XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[6]/XCUIElementTypeStaticText[1]')

def go_store(self): #我要儲值頁面元件
    self.store_title = self.driver.find_element_by_accessibility_id('儲值中心')
    self.store_back = self.driver.find_element_by_accessibility_id('icon nav back white')

def transac_record(self): #交易紀錄頁面元件
    self.transac_record_title = self.driver.find_element_by_accessibility_id('交易紀錄')
    self.transac_record_back = self.driver.find_element_by_accessibility_id('Back')

def pk_record(self): #pk紀錄頁面元件
    self.pk_record_title = self.driver.find_element_by_accessibility_id('PK紀錄')
    self.pk_record_back = self.driver.find_element_by_accessibility_id('Back')

def my_follow(self): #我的追蹤頁面元件
    self.my_follow_title = self.driver.find_element_by_accessibility_id('我的追蹤')
    self.pk_record_back = self.driver.find_element_by_accessibility_id('Back')

def other_set(self): #我的追蹤頁面元件
    self.other_set_title = self.driver.find_element_by_accessibility_id('其他設定')
    self.pk_record_back = self.driver.find_element_by_accessibility_id('Back')
    self.multiple_devices = self.driver.find_element_by_accessibility_id('允許多裝置同時登入')
    self.receive = self.driver.find_element_by_accessibility_id('願意收到所有關於PK Live的通知')
    self.problem_butten = self.driver.find_element_by_accessibility_id('常見問題')
    self.call_me_butten = self.driver.find_element_by_accessibility_id('聯絡我們')
    self.serve_butten = self.driver.find_element_by_accessibility_id('服務條款')
    self.rule_butten = self.driver.find_element_by_accessibility_id('用戶規章')
    self.privacy_butten = self.driver.find_element_by_accessibility_id('隱私權保護政策')
    self.evaluate_butten = self.driver.find_element_by_accessibility_id('給個好評吧')
