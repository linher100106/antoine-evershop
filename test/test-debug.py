import os
import importlib
import inspect

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

from admin.test_login import TestLogin

# Variable globale pour spécifier une fonction précise à tester
FUNCTION_TO_TEST = "test_login"  # Met le nom de la fonction ici pour tester (ex: "test_click_on_product")


def get_test_classes_from_module(module):
    """Récupère toutes les classes de test dans un module."""
    return [member for name, member in inspect.getmembers(module) if
            inspect.isclass(member) and name.startswith('Test')]


def get_all_test_modules(directory):
    """Récupère tous les modules de test dans un répertoire donné."""
    test_modules = []
    for file in os.listdir(directory):
        if file.startswith("test_") and file.endswith(".py"):
            module_name = file[:-3]  # Enlève l'extension .py
            module = importlib.import_module(module_name)
            test_modules.append(module)
    return test_modules


def execute_test(driver, test_class_instance, method):
    """Exécute un test donné."""
    print(f"Running {method} from {test_class_instance.__class__.__name__}")
    getattr(test_class_instance, method)(driver)


def run_tests_in_dependency_order(test_classes, driver):
    """Exécute tous les tests en prenant en compte les dépendances."""
    executed_tests = set()

    # Fonction pour exécuter récursivement les tests dépendants
    def execute_dependent_tests(test_class_instance):
        test_methods = [method for method in dir(test_class_instance) if method.startswith('test_')]

        for method in test_methods:
            if method in executed_tests:
                continue  # Skip si déjà exécuté

            if FUNCTION_TO_TEST and method != FUNCTION_TO_TEST:
                continue  # Si on est en mode debug et on a spécifié une fonction, on exécute seulement celle-ci

            # Exécute le test
            execute_test(driver, TestLogin(), "test_successful_login")
            executed_tests.add("test_successful_login")

    # for test_class in test_classes:
    #     test_class_instance = test_class()

        # Exécute les tests dans la classe
        execute_dependent_tests(TestLogin())


if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-search-engine-choice-screen")
    # options.add_argument("--headless")  # Peut être activé si tu ne veux pas voir le navigateur
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--remote-debugging-port=9222")

    driver = webdriver.Chrome(options=options)

    try:
        # Détection automatique des modules de test dans le répertoire actuel
        #test_modules = get_all_test_modules("admin")
        test_modules = ["test_login"]

        # Collecte de toutes les classes de tests dans les modules
        test_classes = []
        for module in test_modules:
            test_classes.extend(get_test_classes_from_module(module))

        # Exécute les tests avec les dépendances
        run_tests_in_dependency_order(["TestLogin"], driver)
    finally:
        driver.quit()