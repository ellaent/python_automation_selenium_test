from selenium import webdriver

driver = webdriver.Chrome("F:/Python course/chromedriver.exe")
driver.get("https://www.wikipedia.org/")

search_field = driver.find_element_by_id("searchInput")
search_button = driver.find_element_by_xpath("//form[@id='search-form']/fieldset/button")

search_field.send_keys("Test Automation")
search_button.click()

assert "Test Automation" in driver.title
assert "Test 2 Automation" in driver.title

driver.quit()
