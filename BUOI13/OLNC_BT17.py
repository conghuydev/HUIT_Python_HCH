# -----------------------------------------------------------------------------
# Hiển thị Mã, Họ tên, Lớp, Điểm trong Treeview.
# Thêm sinh viên.
# Sửa thông tin sinh viên.
# Xóa sinh viên.
# Chọn dòng để đưa dữ liệu lên các Entry.
# -----------------------------------------------------------------------------
import tkinter as tk
import tkinter.messagebox as mb
from tkinter import ttk
import json
import os

def themSinhVien():
    ma = nhapMa.get().strip()
    ten = nhapHoTen.get().strip()
    lop = nhapLop.get().strip()
    diem = nhapDiem.get().strip()
    
    if not ma or not ten or not lop or not diem:
        mb.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin!")
        return
    
    try:
        diem = float(diem)
        
        if diem < 0 or diem > 10:
            mb.showerror("Lỗi", "Điểm phải nằm trong khoảng 0-10!")
            return
        
    except ValueError:
        mb.showerror("Lỗi", "Vui lòng nhập số hơp lệ!")
        return
    
    for dong in bangSinhVien.get_children():
        duLieu = bangSinhVien.item(dong, "values")
        
        if duLieu[0] == ma:
            mb.showerror("Lỗi", "Mã sinh viên bị trùng!")
            return
        
    bangSinhVien.insert("", tk.END, values=(ma, ten, lop, diem))
    mb.showinfo("Thông báo", "Thêm sinh viên thành công!")
    
    nhapMa.delete(0, tk.END)
    nhapHoTen.delete(0, tk.END)
    nhapLop.delete(0, tk.END)
    nhapDiem.delete(0, tk.END)
        
def chonSinhVien(event):
    luaChon = bangSinhVien.selection()
    
    if not luaChon:
        return
    
    duLieu = bangSinhVien.item(luaChon[0], "values")
    
    nhapMa.delete(0, tk.END)
    nhapHoTen.delete(0, tk.END)
    nhapLop.delete(0, tk.END)
    nhapDiem.delete(0, tk.END)
    
    nhapMa.insert(0, duLieu[0])
    nhapHoTen.insert(0, duLieu[1])
    nhapLop.insert(0, duLieu[2])
    nhapDiem.insert(0, duLieu[3])
    
def xoaSinhVien():
    luaChon = bangSinhVien.selection()
    
    if not luaChon:
        mb.showerror("Lỗi", "Vui lòng chọn sinh viên cần xóa!")
        return
    
    xacNhan = mb.askyesno("Xác nhận", "Bạn có chắc muốn xóa sinh viên này!")
    
    if xacNhan:
        bangSinhVien.delete(luaChon[0])
        
        nhapMa.delete(0, tk.END)
        nhapHoTen.delete(0, tk.END)
        nhapLop.delete(0, tk.END)
        nhapDiem.delete(0, tk.END)
        
        mb.showinfo("Thông báo", "Xóa sinh viên thành công!")
        
def suaSinhVien():
    luaChon = bangSinhVien.selection()
    
    if not luaChon:
        mb.showerror("Lỗi", "Vui lòng chọn sinh viên cần sửa!")
        return
    
    ma = nhapMa.get().strip()
    ten = nhapHoTen.get().strip()
    lop = nhapLop.get().strip()
    diem = nhapDiem.get().strip()
    
    if not ma or not ten or not lop or not diem:
        mb.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin!")
        return
    
    try:
        diem = float(diem)
        
        if diem < 0 or diem > 10:
            mb.showerror("Lỗi", "Điểm phải nằm trong khoảng 0-10!")
            return
        
    except ValueError:
        mb.showerror("Lỗi", "Vui lòng nhập số hơp lệ!")
        return
    
    for dong in bangSinhVien.get_children():
        duLieu = bangSinhVien.item(dong, "values")
        
        if dong != luaChon[0] and duLieu[0] == ma:
            mb.showerror("Lỗi", "Mã sinh viên đã tồn tại!")
            return
        
    bangSinhVien.item(luaChon[0], values=(ma, ten, lop, diem))
    mb.showinfo("Thông báo", "Sửa sinh viên thành công!")
    
    nhapMa.delete(0, tk.END)
    nhapHoTen.delete(0, tk.END)
    nhapLop.delete(0, tk.END)
    nhapDiem.delete(0, tk.END)
  
def luuJSON():
    danhSach = []
    
    for dong in bangSinhVien.get_children():
        duLieu = bangSinhVien.item(dong, "values")
        
        sinhVien = {
            "ma": duLieu[0],
            "ten": duLieu[1],
            "lop": duLieu[2],
            "diem": float(duLieu[3])
        }      
        danhSach.append(sinhVien)
    try:  
        with open("sinhvien.json", "w", encoding="utf-8") as f:
            json.dump(danhSach, f, ensure_ascii=False, indent=4)
            
        mb.showinfo("Thông báo", "Lưu file thành công!")
      
    except (OSError, json.JSONDecodeError, ValueError):
        mb.showerror("Lỗi", "Không thể lưu file!")
    
def docJSON():
    try:
        with open("sinhvien.json", "r", encoding="utf-8") as f:
            danhSach = json.load(f)
            
        for dong in bangSinhVien.get_children():
            bangSinhVien.delete(dong)
            
        for sinhVien in danhSach:
            bangSinhVien.insert(
                "", 
                tk.END,                           
                values=(
                    sinhVien["ma"],
                    sinhVien["ten"],
                    sinhVien["lop"],
                    sinhVien["diem"]
                )
            )
        mb.showinfo("Thông báo", "Đọc file JSON thành công!")

    except FileNotFoundError:
        mb.showerror("Lỗi", "Không tìm thấy file JSON!")
        
    except json.JSONDecodeError:
        mb.showerror("Lỗi", "File JSON không hợp lệ!")
        
root = tk.Tk()
root.title("Quản lý dữ liệu bằng Treeview")
root.geometry("800x400")

bangSinhVien = ttk.Treeview(root, columns=("Ma", "HoTen", "Lop", "Diem"), show="headings")

bangSinhVien.heading("Ma", text="Mã sinh viên")
bangSinhVien.heading("HoTen", text="Họ tên")
bangSinhVien.heading("Lop", text="Lớp")
bangSinhVien.heading("Diem", text="Điểm")

bangSinhVien.pack(fill="both", expand=True, padx=10, pady=10)

khungThongTin = tk.Frame(root)
khungThongTin.pack(pady=10)

tk.Label(khungThongTin, text="Mã sinh viên:").grid(row=0, column=0)
nhapMa = tk.Entry(khungThongTin, width=30)
nhapMa.grid(row=0, column=1, padx=10, pady=10)

tk.Label(khungThongTin, text="Họ tên:").grid(row=0, column=2)
nhapHoTen = tk.Entry(khungThongTin, width=30)
nhapHoTen.grid(row=0, column=3, padx=10, pady=10)

tk.Label(khungThongTin, text="Lớp:").grid(row=1, column=0)
nhapLop = tk.Entry(khungThongTin, width=30)
nhapLop.grid(row=1, column=1, padx=10, pady=10)

tk.Label(khungThongTin, text="Điểm:").grid(row=1, column=2)
nhapDiem = tk.Entry(khungThongTin, width=30)
nhapDiem.grid(row=1, column=3, padx=10, pady=10)

khungNut = tk.Frame(root)
khungNut.pack(pady=10)

tk.Button(khungNut, text="Thêm", width=10, command=themSinhVien).grid(row=0, column=0, padx=10)
tk.Button(khungNut, text="Xóa", width=10, command=xoaSinhVien).grid(row=0, column=1, padx=10)
tk.Button(khungNut, text="Sửa", width=10, command=suaSinhVien).grid(row=0, column=2, padx=10)
tk.Button(khungNut, text="Lưu JSON", width=10, command=luuJSON).grid(row=0, column=3, padx=10)
tk.Button(khungNut, text="Đọc JSON", width=10, command=docJSON).grid(row=0, column=4, padx=10)

bangSinhVien.bind("<<TreeviewSelect>>", chonSinhVien)

root.mainloop()