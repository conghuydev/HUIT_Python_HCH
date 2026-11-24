#----------------------------------------------------------------------------
# Yêu cầu đề bài
# - Sử dụng Colorchooser để thay đổi màu nền cửa sổ và màu chữ.
# - Xử lý trường hợp người dùng hủy chọn màu.
#----------------------------------------------------------------------------
import tkinter as tk
import tkinter.messagebox as mb
from tkinter import colorchooser

def doiMauNen():
    mau = colorchooser.askcolor()
    
    if mau[1] is None:
        return
    
    root.config(bg=mau[1])

def doiMauChu():
    mau = colorchooser.askcolor()
    
    if mau[1] is None:
        return
    
    nhanTieuDe.config(fg=mau[1])

root = tk.Tk()
root.title("Ung dung chon mau")
root.geometry("500x450")

nhanTieuDe = tk.Label(root, text="UNG DUNG CHON MAU", font=("Times New Roman", 16, "bold"))
nhanTieuDe.grid(row=0, column=0, columnspan=2, sticky="nsew", pady=15)

nutDoiMauNen = tk.Button(root, text="Doi mau nen", command=doiMauNen)
nutDoiMauNen.grid(row=2, column=0, pady=15)

nutDoiMauChu = tk.Button(root, text="Doi mau chu", command=doiMauChu)
nutDoiMauChu.grid(row=2, column=1, pady=10)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.mainloop()