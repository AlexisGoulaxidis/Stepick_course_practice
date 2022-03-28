from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select  #for select elements / select_by_value
from selenium.webdriver.support.ui import WebDriverWait  #check time for waiting elements visability
from selenium.webdriver.support import expected_conditions as EC # .element_to_be_clickable((By.ID, ""))
from time import sleep as sleep
import unittest


browser = webdriver.Firefox()
browser.implicitly_wait(5)  #method for waiting assinc element loading from server (auto time sleep)


class test_first(unittest.TestCase):
	def test_required(self):
		link = "http://suninjuly.github.io/registration1.html"
		browser.get(link)
		req_elem = browser.find_elements_by_xpath('//input[@required]')
		elems = [i.send_keys('AnyText') for i in req_elem]
		button = browser.find_element_by_xpath('//button[@type="submit"]').click()
		welcome_text = browser.find_element_by_tag_name('h1').text
		self.assertEqual("Congratulations! You have successfully registered!", welcome_text, f'Congratulations Error! H1 Text is {welcome_text}')
	def test_required2(self):
		sleep(5)
		link = "http://suninjuly.github.io/registration2.html"
		browser.get(link)
		req_elem = browser.find_element_by_xpath('//input[contains(@class, "first") and @required]').send_keys('AnyText')
		req_elem2 = browser.find_element_by_xpath('//input[contains(@class, "second") and @required]').send_keys('AnyText')
		req_elem3 = browser.find_element_by_xpath('//input[contains(@class, "third") and @required]').send_keys('AnyText')
		button = browser.find_element_by_xpath('//button[@type="submit"]')
		welcome_text = browser.find_element_by_tag_name('h1').text
		self.assertEqual("Congratulations! You have successfully registered!", welcome_text, f'Congratulations Error! H1 Text is {welcome_text}')

if __name__ == "__main__":
	try:
		unittest.main()
		sleep(8)
	finally:
		browser.quit()