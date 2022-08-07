import time
from PageObjects.HomePage import HomePage


class TestHomePage:

    def test_home_page(self, driver):

        url = 'https://www.gemini.com/'
        driver.get(url)

        hp = HomePage(driver)
        hp.verify_get_started_text()

    def test_launch_stack_overflow(self, driver):

        url = 'https://stackoverflow.com/'
        driver.get(url)
        time.sleep(2)

        assert driver.current_url == url


class TestHome:

    def test_home_page(self, driver):

        url = 'https://www.gemini.com/'
        driver.get(url)

        hp = HomePage(driver)
        hp.verify_get_started_text()

    def test_launch_stack_overflow(self, driver):

        url = 'https://stackoverflow.com/'
        driver.get(url)
        time.sleep(2)

        assert driver.current_url == url
