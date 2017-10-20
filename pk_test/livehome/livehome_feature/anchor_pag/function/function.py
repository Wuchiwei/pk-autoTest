# -*- coding: utf-8 -*-
import unittest
import os
from random import randint
from appium import webdriver
from time import sleep

def follow(self):  #粉絲數量變化
        self.fans_value1 = self.driver.find_element_by_xpath('//XCUIElementTypeTable[1]/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[4]')
        sum = int(self.fans_value1.get_attribute('value')) + 1
        self.icon_follow = self.driver.find_element_by_accessibility_id('icon follow')
        self.icon_follow.click()
        self.icon_close = self.driver.find_element_by_accessibility_id('icon close')
        self.icon_close.click()
        self.driver.swipe(start_x=45, start_y=240, end_x=45, end_y=400, duration=800) #刷新
        sleep(2)
        self.driver.tap([(160, 280)])
        self.fans_value2 = self.driver.find_element_by_xpath('//XCUIElementTypeTable[1]/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[4]')
        self.assertEqual(int(sum), int(self.fans_value2.get_attribute('value')))

def nofollow(self):  #取消後，粉絲數量變化
        self.fans_value1 = self.driver.find_element_by_xpath('//XCUIElementTypeTable[1]/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[4]')
        sum = int(self.fans_value1.get_attribute('value')) - 1
        self.icon_follow = self.driver.find_element_by_accessibility_id('icon follow')
        self.icon_follow.click()
        self.icon_close = self.driver.find_element_by_accessibility_id('icon close')
        self.icon_close.click()
        self.driver.swipe(start_x=45, start_y=240, end_x=45, end_y=400, duration=800) #刷新
        sleep(2)
        self.driver.tap([(160, 280)])
        self.fans_value2 = self.driver.find_element_by_xpath('//XCUIElementTypeTable[1]/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[4]')
        self.assertEqual(int(sum), int(self.fans_value2.get_attribute('value')))


def imfollow(self):  #粉絲數量立即變化
        self.fans_value1 = self.driver.find_element_by_xpath('//XCUIElementTypeTable[1]/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[4]')
        sum = int(self.fans_value1.get_attribute('value')) + 1
        self.icon_follow = self.driver.find_element_by_accessibility_id('icon follow')
        self.icon_follow.click()
        sleep(1)
        self.fans_value2 = self.driver.find_element_by_xpath('//XCUIElementTypeTable[1]/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[4]')
        self.assertEqual(int(sum), int(self.fans_value2.get_attribute('value')))

def imnofollow(self):  #取消後，粉絲立即數量變化
        self.fans_value1 = self.driver.find_element_by_xpath('//XCUIElementTypeTable[1]/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[4]')
        sum = int(self.fans_value1.get_attribute('value')) - 1
        self.icon_follow = self.driver.find_element_by_accessibility_id('icon follow')
        self.icon_follow.click()
        sleep(1)
        self.fans_value2 = self.driver.find_element_by_xpath('//XCUIElementTypeTable[1]/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[4]')
        self.assertEqual(int(sum), int(self.fans_value2.get_attribute('value')))

def gift_diamond_enough(self): #鑽石足夠的時候送禮
        self.gift_butten = self.driver.find_element_by_accessibility_id('icon gift')
        self.gift_butten.click()
        sleep(1)
        self.diamond_value = self.driver.find_element_by_xpath('//XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[2]')
        self.diamond1 = int(  self.diamond_value.get_attribute('value').replace(',','')   )   - 200
        self.applause_gift_butten = self.driver.find_element_by_accessibility_id('Bear')
        self.applause_gift_butten.click()
        sleep(2)
        self.gift_butten.click()
        sleep(2)
        self.diamond2 = int(  self.diamond_value.get_attribute('value').replace(',','') )
        self.assertEqual(self.diamond1, self.diamond2)

def  gift_stroe_center(self):  #進入儲值程序
        self.gift_butten = self.driver.find_element_by_accessibility_id('icon gift')
        self.gift_butten.click()
        sleep(1)
        self.stroe_butten = self.driver.find_element_by_accessibility_id('儲值')
        self.stroe_butten.click()
        sleep(2)
        self.stroe_title = self.driver.find_element_by_accessibility_id('儲值中心')



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
