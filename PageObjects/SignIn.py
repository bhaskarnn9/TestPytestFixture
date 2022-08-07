class SignIn:

    def __init__(self, driver):
        self.driver = driver

    button_get_started_xpath = "//span[contains(text(), 'Sign in')]//ancestor::div[contains(@class, " \
                               "'NavBarRight')]//button[text()='Get started'] "

    text_get_started_xpath = "//h2[contains(text(), 'Let’s get you started')]"

    def click_button_get_started(self):
        assert self.driver.find_element_by_xpath(self.button_get_started_xpath)
        self.driver.find_element_by_xpath(self.button_get_started_xpath).click()

    def verify_text_get_started(self):
        self.driver.find_element_by_xpath(self.text_get_started_xpath)
