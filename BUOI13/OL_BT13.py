# -----------------------------------------------------------------------------
# Hiển thị danh sách sinh viên gồm Mã, Họ tên, Lớp, Điểm bằng ttk.Treeview.
# Khi chọn một dòng, hiển thị thông tin sinh viên trong các Label.
# -----------------------------------------------------------------------------
import tkinter as tk
from tkinter import ttk

def chonSinhVien(event):
    luaChon = bangSinhVien.selection()
    
    if not luaChon:
        return
    
    duLieu = bangSinhVien.item(luaChon[0], "values")    
    
    nhanMa.config(text=f"Mã sinh viên: {duLieu[0]}")
    nhanHoTen.config(text=f"Họ tên: {duLieu[1]}")
    nhanLop.config(text=f"Lớp: {duLieu[2]}")
    nhanDiem.config(text=f"Điểm: {duLieu[3]}")
    
root = tk.Tk()
root.title("Danh sách sinh viên")
root.geometry("800x400")

bangSinhVien = ttk.Treeview(root, columns=("Ma", "HoTen", "Lop", "Diem"), show="headings")

bangSinhVien.heading("Ma", text="Mã sinh viên")
bangSinhVien.heading("HoTen", text="Họ và tên")
bangSinhVien.heading("Lop", text="Lớp")
bangSinhVien.heading("Diem", text="Điểm")

bangSinhVien.pack(fill="both", expand=True, padx=10, pady=10)

nhanMa = tk.Label(root, text="Mã sinh viên: ")
nhanMa.pack()

nhanHoTen = tk.Label(root, text="Họ tên: ")
nhanHoTen.pack()

nhanLop = tk.Label(root, text="Lớp: ")
nhanLop.pack()

nhanDiem = tk.Label(root, text="Điểm: ")
nhanDiem.pack()

bangSinhVien.insert("", tk.END, values=("SV001", "Nguyễn Văn A", "16DHTH01", "8.5"))
bangSinhVien.insert("", tk.END, values=("SV002", "Nguyễn Văn B", "16DHTH02", "9.0"))
bangSinhVien.insert("", tk.END, values=("SV003", "Nguyễn Văn C", "16DHTH03", "9.5"))

bangSinhVien.bind("<<TreeviewSelect>>", chonSinhVien)


root.mainloop()