from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from test_login import TestLogin


def driverLocal():
    # Initialiser le navigateur
    chrome_options: Options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    chrome_options.add_argument("--disable-popup-blocking")
    service = Service(ChromeDriverManager(driver_version="128.0.6613.120").install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    return driver


login = TestLogin()
login.test_successful_login(driverLocal())
print("ok")
