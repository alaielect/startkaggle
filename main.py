import requests
import os
import sys

KAGGLE_USERNAME = "AlAiElect"
KAGGLE_KERNEL_SLUG = "notebook8f0ddb0d68"
KAGGLE_API_TOKEN = "KGAT_261f60e51db1ac5bd7a612019ff8adbd"

def start_kaggle():
    print("⏳ در حال روشن کردن کاگل...")
    url = "https://www.kaggle.com/api/v1/kernels/run"
    headers = {"Authorization": f"Bearer {KAGGLE_API_TOKEN}", "Content-Type": "application/json"}
    data = {"kernel": f"{KAGGLE_USERNAME}/{KAGGLE_KERNEL_SLUG}"}
    try:
        response = requests.post(url, json=data, headers=headers, timeout=30)
        if response.status_code == 200:
            print("✅ کاگل با موفقیت روشن شد!")
            print(f"📊 پاسخ: {response.json()}")
        else:
            print(f"❌ خطا: {response.status_code}")
            print(f"📝 متن: {response.text[:200]}")
    except Exception as e:
        print(f"❌ خطا: {e}")

if __name__ == "__main__":
    start_kaggle()
