#this is config file for pytest fixtures to remember automaticaly in all tests in this directory

import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
#from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.opera import OperaDriverManager
from selenium.webdriver.chrome.options import Options

#link for WebDriverManager guide https://github.com/SergeyPirogov/webdriver_manager

def pytest_addoption(parser):  #make command for selectd file (name of test)
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: opera or firefox", choices=('opera', 'firefox'))
    parser.addoption('--language', action='store', default='en', help='Choose language')
    
                     

@pytest.fixture #(scope="function") if wanna target on function/class/method
def browser(request):

	browser_name = request.config.getoption("browser_name")  # Request get param from CMD
	user_language = request.config.getoption("language") # Request get Language value from CMD
	#assert language == 'ru' or 'fr' or 'en-gb', '  '#raise pytest.UsageError(f'--language {language} is not correct! Try "ru", "fr", "en-gb"')
	#starting
	browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
	print('\n Start Browser for test')
	if browser_name == 'firefox':
		print('\n Starting Firefox')
		browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
		fp = webdriver.FirefoxProfile()
		fp.set_preference("intl.accept_languages", user_language)
		browser = webdriver.Firefox(firefox_profile=fp)
		browser.get('https://google.com')
		#Create Pref Options for language in browser in param accept_languages
		
	elif browser_name == 'opera':
		print('\n Starting Opera')
		browser = webdriver.Opera(executable_path=OperaDriverManager().install())
		options = Options()
		options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
		browser = webdriver.Opera(options=options)
		browser.get('https://google.com')
		#Create Pref Options for language in browser in param accept_languages
	else:
		raise pytest.UsageError("--browser_name should be opera or firefox")
		
	
	#pytest -s -v --browser_name=" " --language=" "  test.py  / the way to change browser/language when testing, but browser needs to be installed
	
	
	yield browser #last step of fixture
	print('\n Quit browser..')
	browser.quit()
