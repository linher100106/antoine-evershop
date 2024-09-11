from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from test_login_error import TestLoginError
from test_login import TestLogin
from test_products import TestProducts
from test_add_product import TestAddProduct


def driverLocal():
    # Initialiser le navigateur
    chrome_options: Options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--remote-debugging-port=9222")

    # service = Service(ChromeDriverManager(driver_version="128.0.6613.119").install())
    # driver = webdriver.Chrome(service=service, options=chrome_options)
    driver = webdriver.Chrome(options=chrome_options)

    return driver

# Connexion error
loginError = TestLoginError()
driver = driverLocal()
loginError.test_error_login(driver)
print("Login error passed")

# Connexion succès
login = TestLogin()
login.test_successful_login(driver)
print("Login passed")

# Liste de produits
product = TestProducts()
product.test_click_on_product(driver)
print("Product passed")

# Ajout d'un nouveau produit
addproduct = TestAddProduct()
addproduct.test_add_new_product(driver)
print("Add product passed")



