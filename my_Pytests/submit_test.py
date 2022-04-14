from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select  #for select elements / select_by_value
from selenium.webdriver.support.ui import WebDriverWait  #check time for waiting elements visability
from selenium.webdriver.support import expected_conditions as EC # .element_to_be_clickable((By.ID, ""))
from selenium.webdriver.common.keys import Keys #keyboard keys
from time import sleep as sleep
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

browser = webdriver.Firefox()
browser.implicitly_wait(5)  #method for waiting assinc element loading from server (auto time sleep)
browser.get(link)

	
try:
	#find button and send math formule from form variables
	
	button = browser.find_element_by_css_selector('button.btn').click()
	x = int(browser.find_element_by_xpath('//span[@id="input_value"]').text)
	x = str(math.log(abs(12*math.sin(x))))
	ans = browser.find_element_by_xpath("//input[@id='answer']").send_keys(x)
	btn = browser.find_element(By.ID, "solve").click()

		
finally:
	print("♂ "*15)
	sleep(6)
	browser.quit()
	
	
	
def test_cycle_submit():
	#words = ("" , #words)
	elements = browser.find_elements_by_css_selector('input[type="text"]')
	for element in elements:
		element.send_keys('something')
		sleep(0.1)
	button = browser.find_element_by_css_selector("button.btn")
	button.click()
	print('Done, my master!')
	

def test_submit_target():
	
	form_name = browser.find_element_by_name('first_name')
	form_name.send_keys('Ivan')
	form_lastname = browser.find_element_by_name('last_name')
	form_lastname.send_keys("Petrov")
	
	button = browser.find_element_by_css_selector('button.btn')
	button.click()
	print('My work is done, master!')
	
def test_check_input_result():
	words = browser.find_elements_by_css_selector('input[required]') #input*
	for element in words:
		element.send_keys('key')
	sleep(3)
	words2 = browser.find_elements(By.XPATH, '//input[not(@required)]') #not required
	for i in words2:
		i.send_keys('jk')
	sleep(2)
	button = browser.find_element(By.XPATH, "//button[@type='submit']")
	button.click()
	welcome_text = browser.find_element_by_tag_name('h1') #check text after submit
	welcome_text = welcome_text.text
	assert "Congratulations! You have successfully registered!" == welcome_text

def test_get_attribute():
	browser.find_element_by_xpath("//img").get_attribute("attribute")  
	
def test_element_focus_fix():  #when is no clickable element bcs another element obscures it
	button = browser.find_element_by_tag_name("button")
	browser.execute_script("return arguments[0].scrollIntoView(true);", button)
	browser.execute_script("window.scrollBy(0, 100);") #scroll by 100 pixels bottom 
	#execute_script = use js
	button.click()
	
def test_send_file():
	import os
	current_dir = os.path.abspath(os.path.dirname(__file__))  #dirname of this location
	print(os.path.abspath(__file__))
	
	file_path = os.path.join(current_dir, 'file.txt')  #what file to send
	print(os.path.abspath(os.path.dirname(__file__)))
	w_path.send_keys(file_path) #send to input(file) element this file


def test_work_in_new_window():
	browser.switch_to.window(window_name) #switch to continue work
	new_window = browser.window_handles[1] #second tab in browser or [0] - first
	
def test_alert_access():
	alert = browser.switch_to.alert #select alert()
	alert.accept() #accepting the alert
	alert.text #get text from alert
	#if alert has 2 variables (confirm or dismiss), use accept() or dismiss()
	#if alert has prompt (text input), use send_keys()
	
def test_waiting_for_clickable_and_wait_for_text():
	button = WebDriverWait(browser, 5).until(
	EC.element_to_be_clickable((By.ID, "verify"))  #waiting to be clickable button
	) #other check methods in SHPARGALKA
	button.click()
	
	price = WebDriverWait(browser, 20, 2).until(   #wait
	EC.text_to_be_present_in_element((By.ID, "price"), '$100') #text in element
	)
	
	