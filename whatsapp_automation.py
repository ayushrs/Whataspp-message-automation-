from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import math

# ======================
# SETTINGS
# ======================
CSV_FILE = "contacts.csv"   # Path to your contacts file
MESSAGE = "Radhe Radhe"
BATCH_SIZE = 200            # Number of contacts per run
DELAY_BETWEEN_MSGS = 3      # Seconds delay to avoid spam detection

PROFILE_PATH = r"D:\selenium_profile"   # Persistent profile (no QR each time)
# ======================

# Load contacts
df = pd.read_csv(CSV_FILE)
contacts = df["Name"].dropna().tolist()
total_contacts = len(contacts)
print(f"Loaded {total_contacts} contacts from {CSV_FILE}")

# Setup Chrome
options = webdriver.ChromeOptions()
options.add_argument(f"--user-data-dir={PROFILE_PATH}")

driver = webdriver.Chrome(options=options)
driver.get("https://web.whatsapp.com")
print("👉 Scan the QR code if required...")

# Wait until WhatsApp home screen loads (chat list or search bar)
try:
    WebDriverWait(driver, 180).until(
        EC.any_of(
            EC.presence_of_element_located((By.XPATH, "//div[@role='textbox'][@contenteditable='true']")),
            EC.presence_of_element_located((By.ID, "pane-side"))
        )
    )
    print("✅ WhatsApp loaded successfully!")
except:
    print("❌ Timeout: WhatsApp did not load in time.")
    driver.quit()
    exit()

# ======================
# Process in batches
# ======================
total_batches = math.ceil(total_contacts / BATCH_SIZE)

for batch in range(total_batches):
    print(f"\n🚀 Starting batch {batch + 1}/{total_batches}")
    start = batch * BATCH_SIZE
    end = min((batch + 1) * BATCH_SIZE, total_contacts)
    batch_contacts = contacts[start:end]

    for contact in batch_contacts:
        try:
            # 🔍 Search contact
            search_box = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@role='textbox'][@contenteditable='true']"))
            )
            search_box.clear()
            search_box.click()
            time.sleep(1)
            search_box.send_keys(contact)
            time.sleep(2)

            # ✅ Select contact
            user = driver.find_element(By.XPATH, f"//span[@title='{contact}']")
            user.click()
            time.sleep(1)

            # 💬 Find the *last* editable textbox (message box)
            message_box = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.XPATH, "//div[@role='textbox'][@contenteditable='true']"))
            )[-1]

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
