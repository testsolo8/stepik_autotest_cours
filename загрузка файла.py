from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    first = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    first.send_keys("max")
    last = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    last.send_keys("mit")
    email = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    email.send_keys("mail")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test.txt')
    file = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    file.send_keys(file_path)
    input4 = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    input4.click()

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()