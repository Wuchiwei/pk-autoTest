# -*- coding: utf-8 -*-

import unittest
import os
import sys
sys.path.append("../../../../import")
import setup
import element
from random import randint
from appium import webdriver
from time import sleep

class SimpleIOSTests(unittest.TestCase):

    def setUp(self):
        # set up appium
        setup.load_for4(self)
        setup.ck_login_ordinary(self)
        sleep(2)

    def test_game_ordinary_betting_short_case(self):
        element.livehome_element(self)
        self.game.click()
        sleep(1)
        element.livehome_game(self)
        self.driver.tap([(140, 535)])#self.livehome_game_popular.click()
        sleep(1)
        element.livehome_game_popular(self)
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

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
