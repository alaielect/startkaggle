# ============================================
# main.py - روشن کردن کاگل با لاگ کامل
# ============================================
import requests
import os
import sys
import json

# ========== تنظیمات ==========
KAGGLE_USERNAME = "AlAiElect"
KAGGLE_KERNEL_SLUG = "notebook8f0ddb0d68"  # اسم نوت‌بوک رو چک کن
KAGGLE_API_TOKEN = "KGAT_261f60e51db1ac5bd7a612019ff8adbd"

def start_kaggle():
    print("⏳ در حال روشن کردن کاگل...")
    
    # آدرس درست API
    url = "https://www.kaggle.com/api/v1/kernels/run"
    
    headers = {
        "Authorization": f"Bearer {KAGGLE_API_TOKEN}",
        "Content-Type": "application/json"
    }
    
    data = {
        "kernel": f"{KAGGLE_USERNAME}/{KAGGLE_KERNEL_SLUG}",
        "args": ["سلام! این یک تست از راه دور است."]
    }
    
    print(f"📤 ارسال به: {url}")
    print(f"📤 داده: {json.dumps(data, indent=2)}")
    
    try:
        response = requests.post(url, json=data, headers=headers, timeout=60)
        print(f"📊 کد وضعیت: {response.status_code}")
        
        if response.status_code == 200:
            print("✅ کاگل با موفقیت روشن شد!")
            print(f"📝 پاسخ: {response.json()}")
        else:
            print(f"❌ خطا: {response.status_code}")
            print(f"📝 متن: {response.text[:500]}")
            
            # راهنمایی برای خطای ۴۰۴
            if response.status_code == 404:
                print("\n💡 راهنمایی:")
                print("1. اسم نوت‌بوک رو چک کن. توی لینک چیه؟")
                print("2. آیا نوت‌بوک عمومی (Public) هست؟")
                print("3. توکن API معتبر هست؟")
                
    except Exception as e:
        print(f"❌ خطا: {e}")

if __name__ == "__main__":
    print("🚀 شروع فرآیند...")
    start_kaggle()
