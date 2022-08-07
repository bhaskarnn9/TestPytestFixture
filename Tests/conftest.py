import pytest
from selenium import webdriver


@pytest.fixture(name='driver', scope='class', autouse=True)
def setup():
    driver = webdriver.Chrome(executable_path='/Users/bhaskarneel/Development/Selenium_Dependencies/chromedriver')
    driver.maximize_window()
    driver.implicitly_wait(3)
    yield driver
    driver.close()
