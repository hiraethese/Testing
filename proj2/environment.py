from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time

base_url = "http://opencart:8080/"
wait_time = 1

def get_driver():
    '''Get Chrome/Firefox driver from Selenium Hub'''
    chrome_options = ChromeOptions()
    firefox_options = FirefoxOptions()

    try:
        driver = webdriver.Remote(
                command_executor='http://localhost:4444/wd/hub',
                options=chrome_options)
    except WebDriverException:
        driver = webdriver.Remote(
                command_executor='http://localhost:4444/wd/hub',
                options=firefox_options)

    driver.implicitly_wait(wait_time)
    return driver

def before_all(context):
    time.sleep(1)
    context.driver = get_driver()
    context.base_url = base_url

def after_all(context):
    context.driver.quit()
