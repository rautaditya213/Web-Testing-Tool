from selenium import webdriver

def test_page_load(url):

    driver = webdriver.Chrome()

    driver.get(url)

    # Check that page title exists
    assert driver.title != ""

    driver.quit()