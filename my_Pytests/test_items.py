import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  #check time for waiting elements visability
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


#@pytest.mark.parametrize('language', ["ru", "en-gb"])  -  If wanna test all list of languages as cycle
@pytest.mark.xfail(reason="problem here!")
@pytest.mark.smoke
def test_basket_button(browser):
	wait = WebDriverWait(browser,10)
	print('HI')
	browser.get(link)
	wait.until(EC.visability_of_element_available((By.XPATH, '//button[@class="btn btn-lg btn-primary btn-add-to-basket"]')))
	sleep(30)
	
