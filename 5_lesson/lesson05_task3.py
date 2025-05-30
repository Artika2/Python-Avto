from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


def input_text_test():
    driver = None
    try:
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

        driver.get("http://the-internet.herokuapp.com/inputs")


        input_field = driver.find_element(By.TAG_NAME, "input")

        input_field.send_keys("Sky")
        print("✅ Введён текст 'Sky'")

        input_field.clear()
        print("✅ Поле очищено")

        input_field.send_keys("Pro")
        print("✅ Введён текст 'Pro'")

    except Exception as e:
        print(f"❌ Ошибка: {e}")
    finally:
        if driver:
            driver.quit()
            print("✅ Браузер закрыт")


if __name__ == "__main__":
    input_text_test()