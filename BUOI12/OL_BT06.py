import tkinter as tk
import os
import json
import hashlib
import hmac
import tkinter.messagebox as mb

FILE_NAME = "user.json"

# Doc danhs ach nguoii dung
def readUser():
    if not os.path.exists(FILE_NAME):
        return []
    
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        return json.load(f)
    
# Kiem tra mat khau
def verifyPassword(password, saltHex, hashHex):
    salt = bytes.fromhex(saltHex)
    
    hashed = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 600000)
    
    return hmac.compare_digest(hashed.hex(), hashHex)

# Dang nhap
def login():
    email = entry_email.get().strip().lower()
    password = entry_password.get()
    
    # Kiem tra thong tin rong
    if not email or not password:
        mb.showerror("Loi", "Vui long nhap day du thong tin!")
        return
    
    # Doc file JSON
    try:
        users = readUser()
        
        if not isinstance(users, list):
            raise ValueError
            
    except (OSError, json.JSONDecodeError, ValueError):
        mb.showerror("Loi", "Khong mo duoc file user.json!")
        return
    
    # Kiểm tra email và mật khẩu   
    for user in users:
        if user["email"].lower() == email:
            try:
                valid = verifyPassword(password, user["salt"], user["password_hash"])
            except (KeyError, ValueError, TypeError):
                valid = False
                
            if valid:
                mb.showinfo("Thong bao", "Dang nhap thanh cong!")
            else:
                mb.showerror("Loi", "Dang nhap that bai!")
                
            return 
    mb.showerror("Loi", "Dang nhap that bai!")
    
# Giao dien
root = tk.Tk()
root.title("Dang nhap tai khoan")
root.geometry("450x220")

tk.Label(root, text="Email:").grid(row=0, column=0, padx=10, pady=10)
entry_email = tk.Entry(root, width=30)
entry_email.grid(row=0, column=1)

tk.Label(root, text="Mat khau:").grid(row=1, column=0, padx=10, pady=10)
entry_password = tk.Entry(root, width=30, show="*")
entry_password.grid(row=1, column=1)

loginButton = tk.Button(root, text="Dang nhap", width=30, command=login)
loginButton.grid(row=2, column=0, columnspan=2, pady=15)

root.mainloop()