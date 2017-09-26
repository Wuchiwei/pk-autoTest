# -*- coding: utf-8 -*-
"""
Simple iOS tests, showing accessing elements and getting/setting text from them.
"""
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
        setup.setUp2(self)
        setup.ck_login(self)
        element.livehome_element(self)

    def test_page_ch_case1(self):  #頁面切換

        self.assertEqual(u'PK直播', self.pk_title.get_attribute(u'name'))
        self.game.click()
        sleep(1)
        self.game_title = self.driver.find_element_by_accessibility_id('遊戲大廳')
        self.assertEqual(u'遊戲大廳', self.game_title.get_attribute(u'name'))
        self.live.click()
        sleep(1)
        self.next_message = self.driver.find_element_by_accessibility_id('下次再說囉！')
        self.next_message.click()
        sleep(1)
        self.info.click()
        sleep(1)
        self.icon_diamond = self.driver.find_element_by_accessibility_id('icon diamond')
        self.assertEqual('icon diamond', self.icon_diamond.get_attribute('name'))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
