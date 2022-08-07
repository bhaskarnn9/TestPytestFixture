import pytest
from selenium import webdriver


@pytest.fixture(name='driver', scope='session', autouse=True)
def setup():
    driver = webdriver.Chrome(
        executable_path='/Users/bhaskarneel/Development/Selenium_Dependencies/chromedriver')
    driver.maximize_window()
    driver.implicitly_wait(2)
    yield driver
    driver.close()
