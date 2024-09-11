import pytest
import selenium
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_login import TestLogin

class TestProducts(TestLogin):
    def test_click_on_product(self, driver):
        try:
            # Wait for and click on the Catalog menu item
            catalog_menu = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//span[text()='Catalog']"))
            )
            catalog_menu.click()

            # Wait for and click on the Products menu item
            products_menu = WebDriverWait(driver, 15).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//a[contains(@href, '/admin/products') and contains(., 'Products')]"))
            )
            products_menu.click()

            # Wait for the Products page heading to appear and verify its visibility
            page_heading = WebDriverWait(driver, 15).until(
                EC.visibility_of_element_located((By.XPATH, "//h1[text()='Products']"))
            )
            assert page_heading.is_displayed(), "Products page did not load correctly"

        except TimeoutException as e:
            print(f"TimeoutException encountered: {e}")
            driver.save_screenshot('screenshot.png')  # Save a screenshot for further debugging
            raise