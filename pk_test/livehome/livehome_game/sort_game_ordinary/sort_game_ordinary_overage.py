# -*- coding: utf-8 -*-

import unittest
import os
import sys
sys.path.append("../../../../import")
import setup
import element
sys.path.append("../function_game")
import function_game
from random import randint
from appium import webdriver
from time import sleep

class SimpleIOSTests(unittest.TestCase):

    def setUp(self):
        # set up appium
        setup.load_for4(self)
        setup.ck_login_ordinary(self)
        sleep(2)

    def test_sort_game_ordinary_overage_case(self):
        element.livehome_element(self)
        self.game.click()
        sleep(2)
        element.livehome_game(self)
        self.driver.swipe(190,590,0,-530)
        self.driver.tap([(57, 480)])
        sleep(1)
        self.driver.tap([(57, 480)])
        sleep(1)
        element.livehome_game_popular(self)
        self.coin1 = int(self.livehome_game_popula_coin.get_attribute('value').replace(',',''))
        self.diamonds1 = int(self.livehome_game_popula_diamonds.get_attribute('value').replace(',',''))
        self.livehome_game_popular_back.click()
        sleep(1)
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
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
