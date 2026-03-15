from selenium import webdriver

def test_page_load(url):

    driver = webdriver.Chrome()

    driver.get(url)

    assert driver.title != ""

    driver.quit()