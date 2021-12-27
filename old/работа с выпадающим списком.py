from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = int(browser.find_element(By.ID, "num1").text)
    y = int(browser.find_element(By.ID, "num2").text)
    summ = x + y
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(summ))
    submit = browser.find_element(By.CLASS_NAME, "btn")
    submit.click()



finally:
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()