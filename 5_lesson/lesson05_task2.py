from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def click_blue_button():
    driver = None
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        driver.get("http://uitestingplayground.com/dynamicid")

        button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
        button.click()
        print("✅ Успешный клик!")

    except Exception as e:
        print(f"❌ Ошибка: {e}")
    finally:
        if driver:
            driver.quit()


if __name__ == "__main__":
    for _ in range(3):
        click_blue_button()
        input("Нажмите Enter для следующего запуска...")