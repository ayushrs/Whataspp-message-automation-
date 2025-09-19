from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import math

# ======================
# SETTINGS
# ======================
CSV_FILE = "contacts.csv"   # Path to your contacts file
MESSAGE = "hello my name is ayush"
BATCH_SIZE = 200            # Number of contacts per run
DELAY_BETWEEN_MSGS = 3      # Seconds delay to avoid spam detection

# Use a dedicated profile folder for Selenium
# (This will be created if it doesn’t exist)
PROFILE_PATH = r"D:\selenium_profile"   # <-- NEW FOLDER just for Selenium
# ======================

# Load contacts
df = pd.read_csv(CSV_FILE)
contacts = df["Name"].dropna().tolist()
total_contacts = len(contacts)
print(f"Loaded {total_contacts} contacts from {CSV_FILE}")

# Setup Chrome with persistent profile (no QR every time after first login)
options = webdriver.ChromeOptions()
options.add_argument(f"--user-data-dir={PROFILE_PATH}")

driver = webdriver.Chrome(options=options)
driver.get("https://web.whatsapp.com")
print("👉 Scan the QR code once. It will stay logged in for future runs.")
time.sleep(15)  # wait for WhatsApp to fully load

# Process in batches
total_batches = math.ceil(total_contacts / BATCH_SIZE)

for batch in range(total_batches):
    print(f"\n🚀 Starting batch {batch + 1}/{total_batches}")
    start = batch * BATCH_SIZE
    end = min((batch + 1) * BATCH_SIZE, total_contacts)
    batch_contacts = contacts[start:end]

    for contact in batch_contacts:
        try:
            # 🔍 Search contact
            search_box = driver.find_element(By.XPATH, "//div[@contenteditable='true'][@data-tab='3']")
            search_box.clear()
            search_box.click()
            time.sleep(1)
            search_box.send_keys(contact)
            time.sleep(2)

            # ✅ Select contact
            user = driver.find_element(By.XPATH, f"//span[@title='{contact}']")
            user.click()
            time.sleep(1)

            # 💬 Type and send message
            message_box = driver.find_element(By.XPATH, "//div[@contenteditable='true'][@data-tab='10']")
            message_box.send_keys(MESSAGE)
            message_box.send_keys(Keys.ENTER)

            print(f"✅ Message sent to {contact}")
            time.sleep(DELAY_BETWEEN_MSGS)

        except Exception as e:
            print(f"❌ Could not send to {contact}: {e}")
            continue

    print(f"✅ Finished batch {batch + 1}. Take a break before next batch!")

print("\n🎉 All messages sent!")
driver.quit()
