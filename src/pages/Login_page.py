# this page is just for myself ;)

class Login():
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)

    def login(self, data):
        email = self.driver.find_element_by_id("identifierId")
        email.send_keys(data['email'])
        next_button = self.driver.find_element_by_xpath("//*[text()='Далее']")
        next_button.click()
        psswd = self.driver.find_element_by_name("password")
        psswd.send_keys(data['password'])
        one_more_next_button = self.driver.find_element_by_xpath("//*[@id='passwordNext']")
        one_more_next_button.click()
