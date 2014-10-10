#coding: utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import unittest,time,re,sys
reload(sys)
sys.setdefaultencoding('utf-8')

class test(unittest.TestCase):

	att = {}


	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(30)
		self.base_url = "http://bj.meituan.com"
		self.verificationErrors = []
		self.accept_next_alert = True

	def test_1(self):
		driver = self.driver
		driver.get(self.base_url)
		driver.find_element_by_xpath("//a[text()='登录']").click()
		driver.find_element_by_xpath("//input[@id='login-email']").send_keys("18021093592")
		driver.find_element_by_xpath("//input[@id='login-password']").send_keys("1234567")
		driver.find_element_by_xpath("//input[@value='登录']").click()
		try:
			element = WebDriverWait(driver,10).until(EC.title_contains("北京团购大全"))
			print(driver.title)
			att = driver.get_cookies()
			print(att)
		except:
			print("登录失败")
		driver.quit()


if __name__ == "__main__":
	unittest.main()
