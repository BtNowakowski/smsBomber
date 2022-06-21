from selenium import webdriver
from selenium.webdriver.common.by import By

x = 3
for i in range(x):
    driver = webdriver.Chrome()
    driver.get('https://www.amazon.pl/')
    driver.find_element(by=By.CSS_SELECTOR, value='a[data-nav-role="signin"]').click()
    driver.find_element(by=By.CSS_SELECTOR, value='a[data-csa-c-func-deps="aui-da-a-expander-toggle"]').click()
    driver.find_element(by=By.ID, value='auth-fpp-link-bottom').click()
    input_1 = driver.find_element(by=By.ID, value='ap_email')
    input_1.click()
    input_1.send_keys('123456789')
    driver.find_element(by=By.ID, value='continue').click()
    driver.quit()
