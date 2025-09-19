WhatsApp Automation with Selenium

This project automates sending WhatsApp messages to multiple contacts using Python, Selenium, and Chrome.
It supports:

Importing contacts from a CSV file

Sending messages in batches (e.g., 200 at a time to avoid spam detection)

Using an existing Chrome profile to skip scanning the QR code every time

⚡ Features

✅ Load contacts from a contacts.csv file
✅ Send personalized or bulk messages
✅ Batch sending (e.g., 200 contacts per run)
✅ Delay between messages to mimic human behavior
✅ Uses your WhatsApp Web session without logging in repeatedly

📂 Project Structure
├── whatsapp_automation.py   # Main automation script
├── contacts.csv             # CSV file with contacts
└── README.md                # Project documentation

🛠 Requirements

Python 3.9+ (tested on Python 3.13.3)

Google Chrome (latest stable version)

ChromeDriver (matching your Chrome version)

Download from: ChromeDriver

Install dependencies:

pip install selenium pandas

📄 CSV Format

Your contacts.csv must have a column named Name with WhatsApp contact names saved in your phone. Example:

Name
John Doe
Person 1
Family Group
Best Friend

⚙️ Configuration

Inside whatsapp_automation.py, you can configure:

CSV_FILE = "contacts.csv"        # Path to your contacts file
MESSAGE = "hello my name is ayush"
BATCH_SIZE = 200                 # Number of contacts per batch
DELAY_BETWEEN_MSGS = 3           # Seconds delay between messages

PROFILE_PATH = r"C:\Users\<YourUser>\AppData\Local\Google\Chrome\User Data"
PROFILE_DIR = "Person 1"         # Change to your Chrome profile (e.g., "Default", "Profile 1")


👉 Important: Replace <YourUser> with your Windows username.

▶️ Running the Script

Make sure all Chrome windows are closed.

Run the script:

python whatsapp_automation.py


The script will open WhatsApp Web with your chosen profile.

Messages will be sent batch by batch.

⚠️ Disclaimer

This project is for educational purposes only.

Use responsibly. Spamming or misuse of WhatsApp automation may lead to account ban.

Always respect WhatsApp’s terms of service.

🤝 Contributing

Feel free to fork this repo, improve the code, and submit pull requests 🚀