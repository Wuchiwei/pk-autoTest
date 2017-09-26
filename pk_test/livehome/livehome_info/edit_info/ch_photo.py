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



import platform
import tempfile
import shutil

from PIL import Image
PATH = lambda p: os.path.abspath(p)
TEMP_FILE = PATH(tempfile.gettempdir() + "/temp_screen.png")


class SimpleIOSTests(unittest.TestCase):

    def setUp(self):
        # set up appium
        setup.setUp2(self)
        setup.ck_login(self)
        sleep(1)
        element.livehome_element(self)
        self.info.click()
        sleep(1)
        self.driver.get_screenshot_as_file(TEMP_FILE)
        self.a1 = Image(TEMP_FILE)
    def test_ch_photo(self):
        element.livehome_info(self)
        self.profile_edit_butten.click()
        sleep(1)
        element.edit_info(self)
        self.ch_photo.click()
        sleep(1)
        self.driver.find_element_by_xpath('//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView[1]/XCUIElementTypeCell[1]/XCUIElementTypeImage[1]').click()
        sleep(1)
        self.driver.find_element_by_accessibility_id('Choose').click()
        sleep(1)
        self.set_butten.click()
        sleep(2)
        self.driver.get_screenshot_as_file(TEMP_FILE)
        self.a2 = Image(TEMP_FILE)
        self.assertTrue(self.a1,self.a2)
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
