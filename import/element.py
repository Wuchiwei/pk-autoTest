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
    self.user_id_test = self.driver.find_element_by_xpath('//XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTextField[1]')
    self.user_passwd_test = self.driver.find_element_by_xpath('//XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeSecureTextField[1]')
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

def livehome_game(self):
    self.livehome_game_title = self.driver.find_element_by_accessibility_id('遊戲大廳')
    self.livehome_game_ad = self.driver.find_element_by_xpath('//XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[1]')
    self.livehome_game_electronic = self.driver.find_element_by_xpath('//XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[2]/XCUIElementTypeCollectionView[1]')
    #game_electronic -->  self.driver.tap([(100, 330)])
    self.livehome_game_popular = self.driver.find_element_by_xpath('//XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[3]/XCUIElementTypeOther[1]')
    #game_popular --> self.driver.tap([(140, 535)])

def livehome_game_popular(self):
    self.livehome_game_popular_back = self.driver.find_element_by_accessibility_id('icon nav back white')
    self.livehome_game_popular_pk = self.driver.find_element_by_accessibility_id('PK !')
    self.livehome_game_popula_coin = self.driver.find_element_by_xpath('//XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[5]/XCUIElementTypeStaticText[1]')
    self.livehome_game_popula_diamonds = self.driver.find_element_by_xpath('//XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[5]/XCUIElementTypeStaticText[2]')
    self.livehome_game_popula_store = self.driver.find_element_by_accessibility_id('儲值')
    self.livehome_game_popula_pkrecord = self.driver.find_element_by_accessibility_id('PK紀錄')

def livehome_live(self):  #開啟直播頁面元件
    self.live_message = self.driver.find_element_by_accessibility_id('開啟直播')
    self.live_connect = self.driver.find_element_by_accessibility_id('聯絡客服，我要當主播')
    self.live_signout = self.driver.find_element_by_accessibility_id('登出')
    self.live_next = self.driver.find_element_by_accessibility_id('下次再說囉！')

def livehome_info(self):  #個人資料頁面元件
    self.sign_out_butten = self.driver.find_element_by_accessibility_id('登出')
    self.livehome_info_diamonds = self.driver.find_element_by_xpath('//XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeStaticText[1]')
    self.livehome_info_coin = self.driver.find_element_by_xpath('//XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeStaticText[5]')
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

#---------------------------------主播-----------------------------------------------------

def anchor_info(self): #主播帳號個人頁面元件
    self.anchor_info_out = self.driver.find_element_by_accessibility_id('登出')  #登出
    self.anchor_info_nickname = self.driver.find_element_by_xpath('//XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeStaticText[1]')
    self.anchor_info_page = self.driver.find_element_by_accessibility_id('個人資訊頁管理')
    self.anchor_info_report = self.driver.find_element_by_accessibility_id('收益報表')
    self.anchor_info_redlist = self.driver.find_element_by_accessibility_id('黑名單 / 紅名單')
    self.anchor_info_rank = self.driver.find_element_by_accessibility_id('送禮及競猜排行榜')
    self.anchor_info_otherset = self.driver.find_element_by_accessibility_id('其他設定')

def edit_anchor_info(self):#主播帳號編輯個人資訊頁管理
    self.edit_anchor_info_set = self.driver.find_element_by_accessibility_id('儲存')
    self.edit_anchor_info_cancel = self.driver.find_element_by_accessibility_id('取消')
    self.edit_anchor_info_chphoto = self.driver.find_element_by_accessibility_id('更換大頭照')
    self.edit_anchor_info_chpasswd = self.driver.find_element_by_accessibility_id('變更密碼')
    self.edit_anchor_info_nickname = self.driver.find_element_by_xpath('//XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[3]/XCUIElementTypeTextField[1]')
    self.edit_anchor_info_birthday = self.driver.find_element_by_xpath('//XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[4]/XCUIElementTypeTextField[1]')
    self.edit_anchor_info_introducte = self.driver.find_element_by_xpath('//XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[5]/XCUIElementTypeTextView[1]')

def edit_anchor_info_chpasswd_page(self):#主播變更密碼頁面
    self.edit_anchor_info_chpasswd_page_passwd = self.driver.find_element_by_xpath('///XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeSecureTextField[1]')
    self.edit_anchor_info_chpasswd_page_newpasswd = self.driver.find_element_by_xpath('//XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeSecureTextField[2]')
    self.edit_anchor_info_chpasswd_page_define = self.driver.find_element_by_accessibility_id('確定')

def anchor_info_report(self):#主播收益報表頁面
    self.anchor_info_report_title = self.driver.find_element_by_accessibility_id('收益報表 ▼')
    self.anchor_info_report_day = self.driver.find_element_by_xpath('//XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeStaticText[1]')
    self.anchor_info_report_giftincome = self.driver.find_element_by_xpath('//XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[1]')
    self.anchor_info_report_pkincome = self.driver.find_element_by_xpath('//XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[2]')
    self.anchor_info_report_back = self.driver.find_element_by_accessibility_id('Back')
def anchor_info_report_dateform(self):#主播收益報表日期表單
    self.anchor_info_report_date1 = self.driver.find_element_by_xpath('//XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeButton[1]')
    self.anchor_info_report_date2 = self.driver.find_element_by_xpath('//XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeButton[2]')
    self.anchor_info_report_date3 = self.driver.find_element_by_xpath('//XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeButton[3]')

def anchor_info_otherset(self): #主播其他設定
    self.anchor_info_otherset_problem = self.driver.find_element_by_accessibility_id('常見問題')
    self.anchor_info_otherset_contact = self.driver.find_element_by_accessibility_id('聯絡我們')
    self.anchor_info_otherset_service = self.driver.find_element_by_accessibility_id('服務條款')
    self.anchor_info_otherset_rule = self.driver.find_element_by_accessibility_id('用戶規章')
    self.anchor_info_otherset_privacy = self.driver.find_element_by_accessibility_id('隱私權保護政策')
    self.anchor_info_otherset_review = self.driver.find_element_by_accessibility_id('給個好評吧')
    self.anchor_info_otherset_morelogin = self.driver.find_element_by_xpath('//XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[1]/XCUIElementTypeSwitch[1]')
    self.anchor_info_otherset_notice = self.driver.find_element_by_xpath('//XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[2]/XCUIElementTypeSwitch[1]')


def anchor_live(self): #主播開播頁面
    self.anchor_live_title = self.driver.find_element_by_xpath('//XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTextField[1]')
    self.anchor_live_rank = self.driver.find_element_by_xpath('//XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeTextField[1]')
    self.anchor_live_game = self.driver.find_element_by_xpath('//XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeButton[1]')
    self.anchor_live_money = self.driver.find_element_by_xpath('//XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTextField[2]')
    self.anchor_live_open = self.driver.find_element_by_accessibility_id('開始直播')

def anchor_live_game(self): #主播開播頁面的預測遊戲
    self.anchor_live_game_clean = self.driver.find_element_by_accessibility_id('清除')
    self.anchor_live_game_title = self.driver.find_element_by_accessibility_id('遊戲分類')
    self.anchor_live_game_stop = self.driver.find_element_by_accessibility_id('Stop')
    self.anchor_live_game_list = self.driver.find_element_by_xpath('//XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[1]')

def anchor_live_open(self): #主播開啟直播後畫面
    self.anchor_live_open_message = self.driver.find_element_by_accessibility_id('icon message')
    self.anchor_live_open_switchcam = self.driver.find_element_by_accessibility_id('icon switchcam')
    self.anchor_live_open_gamepanel = self.driver.find_element_by_accessibility_id('icon game panel')
    self.anchor_live_open_share = self.driver.find_element_by_accessibility_id('icon share')
