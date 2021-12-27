import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

# answer = math.log(int(time.time()))

@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('test', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, test):
    answer = math.log(int(time.time()))
    link = f"https://stepik.org/lesson/{test}/step/1"
    browser.get(link)
    browser.implicitly_wait(7)
    answer2 = browser.find_element(By.CLASS_NAME, "ember-text-area")
    answer2.send_keys(answer)
    #time.sleep(1)
    key = browser.find_element(By.CLASS_NAME, "submit-submission")
    key.click()
    time.sleep(1)
    answer3 = browser.find_element(By.CLASS_NAME, "smart-hints__hint").text
    assert "Correct!" in answer3
