import time


class CreateAccount():
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)

    def fill_data(self, data):
        first_name_field = self.driver.find_element_by_id("firstName")
        last_name_field = self.driver.find_element_by_id("lastName")
        password_field = self.driver.find_element_by_name("Passwd")
        confirm_password_field = self.driver.find_element_by_name("ConfirmPasswd")
        self.username_field = self.driver.find_element_by_id("username")
        first_name_field.send_keys(data['f_name'])
        last_name_field.send_keys(data['l_name'])
        password_field.send_keys(data['password'])
        confirm_password_field.send_keys(data['password'])

    def validate_username_field(self, email, validation_error):
        if self.username_field:
            self.username_field.clear()
            self.username_field.send_keys(email)
            next_button = self.driver.find_element_by_id("accountDetailsNext")
            next_button.click()
            time.sleep(1)
            assert validation_error in self.driver.page_source
            time.sleep(1)
