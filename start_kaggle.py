# ============================================
# start_kaggle.py - روشن کردن کاگل با Selenium
# ============================================
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

def start_kaggle():
    print("🚀 راه‌اندازی مرورگر...")
    
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    driver = webdriver.Chrome(options=options)
    
    try:
        print("🔓 رفتن به نوت‌بوک...")
        driver.get("https://www.kaggle.com/code/alaielect/notebook8f0ddb0d68")
        wait = WebDriverWait(driver, 30)
        
        # پیدا کردن دکمه Save Version
        print("🔘 دنبال دکمه Save Version...")
        save_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(), 'Save Version')]")
        ))
        save_btn.click()
        print("✅ Save Version کلیک شد!")
        time.sleep(2)
        
        # انتخاب Save & Run All
        print("🔘 انتخاب Save & Run All...")
        run_all = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//input[@value='Save & Run All (Commit)']")
        ))
        run_all.click()
        print("✅ Save & Run All انتخاب شد!")
        time.sleep(1)
        
        # کلیک نهایی Save
        print("🔘 کلیک روی Save...")
        save_final = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(), 'Save')]")
        ))
        save_final.click()
        print("✅ Save کلیک شد!")
        
        time.sleep(5)
        print("🎉 کاگل با موفقیت روشن شد!")
        return True
        
    except Exception as e:
        print(f"❌ خطا: {e}")
        return False
    finally:
        driver.quit()

if __name__ == "__main__":
    start_kaggle()
