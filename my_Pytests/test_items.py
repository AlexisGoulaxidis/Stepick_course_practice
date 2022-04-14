import pytest

link = "http://selenium1py.pythonanywhere.com/"

@pytest.mark.xfail
def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")

@pytest.mark.xfail(reason="problem here!")
@pytest.mark.parametrize('language', ["ru", "en-gb"])
def test_guest_should_see_login_link(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")
    
@pytest.mark.xfail(reason="problem here!")    
def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#magic_link")
