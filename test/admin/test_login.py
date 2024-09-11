import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLogin:
    def test_successful_login(self, driver):
        # Accéder à la page d'administration du site
        driver.get("http://localhost:3000/admin")

        # Cibler les champs du formulaire de connexion et le bouton submit
        email_input = driver.find_element(By.NAME, "email")
        password_input = driver.find_element(By.NAME, "password")
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

        # Se connecter
        email_input.send_keys("a.nouvene@it-students.fr")
        time.sleep(1)
        password_input.send_keys("azerty82$")
        time.sleep(1)
        login_button.click()

        # Vérifier la connexion au dashbord
        WebDriverWait(driver, 10).until(EC.title_contains("Dashboard"))
        time.sleep(3)

        try:
            assert "Dashboard" in driver.title
        except Exception as e:
            print("Echec de connexion", e)




