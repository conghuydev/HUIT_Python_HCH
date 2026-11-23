import tkinter as tk
import tkinter.messagebox as mb
from tkinter import ttk

def xacNhan():
    thanhPho = comboCity.get()
    
    if not thanhPho:
        mb.showerror("Loi", "Vui long chon thanh pho!")
    else:
        mb.showinfo("Thong bao", f"Thanh pho da chon: {thanhPho}")
        
def nhapLai():
    comboCity.set("")

root = tk.Tk()
root.title("Chon Thanh Pho")
root.geometry("400x250")

tk.Label(root, text="Chon thanh pho").pack(pady=15)

dsThanhPho = ["Ha Noi", "TP.HCM", "Da Nang", "Can Tho", "Hai Phong"]

comboCity = ttk.Combobox(root, values=dsThanhPho, state="readonly") # readonly chi cho phep chon thanh pho tu danh sach, khong tu y nhap
comboCity.pack(pady=10)

tk.Button(root, text="Xac nhan", command=xacNhan).pack(pady=5)
tk.Button(root, text="Nhap lai", command=nhapLai).pack(pady=5)
tk.Button(root, text="Dong", command=root.destroy).pack(pady=5)

root.mainloop()
