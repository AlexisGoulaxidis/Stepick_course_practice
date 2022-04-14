#this is config file for pytest fixtures to remember automaticaly in all tests in this directory

import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
#from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.opera import OperaDriverManager
from selenium.webdriver.chrome.options import Options

#link for webdriver guide https://github.com/SergeyPirogov/webdriver_manager

def pytest_addoption(parser):  #make command for selectd file (name of test)
    parser.addoption('--browser_name', action='store', default='opera',
                     help="Choose browser: opera or firefox", choices=('opera', 'firefox'))
                     

@pytest.fixture #scope="function" if wanna localize
def browser(request):

	browser_name = request.config.getoption("browser_name")  # Request get param from CMD
	print('\n Start Browser for test')
	if browser_name == 'firefox':
		print('\n Starting Firefox')
		browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
		fp = webdriver.FirefoxProfile()
		p.set_preference("intl.accept_languages", user_language)
		browser = webdriver.Firefox(firefox_profile=fp)
		#Create Pref Options for language in browser in param accept_languages
		
	elif browser_name == 'opera':
		print('\n Starting Opera')
		browser = webdriver.Opera(executable_path=OperaDriverManager().install())
		options = Options()
		options.add_experimental_option('prefs', {'intl.accept_languages': user_language}) #Create Pref Options for language in browser in param accept_languages
		browser = webdriver.Opera(options=options)
	else:
		raise pytest.UsageError("--browser_name should be opera or firefox")
		
	#browser = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
	
	#pytest -s -v --browser_name=" " test.py  / the way to change browser when testing, but browser needs to be installed
	yield browser
	print('\n Quit browser..')
	browser.close()
	browser.quit()
