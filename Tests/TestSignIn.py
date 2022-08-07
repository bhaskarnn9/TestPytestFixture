from PageObjects.SignIn import SignIn


class TestSignIn:

    def test_sign_in(self, driver):

        url = 'https://www.gemini.com/'
        driver.get(url)

        si = SignIn(driver)
        si.click_button_get_started()
        si.verify_text_get_started()
