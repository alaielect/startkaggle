from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def run_kaggle():
    print("⏳ Starting Kaggle notebook...")
    options = Options()
    options.add_argument('--headless')  # بدون نمایش مرورگر
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://www.kaggle.com/code/alaielect/notebook8f0ddb0d68")
        wait = WebDriverWait(driver, 30)
        
        # منتظر دکمه Run
        run_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Run')]")))
        run_button.click()
        print("✅ Clicked on Run button!")
        
        # منتظر اجرا
        time.sleep(30)
        print("✅ Notebook is running!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    run_kaggle()
