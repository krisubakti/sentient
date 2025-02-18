import time
import random
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import os
from pyfiglet import figlet_format
from termcolor import colored

# Load environment variables
load_dotenv()

# Print banner
print(colored(figlet_format("PEMPEK LAHAT"), "blue"))
print("🔹 Script mulai berjalan...")

# Load private keys from .env
accounts = [
    os.getenv("WALLET_PRIVATE_KEY_1"),
    os.getenv("WALLET_PRIVATE_KEY_2"),
    os.getenv("WALLET_PRIVATE_KEY_3")
]
print(f"🔹 Akun yang ditemukan: {accounts}")

# Questions list
questions = [
    "Apa manfaat desentralisasi dalam blockchain?",
    "Bagaimana keamanan dalam jaringan blockchain terjamin?",
    "Apa perbedaan antara Proof of Work dan Proof of Stake?",
    "Mengapa gas fee di Ethereum bisa tinggi?",
    "Apa keuntungan menggunakan smart contract?",
    "Bagaimana cara kerja mekanisme konsensus dalam blockchain?",
    "Apa itu layer 2 dalam teknologi blockchain?",
    "Bagaimana NFT bisa memiliki nilai?",
    "Apa tantangan utama dalam adopsi blockchain?",
    "Apa keuntungan menggunakan DeFi dibandingkan bank tradisional?"
]
print("🔹 Environment variables dimuat...")

# Voting options
vote_options = ["Left is Better", "Right is Better", "Tie", "Both are Bad"]

def run_automation(account):
    with sync_playwright() as p:
        print("🔹 Membuka browser...")
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        print("🔹 Mengakses website Sentient...")
        page.goto("https://dobby-arena.sentient.xyz/")
        time.sleep(5)

        print("🔹 Mencari tombol login...")
        page.click("text=Login with Wallet")
        time.sleep(10)  # Tunggu login manual

        for i in range(10):
            question = random.choice(questions)
            print(f"🔹 Mengirim pertanyaan: {question}")
            page.wait_for_selector("textarea", timeout=10000)
            page.fill("textarea", question)
            page.keyboard.press("Enter")
            
            time.sleep(5)

            random_vote = random.choice(vote_options)
            print(f"🔹 Memilih vote: {random_vote}")
            page.wait_for_selector(f"text={random_vote}", timeout=10000)
            page.click(f"text={random_vote}")

            print(f"✅ Vote berhasil: {random_vote}")
            time.sleep(3)

        print("🔹 Menutup browser...")
        browser.close()

# Execute for each account
for account in accounts:
    if account:
        run_automation(account)
        print("🔹 Menunggu sebelum menjalankan akun berikutnya...")
        time.sleep(20)  # Jeda antar akun

print("✅ Script selesai!")