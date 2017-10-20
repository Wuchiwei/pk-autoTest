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

    def test_latst_game_ordinary_overage_case(self):
        element.livehome_element(self)
        self.game.click()
        sleep(2)
        element.livehome_game(self)
        self.driver.swipe(190,570,0,-400)
        self.driver.tap([(57, 480)])
        sleep(1)
        element.livehome_game_popular(self)
        function_game.game_ordinary_overage(self)
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
