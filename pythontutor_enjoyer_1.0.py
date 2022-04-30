from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select  #for select elements / select_by_value
from selenium.webdriver.support.ui import WebDriverWait  #check time for waiting elements visability
from selenium.webdriver.support import expected_conditions as EC # .element_to_be_clickable((By.ID, ""))
from selenium.webdriver.common.keys import Keys #keyboard keys
from selenium.webdriver.common.action_chains import ActionChains #for keyboard
from selenium.webdriver.firefox.options import Options
from time import sleep as sleep
from random import randint as rand
import re


prof = webdriver.FirefoxProfile(
  r'/home/kali/.mozilla/firefox/ir7gkide.TestProfile')
browser = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver', firefox_profile=prof)
browser.delete_all_cookies()

action = ActionChains(browser)

link = "https://pythontutor.ru/lessons/inout_and_arithmetic_operations/"

browser.get(link)
browser.implicitly_wait(3)
wait = WebDriverWait(browser,10)


def login_mode():
	if browser.find_element(By.XPATH, "//a[contains(@href, '/accounts/login/')]"):
		def what_to_do():
			sol = input('Дружище, ты не зашёл в аккаунт \n Введи "Y" если хочешь чтобы я создал тебе случайный аккаунт \n Либо "N" и я подожду пока войдёшь в аккаунт.\n')
			assert sol == 'Y' or 'N' or 'y' or 'n', "Либо Y либо N, я всё вижу!"
			if re.match('[Yy]', sol):
				print('Little Wait...')
				browser.find_element(By.XPATH, "//a[contains(@href, '/accounts/register/')]").click()
				sleep(1)
				elems = browser.find_elements(By.XPATH,('//input[@type="text"]'))
				for inputs in elems:
					inputs.send_keys('Randy', rand(1,9999), 'Text')
					if inputs.get_attribute('name') == 'email':
						inputs.send_keys('Randy', rand(1,999), 'Text' + '@gmail.com')
					elif browser.find_elements(By.XPATH,('//input[@type="password"]')):
						browser.execute_script(f'''document.getElementById("password").setAttribute('value', 'imjustrandypleasedonttouchme!' );''')
						browser.execute_script(f'''document.getElementById("confirm_password").setAttribute('value', 'imjustrandypleasedonttouchme!' );''')
					
				browser.find_element(By.XPATH, '//button[@type="submit"]').click()
				print('All is Done! \nNow select range!')
			elif re.match('[Nn]', sol):
				print('OK, LOGIN...')
			else:
				print('Something wrong, try again')
				browser.close()
		what_to_do()
login_mode()







#starting input
start_num , end_num = int(input('1. Input when i will start using numbers 1-11: ')), int(input('2. Input when i will finish using numbers 2-11: '))
assert 2 <= end_num <= 11, 'Must be between 2 and 11'

browser.get(link)
#very big cycle :D

try:
	
	while start_num < end_num+1:
		title_xpath = f"//div[@class='lesson__item_id'][text()='{start_num}.']/ancestor::a[1]"
		title_href = browser.find_element(By.XPATH, title_xpath).get_attribute('href')
		print('FULL IS', title_href)
		
		browser.get(title_href) #going to link of [i]
		
		title_href_short = title_href[title_href.find('lessons'):]
		
		lesson = f"//a[contains(@href, '{title_href_short}problems')]"
		
		#len of lessons for new cycle
		lesson_len = len(list(browser.find_elements(By.XPATH, lesson)))
		try:
			lesson_procent += lesson_len
		except:
			lesson_procent = 1
		print('\n LESSON LEN IS', lesson_len, '\n')
		print('Short is', title_href_short)
		for i in range(1, lesson_len+1):
			#if i >= lesson_len:
				#break
			try:
				if (browser.find_element(By.XPATH,  lesson + f'/ancestor::li[@class="solved"]/ancestor::ul[1]/li[position()="{i}"]')) is True:
					j+=1  #try J
					continue
			except:
				print('No Solved Elements')
			finally:
				print('\ni is ', i)
				lesson = f"//a[contains(@href, '{title_href_short}problems')]/ancestor::ul[1]/li[position()='{i}']"
				lessons = list(browser.find_elements(By.XPATH, lesson))
				lessons_len = len(lessons)
				print(f'> We have {lessons_len} here! <')
				for j in range(lessons_len):
					print('\nJ NUMBER IS\n', j)
					try:
						
						lessons[j].click()
						problem_text = browser.find_element(By.XPATH,'//h3[@class="problem_name"]').text
						browser.execute_script("window.open('https://google.com');")#new window
						window_first = browser.window_handles[1]
						browser.switch_to.window(window_first)
						#now we go to google our problems and solve the answers
						#browser.get('https://google.com')
						wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@name="q"]')))
						google_input = browser.find_element_by_xpath('//*[@name="q"]')
						google_input.send_keys(problem_text, ' pyanswer', Keys.ENTER) #browser.find_element(By.XPATH, '//input[@class and @type="text"]').send_keys(problem_text ' pyanswer').send_keys(Keys.ENTER)
						sleep(1)
						try:
							problem_text_element = problem_text.split()
							if ('Часы - 2' in problem_text_element) or ('Частотный' in problem_text_element):
								problem_text_element = 'CLOCK - 2 NOT WORKS'
							else:
								problem_text_element = problem_text_element[1]  #first text of problem name for check
							
							browser.find_element(By.XPATH, f'//div//cite[contains(text(), "https://pyanswer.site")]/ancestor::div[2]//h3[contains(text(),"Задача {problem_text_element}")][1]')
							wait.until(EC.visibility_of_element_located((By.XPATH, '//div//cite[contains(text(), "https://pyanswer.site")]')))
							browser.find_element(By.XPATH, f'//div//cite[contains(text(), "https://pyanswer.site")]').click()
							wait.until(EC.visibility_of_element_located((By.XPATH, f'//span[text()="Copy to Clipboard"][1]')))
							
							if 'Количество нулей' or 'Улитка' or 'Родословная' in problem_text_element:
								Clipboard = browser.find_element(By.XPATH, f"//span[text()='Copy to Clipboard'][contains(@data-id, 'fusion_syntax_highlighter_2')]")
								Clipboard.click()
							else:	
								Clipboard = browser.find_element(By.XPATH, f"//span[text()='Copy to Clipboard'][1]")
								Clipboard.click()
							browser.execute_script("arguments[0].scrollIntoView(true);", Clipboard)
						except:
							#print('\n IS NONE! \n')
							browser.get('https://google.com')
							google_input = browser.find_element_by_xpath('//*[@name="q"]')
							google_input.send_keys(problem_text, ' informatikaexpert', Keys.ENTER)
							#print('\n I PUT ENTER')
							wait.until(EC.visibility_of_element_located((By.XPATH, '//div//cite[contains(text(), "informatikaexpert.ru")]')))
							browser.find_element(By.XPATH, f'//div//cite[contains(text(), "informatikaexpert.ru")]').click()
							#print('\n I CLICK IT')
							wait.until(EC.visibility_of_element_located((By.XPATH, f'//div[@class="crayon-line crayon-striped-line"]')))
							#print('\n I WAITED IT')
							browser.execute_script("document.querySelector('.crayon-toolbar').setAttribute('style','font-size: 12px !important; height: 18px !important; line-height: 18px !important; margin-top: 0px; position: absolute; z-index: 2; display: flex;')")
							#print('\n I CHANGED STYLE JS')
							wait.until(EC.visibility_of_element_located((By.XPATH, f'//*[@class="crayon-button urvanov-syntax-highlighter-popup-button"]'))
							)
							browser.execute_script("document.querySelector('.urvanov-syntax-highlighter-popup-button').click()")
							new_window = browser.window_handles[2]
							browser.switch_to.window(new_window)
							browser.execute_script("document.querySelector('body').style.background='black'")
							new_block = browser.find_element_by_xpath('//body')
							new_block.send_keys(Keys.CONTROL + 'a')
							sleep(1)
							new_block.send_keys(Keys.CONTROL + 'c')
							#print('\n I COPY')
							browser.execute_script('window.close()')
							browser.switch_to.window(window_first)   #switch back
							
							#browser.find_element(By.XPATH, '//div[@title="Copy"]').click()
						#browser.find_element(By.XPATH, f'//span[text()="Copy to Clipboard"][1]').click()
						sleep(0.5)
						browser.execute_script("window.close();")
						window_zero = browser.window_handles[0]
						browser.switch_to.window(window_zero)
						CONTENT = browser.find_element(By.XPATH, f'//textarea[@class="ace_text-input"][1]')
						#//textarea[@class="ace_text-input"][1]
						#//div[contains(@class,'ace_layer ace_marker-layer')]/*
						#//div[@class="ace_content"]//*
						#//div[@class="ace_layer ace_text-layer"] TRY THIS FIRST
						#//div[@class="ace_layer ace_text-layer"]//span[@class="ace_identifier"]  #HERE ALL ELEMENTS
						#browser.execute_script("arguments[0].scrollIntoView();", CONTENT);
			#sleep(3) IF I WANNA TO SHOW
						#action.move_to_element_with_offset(CONTENT, 20, 30).click().perform()
						CONTENT.send_keys(Keys.CONTROL + 'a')
						CONTENT.send_keys(Keys.CONTROL + 'v')
						sleep(0.4)
						try:
							browser.execute_script("document.getElementByXPath('//button[@class='btn btn-primary btn-lg submit_solution__client-submit' and contains(text(),'Проверить')]').click();")
							#button_apply = browser.find_element(By.XPATH, '//button[@class="btn btn-primary btn-lg submit_solution__client-submit" and contains(text(),"Проверить")]').send_keys(Keys.RETURN)
						except:
							#detroy this nav bar!!!
							#button_apply = browser.find_element(By.XPATH, '//button[@class="btn btn-primary btn-lg submit_solution__client-submit" and contains(text(),"Проверить")]').send_keys(' ')
							button_apply = browser.find_element(By.XPATH, '//button[@class="btn btn-primary btn-lg submit_solution__client-submit"]')
							button_apply.click()
						#move to button
						try:
							
							browser.execute_script("arguments[0].scrollIntoView(true);", button_apply)
							sleep(1)
						except:
							print('\nI cant Scroll Into View :(')
						
						try:
							#wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="status_solved"]/b')))
							solve = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='other_solutions']")))
							try:
								success_value += 1
							except:
								success_value = 1
							print(f'\nSuccess value is ', success_value)
							#assert browser.find_element(By.XPATH, '//div[@class="status_solved"]/b').text == 'Правильное решение, поздравляем.' , f' !!! WE HAVE PROBLEM WITH {problem_text} !!!'
						except:
							browser.execute_script("document.getElementByXPath('//button[@class='btn btn-primary btn-lg submit_solution__client-submit' and contains(text(),'Проверить')]').click();")
							print('\nIm Trying To Solve Again!')
							print(f'\n PROBLEM {problem_text} IS NOT SOLVED OR NEEDS TIME')
						sleep(0.5)
					except: #AssertionError
						sleep(0.3)
						browser.execute_script("var xpath = '/html/body/div[3]'; var matchingElement = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue; matchingElement.remove();")
						print('\n I DESTROYED ACHIEVEMENT! \n')
						problem_start_position = browser.find_element(By.XPATH, '//h3[@class="lesson_name"]')
						browser.execute_script("arguments[0].scrollIntoView(true);", problem_start_position)
						#B_cookies = browser.get_cookies()
						#print('\n COOKIES \n' ,B_cookies)
						
						#PREVIUS METHODS
						
							#Ee_XPath = "//div[contains(@class, 'src-components-AchievementsModal-___AchievementsModal__container')]//span[text()='Еееее']/ancestor::div[1]"
							#wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, Ee_XPath)))
							#wait.until(EC.visibility_of_element_located((By.XPATH, Ee_XPath)))
							
							#try:
							#	Eeeee = browser.execute_script(f"document.getElementByXPath({Ee_XPath});")
							#	browser.execute_script("arguments[0].scrollIntoView(true);", Eeeee)
							#	java_find_ee = browser.execute_script(f"document.getElementByXPath({Ee_XPath});")
							#	wait.until(EC.element_to_be_clickable((java_find_ee)).click())
							#	print('I scrolled and clicked into Achivement!')
							#except:
							#	print('\nSorry, i cant scroll into Achivement \n')
							#browser.find_element(By.XPATH, '//span[text()="Еееее"]').click()
						
							
							#JS TO FIND THIS
						
							#var xpath = '//div[contains(@style, "position: fixed; height: 100%; width: 100%;")]';
#var xpath = '/html/body/div[3]'
#var matchingElement = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
#matchingElement.remove()
						
					#except:
					#	print('>>> ERROR IN__', j, '__ELEMENT <<<')
					finally:
						
						print(f'\n>>> LESSON {problem_text} IS COMPLETED <<<\n')
						print('\nI went to', i, j ,'and did something\n', sep="_")
				lesson_text = browser.find_element(By.XPATH, lesson).text
				
				print(f'The i ({i}) text of lesson is: __{lesson_text}__')
			
		start_num += 1 #end of first cycle
finally:
	try:
	
		success_procent = 100 - ((lesson_procent - success_value) * (lesson_procent * 0.01)) #value of success procent
		print('\n I FINISHED ',success_procent, '% LESSONS')
	except:
		print('I cant insert statistics')
	
	print(f'\nProgram done, master!')
	browser.quit()
		

def get_coordinates(ace_elem):
	el = ace_elem.get_location()
	el_x = el.getX()
	el_y = el.getY()
	return el_x, el_y
def do_coordinates(ace_elem, el_x, el_y):
	action.move_by_offset(el_x, el_y).click()
	action.key_down(Keys.DOWN)
	sleep(5)
	action.key_up(Keys.DOWN)


				
			
			
	
	
