from PageObjects.SignIn import SignIn
from Utils.Utils import Utils
from selenium.common.exceptions import NoSuchElementException


class TestSignIn:

    def test_sign_in(self, driver):
        url = 'https://www.gemini.com/'
        driver.get(url)

        si = SignIn(driver)
        si.click_button_get_started()

        try:
            assert si.verify_text_get_started()
        except NoSuchElementException:
            print('\nEnter exception')
            Utils.take_screenshot(driver)
            assert False
