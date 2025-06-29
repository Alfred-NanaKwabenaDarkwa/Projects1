import json
import hashlib
import getpass
import os
from datetime import datetime 
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import secrets

JOURNAL_FILE = "journal.dat"
PASSWORD_FILE = "password.hash"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def derive_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key

def encrypt_data(data, password, salt=None):
    if salt is None:
        salt = secrets.token_bytes(16) 
    key = derive_key(password, salt)
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data.encode())
    return salt + encrypted  

def decrypt_data(encrypted_data, password):
    if len(encrypted_data) < 16:
        return None  
    salt = encrypted_data[:16]
    ciphertext = encrypted_data[16:]
    key = derive_key(password, salt)
    fernet = Fernet(key)
    try:
        return fernet.decrypt(ciphertext).decode()
    except:
        return None

def set_password():
    password = getpass.getpass("Set a new password : ")
    confirm_password = getpass.getpass("Confirm your password : ")
    if password == confirm_password:
        try:
            with open(PASSWORD_FILE, 'w') as f:
                f.write(hash_password(password))
            print('Password set sucessfully')
            return password
        except IOError as e:
            print(f"Error writing password file: {e}")
            return None
    else:
        print('Passwords don\'t match . Try again')
        return set_password()

def verify_password():
    if not os.path.exists(PASSWORD_FILE):
        print('No password set. Please set a password first.')
        return set_password()
    password = getpass.getpass('Enter your password for verification: ')
    try:
        with open(PASSWORD_FILE, 'r') as f:
            stored_hash = f.read().strip()
    except IOError as e:
        print(f"Error reading password file: {e}")
        return None
    if hash_password(password) == stored_hash:
        return password
    print('Incorrect password')
    return None

def load_journal(password):
    if os.path.exists(JOURNAL_FILE):
        with open(JOURNAL_FILE, 'rb') as f:
            encrypted_data = f.read()
        plaintext = decrypt_data(encrypted_data, password)
        if plaintext is None:
            print('Failed to decrypt journal. Incorrect password or corrupted file')
            return None
        try:
            return json.loads(plaintext)
        except json.JSONDecodeError:
            print("Error parsing journal data.")
            return None
    return {}

def save_journal(journal,password):
    json_data = json.dumps(journal, indent=4)
    encrypted_data = encrypt_data(json_data, password)
    with open(JOURNAL_FILE, 'wb') as f:
        f.write(encrypted_data)

def add_entry(journal, password):
    if not isinstance(journal, dict):
        print("Error : Journal data is invalid")
        return
    entry = input('Add your journal entry: ')
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    date_key = date[:10]
    if date_key not in journal:
        journal[date_key] = []
    journal[date_key].append({"time": date, "entry" : entry})
    save_journal(journal, password)
    print('\n Entry saved successfully')

def view_entries(journal):
    if not isinstance(journal, dict):
        print("Error: Journal data is invalid.")
        return
    if not journal:
        print('\n No entries found')
        return
    for date, entries in journal.items():
        print(f"\n Entries for {date}:")
        for entry in entries:
            print(f"[{entry['time']}] {entry['entry']}")

def main():
    print("Welcome to your 'secret CLI diary / journal 😊")

    password = verify_password()
    if password is None:
        print('Quiting')
        return
    
    journal = load_journal(password)
    if journal is None:
        print("Cannot load journal. Quiting.")
        return

    while True:
        print("\n Journal Menu?")
        print("1. Add entries")
        print('2. View entries')
        print("3. Change password")
        print("4. Exit")
        choice = input("Choose and enter an option from 1 to 4: ")

        if choice == "1":
            add_entry(journal, password)
        elif choice == "2":
            view_entries(journal)
        elif choice == "3":
            new_password = verify_password()
            if new_password:
                new_password = set_password()
                if journal:
                    save_journal(journal, new_password)
                    password = new_password
            else:
                print('Wrong password. Cannot change password.')
        elif choice == "4":
            print("\n Quiting your fav journal, 👋. See you later")
            break
        else:
            print("You entered a choice which isn't in the list. Please retry")

if __name__ == "__main__":
    main()
