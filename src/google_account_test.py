from selenium import webdriver
from src.pages.create_account_page import CreateAccount
from src.pages.sign_in_page import SignIn

driver = webdriver.Chrome("F:/Python course/chromedriver.exe")
driver.get("https://accounts.google.com/")
driver.implicitly_wait(5)

validation_error = "Имя пользователя может включать латинские буквы (a-z), цифры (0-9) и точку (.)."
user_data = {'f_name': 'El', 'l_name': 'Ent', 'password': 'Ent123456!', 'email': 'pythonautomation19'}
email_list = {'@a.a', 'a@-a.a', 'a@a@a.a', 'a@a'}

sign_in_page = SignIn(driver)
sign_in_page.start_creating()

create_page = CreateAccount(driver)
create_page.fill_data(user_data)

for email in email_list:
    create_page.validate_username_field(email, validation_error)
