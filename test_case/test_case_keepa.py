# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("https://keepa.com/#!product/5-B0B5SDFLTB")
        time.sleep(2)
        driver.find_element_by_id("tabTrack").click()
        driver.find_element_by_id("csvtype-5-18-threshold").click()
        driver.find_element_by_xpath("//div[@id='tracking__panel--5']/section/div/div/div/div[2]/div/table/tbody/tr[5]/td").click()
        driver.find_element_by_id("csvtype-5-0-threshold").click()
        driver.find_element_by_xpath("//div[@id='tracking__panel--5']/section[2]/div/div/div/div[2]/div/table/tbody/tr[4]/td").click()
        driver.find_element_by_id("submitTracking").click()
        #ERROR: Caught exception [unknown command []]
        #ERROR: Caught exception [unknown command []]
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
