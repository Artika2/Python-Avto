from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


def login_test():
    driver = None
    try:
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

        driver.get("http://the-internet.herokuapp.com/login")

        # 3. Ввести логин
        username_field = driver.find_element(By.ID, "username")
        username_field.send_keys("tomsmith")

        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("SuperSecretPassword!")

        login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
        login_button.click()

        success_message = driver.find_element(By.ID, "flash").text
        print("Сообщение после входа:", success_message.split("\n")[0])

    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        if driver:
            driver.quit()
            print("Браузер закрыт")


if __name__ == "__main__":
    login_test()