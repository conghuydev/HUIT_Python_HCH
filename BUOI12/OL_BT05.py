import tkinter as tk
import tkinter.messagebox as mb
import json
import os
import re
import secrets
import hashlib
from datetime import datetime, date

FILE_NAME = "user.json"

# DOC DANH SACH NGUOI DUNG
def readUser():
    if not os.path.exists(FILE_NAME):
        return []
    
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        return json.load(f)

# LUU DANH SACH NGUOI DUNG
def saveUser(users):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        return json.dump(users, f, ensure_ascii=False, indent=4)
    
# TINH TUOI
def calculateAge(birthday):
    today = date.today()
    age = today.year - birthday.year
    
    if (today.month, today.day) < (birthday.month, birthday.day):
        age -=1
    
    return age

# BAM MAT KHAU 
def hashPassword(password):
    salt = secrets.token_bytes(16)
    
    hashed = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 600000)
    return salt.hex(), hashed.hex()

# DANG KY TAI KHOAN 
def register():
    name = entryName.get().strip()
    birthdayText = entryBirthday.get().strip()
    email = entryEmail.get().strip().lower()
    password = entryPassword.get()
    confirm = entryConfirm.get()

    # KIEM TRA THONG TIN RONG
    if not name or not birthdayText or not email or not password or not confirm:
        mb.showwarning("Canh bao", "Vui long nhap day du thong tin!")
        return 
    
    # KIEM TRA DINH DANG EMAIL
    emailPattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    
    if not re.fullmatch(emailPattern, email):
        mb.showerror("Loi", "Email khong dung dinh dang!")
        return 
    
    # KIEM TRA MAT KHAU TRUNG KHOP
    if password != confirm:
        mb.showerror("Loi", "Hai mat khau khong trung nhau!")
        return
    
    # KIEM TRA NGAY SINH
    try:
        birthday = datetime.strptime(birthdayText, "%d/%m/%Y").date()
        
    except ValueError:
        mb.showerror("Loi", "Ngay sinh khong hop le! Vui long nhap theo dd/mm/yyyy.")
        return
    
    # KIEM TRA DU 18 TUOI
    if calculateAge(birthday) < 18:
        mb.showerror("Loi", "Nguoi dung phai tu 18 tuoi tro len!")
        return
    
    # DOC DU LIEU JSON
    try:
        users = readUser()
        
        if not isinstance(users, list):
            raise ValueError
            
    except (OSError, json.JSONDecodeError, ValueError):
        mb.showerror("Loi", "Khong the doc duoc file user.json!")
        return 
    
    # KIEM TRA EMAIL DA TON TAI 
    for user in users:
        if user["email"].lower() == email:
            mb.showerror("Loi", "Email da ton tai!")
            return
        
    # BAM MAT KHAU
    salt, passwordHash = hashPassword(password)
    
    # TAO TAI KHOAN MOI 
    newUser = {
        "name":name,
        "birthday":birthdayText,
        "email":email,
        "salt": salt,
        "password_hash": passwordHash
    }
    
    # THEM TAI KHOAN VAO DANH SACH
    users.append(newUser)
    
    # GHI DU LIEU VAO JSON
    try:
        saveUser(users)
    
    except OSError:
        mb.showerror("Loi", "Khong the luu thong tin nguoi dung!")
        return
    
    mb.showinfo("Thong bao", "Dang ky tai khoan thanh cong!")
    
    # XOA CAC O NHAP LIEU
    entryName.delete(0, tk.END)
    entryBirthday.delete(0, tk.END)
    entryEmail.delete(0, tk.END)
    entryPassword.delete(0, tk.END)
    entryConfirm.delete(0, tk.END)
    
root = tk.Tk()
root.title("Dang ky tai khoan")
root.geometry("450x300")

tk.Label(root, text="Ho va ten:").grid(
    row=0, column=0, padx=10, pady=10)
entryName = tk.Entry(root, width=30)
entryName.grid(row=0, column=1)

tk.Label(root, text="Ngay sinh:").grid(
    row=1, column=0,padx=10, pady=10)
entryBirthday = tk.Entry(root, width=30)
entryBirthday.grid(row=1, column=1)

tk.Label(root, text="Email:").grid(
    row=2, column=0, padx=10, pady=10)
entryEmail = tk.Entry(root, width=30)
entryEmail.grid(row=2, column=1)

tk.Label(root, text="Mat khau:").grid(
    row=3, column=0, padx=10, pady=10)
entryPassword= tk.Entry(root, width=30)
entryPassword.grid(row=3, column=1)

tk.Label(root, text="Nhap lai mat khau:").grid(
    row=4, column=0, padx=10, pady=10)
entryConfirm = tk.Entry(root, width=30)
entryConfirm.grid(row=4, column=1)

registerButton = tk.Button(root, text="Dang ky", width=15, command=register)
registerButton.grid(row=5, column=0, columnspan=2, pady=20)

root.mainloop()

    
        
    