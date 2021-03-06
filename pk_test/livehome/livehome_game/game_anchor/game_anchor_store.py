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
        setup.ck_login_anchor(self)
        sleep(1)

    def test_game_anchor_store_case(self):
        element.livehome_element(self)
        self.game.click()
        sleep(1)
        element.livehome_game(self)
        self.driver.tap([(140, 535)])#self.livehome_game_popular.click()
        sleep(1)
        element.livehome_game_popular(self)
        self.livehome_game_popula_store.click()
        sleep(1)
        self.driver.find_element_by_accessibility_id('主播規範')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
