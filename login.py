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

	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(30)
		self.base_url = "http://bj.meituan.com"
		self.verificationErrors = []
		self.accept_next_alert = True

	def test_1(self):
		print("-------test_1---------------")
		driver = self.driver
		driver.get(self.base_url)
		driver.find_element_by_xpath("//a[text()='登录']").click()
		driver.find_element_by_xpath("//input[@id='login-email']").send_keys("18021093592")
		driver.find_element_by_xpath("//input[@id='login-password']").send_keys("1234567")
		driver.find_element_by_xpath("//input[@value='登录']").click()
		try:
			element = WebDriverWait(driver,10).until(EC.title_contains("北京团购大全"))
			print(driver.current_url)
			return driver.current_url
		except:
			print("登录失败")
			return 0
		driver.quit()


	def test_2(self):
		print("--------test_2------------")
		driver = self.driver
		url = self.test_1()
		driver.get(url)
		driver.find_element_by_xpath("//a[text()='酒店']").click()
		driver.find_element_by_link_text("可看房态").click()
		driver.find_element_by_xpath("//img[@src ='http://p0.meituan.net/320.0.a/deal/__21204622__5612580.jpg']").click()


if __name__ == "__main__":
	unittest.main()