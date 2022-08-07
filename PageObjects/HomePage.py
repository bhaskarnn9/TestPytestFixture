
class HomePage:

    def __init__(self, driver):
        self.driver = driver

    get_started_text_xpath = "(//button[contains(text(), 'Get started')])[1]"

    def verify_get_started_text(self):
        self.driver.find_element_by_xpath(self.get_started_text_xpath)
