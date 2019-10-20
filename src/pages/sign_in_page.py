import time


class SignIn():
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)

    def start_creating(self):
        create_account_button = self.driver.find_element_by_xpath("//*[text()='Создать аккаунт']")
        create_account_button.click()
        time.sleep(1)
        for_myself_button = self.driver.find_element_by_xpath("//*[text()='Для себя']")
        for_myself_button.click()