from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    #time.sleep(2)
    browser.execute_script("document.getElementsByTagName('button')[0].classList.remove('trollface');")
    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)
    submit = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    submit.click()


finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()