# -*- coding: utf-8 -*-

import unittest
import os
import setup
from random import randint
from appium import webdriver
from time import sleep

def game_ordinary_store(self):
    self.livehome_game_popula_store.click()
    self.driver.find_element_by_accessibility_id('儲值中心')

def game_ordinary_pkrecord(self):
    self.livehome_game_popula_pkrecord.click()
    self.driver.find_element_by_accessibility_id('PK紀錄')

def game_ordinary_overage(self):
    self.coin1 = int(self.livehome_game_popula_coin.get_attribute('value').replace(',',''))
    self.diamonds1 = int(self.livehome_game_popula_diamonds.get_attribute('value').replace(',',''))
    self.livehome_game_popular_back.click()
    sleep(1)
    self.home.click()
    sleep(1)
    self.driver.tap([(160, 280)])
    sleep(1)
    self.gift_butten = self.driver.find_element_by_accessibility_id('icon gift')
    self.gift_butten.click()
    sleep(1)
    self.diamonds2_value = self.driver.find_element_by_xpath('//XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[2]')
    self.diamonds2 = int(  self.diamonds2_value.get_attribute('value').replace(',',''))
    self.coin2_value = self.driver.find_element_by_xpath('//XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[1]')
    self.coin2 = int(  self.coin2_value.get_attribute('value').replace(',',''))
    self.assertEqual(self.coin1 ,self.coin2)
    self.assertEqual(self.diamonds1 ,self.diamonds2)

def game_ordinary_betting(self):
    self.coin1 = int(self.livehome_game_popula_coin.get_attribute('value').replace(',',''))
    self.diamonds1 = int(self.livehome_game_popula_diamonds.get_attribute('value').replace(',',''))

    self.total = 0
    if  self.coin1 < 1000 :
        self.total = self.coin1 + self.diamonds1
        self.total = self.total - 1000
        self.diamonds1 = self.total
        self.coin1 = 0
    else :
        self.coin1 = self.coin1 - 1000

    self.livehome_game_popular_pk.click()
    self.driver.find_element_by_xpath('//XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[5]/XCUIElementTypeTextField[1]').send_keys(1000)
    self.driver.find_element_by_accessibility_id('確定').click()
    self.driver.find_element_by_accessibility_id('Done').click()
    sleep(2)
    self.coin2 = int(self.livehome_game_popula_coin.get_attribute('value').replace(',',''))
    self.diamonds2 = int(self.livehome_game_popula_diamonds.get_attribute('value').replace(',',''))
    self.assertEqual(self.diamonds1, self.diamonds2)
    self.assertEqual(self.coin1, self.coin2)

def game_ordinary_betting_short(self):
    self.coin1 = int(self.livehome_game_popula_coin.get_attribute('value').replace(',',''))
    self.diamonds1 = int(self.livehome_game_popula_diamonds.get_attribute('value').replace(',',''))
    self.livehome_game_popular_pk.click()
    self.driver.find_element_by_xpath('//XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[5]/XCUIElementTypeTextField[1]').send_keys(200)
    self.driver.find_element_by_accessibility_id('確定').click()
    sleep(1)
    self.coin2 = int(self.livehome_game_popula_coin.get_attribute('value').replace(',',''))
    self.diamonds2 = int(self.livehome_game_popula_diamonds.get_attribute('value').replace(',',''))
    self.assertEqual(self.diamonds1, self.diamonds2)
    self.assertEqual(self.coin1, self.coin2)
