import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet
import os
import json

# ========== SETUP ==========
# Generate or load key
KEY_FILE = "secret.key"
DATA_FILE = "vault.json"

if os.path.exists(KEY_FILE):
    with open(KEY_FILE, "rb") as f:
        key = f.read()
else:
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)

fernet = Fernet(key)

# Load data
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        encrypted_data = json.load(f)
else:
    encrypted_data = {}

# ========== FUNCTIONS ==========

def save_password():
    site = site_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if not site or not password:
        messagebox.showwarning("Warning", "Site and Password cannot be empty!")
        return

    encrypted_pass = fernet.encrypt(password.encode()).decode()
    encrypted_data[site] = {"email": email, "password": encrypted_pass}

    with open(DATA_FILE, "w") as f:
        json.dump(encrypted_data, f, indent=2)

    site_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    messagebox.showinfo("Saved", f"Password for {site} saved successfully!")

def search_password():
    site = site_entry.get()
    if site in encrypted_data:
        record = encrypted_data[site]
        decrypted_pass = fernet.decrypt(record["password"].encode()).decode()
        messagebox.showinfo("Found", f"Email: {record['email']}\nPassword: {decrypted_pass}")
    else:
        messagebox.showerror("Not Found", f"No entry found for {site}")

# ========== GUI ==========
root = tk.Tk()
root.title("Secure Password Manager")
root.geometry("400x300")
root.resizable(False, False)

tk.Label(root, text="🔐 Secure Password Manager", font=("Arial", 16)).pack(pady=10)

form = tk.Frame(root)
form.pack(pady=10)

tk.Label(form, text="Site/Platform:").grid(row=0, column=0, sticky="e")
tk.Label(form, text="Email/Username:").grid(row=1, column=0, sticky="e")
tk.Label(form, text="Password:").grid(row=2, column=0, sticky="e")

site_entry = tk.Entry(form, width=30)
email_entry = tk.Entry(form, width=30)
password_entry = tk.Entry(form, width=30, show="*")

site_entry.grid(row=0, column=1, pady=5)
email_entry.grid(row=1, column=1, pady=5)
password_entry.grid(row=2, column=1, pady=5)

buttons = tk.Frame(root)
buttons.pack(pady=10)

tk.Button(buttons, text="💾 Save", command=save_password, width=10).grid(row=0, column=0, padx=10)
tk.Button(buttons, text="🔍 Search", command=search_password, width=10).grid(row=0, column=1, padx=10)

tk.Label(root, text="All data is encrypted 🔒", font=("Arial", 9), fg="gray").pack(side="bottom", pady=10)

root.mainloop()

