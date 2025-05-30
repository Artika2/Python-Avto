from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_blue_button():
    driver = webdriver.Chrome()

    try:
        driver.get("http://uitestingplayground.com/classattr")

        blue_button = driver.find_element(By.XPATH, "//button[contains(concat(' ', @class, ' '), ' btn-primary ')]")
        blue_button.click()


        time.sleep(1)
        alert = driver.switch_to.alert
        alert.accept()

        print("Скрипт выполнен успешно")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        driver.quit()


if __name__ == "__main__":
    for _ in range(3):
        test_blue_button()
        input("Нажмите Enter для следующего запуска...")