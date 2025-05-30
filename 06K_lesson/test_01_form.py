from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time


def test_form_validation():
    driver = None
    try:

        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        time.sleep(2) 

        driver.find_element(By.NAME, "first-name").send_keys("Иван")
        driver.find_element(By.NAME, "last-name").send_keys("Петров")
        driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
        driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
        driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
        # Zip code оставляем пустым
        driver.find_element(By.NAME, "city").send_keys("Москва")
        driver.find_element(By.NAME, "country").send_keys("Россия")
        driver.find_element(By.NAME, "job-position").send_keys("QA")
        driver.find_element(By.NAME, "company").send_keys("SkyPro")

        driver.find_element(By.CSS_SELECTOR, "button.btn.btn-outline-primary.mt-3").click()
        time.sleep(2)

        zip_code = driver.find_element(By.NAME, "zip-code")
        assert "is-invalid" in zip_code.get_attribute("class"), "Поле Zip code не подсвечено красным"

        valid_fields = [
            "first-name", "last-name", "address", "e-mail",
            "phone", "city", "country", "job-position", "company"
        ]

        for field in valid_fields:
            element = driver.find_element(By.NAME, field)
            assert "is-valid" in element.get_attribute("class"), f"Поле {field} не подсвечено зеленым"

        print("Все проверки пройдены успешно!")

    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        if driver:
            driver.quit()


if __name__ == "__main__":
    test_form_validation()