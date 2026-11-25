# -----------------------------------------------------------------------------
# Hiển thị Mã sinh viên, Họ tên, Ngày sinh, Lớp, Điểm bằng Treeview.
# Thêm, sửa, xóa sinh viên.
# Tìm kiếm và sắp xếp dữ liệu.
# Sử dụng Menu, DateEntry, Colorchooser.
# Lưu dữ liệu bằng JSON.
# -----------------------------------------------------------------------------
import tkinter as tk
import tkinter.messagebox as mb
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import date
import json

def themSinhVien():
    ma = nhapMa.get().strip()
    ten = nhapHoTen.get().strip()
    ngay = nhapNgaySinh.get_date()
    ngayChuoi = ngay.strftime("%d/%m/%Y")
    lop = nhapLop.get().strip()
    diem = nhapDiem.get().strip()
    
    if not ma or not ten or not lop or not diem:
        mb.showerror("Loi", "Vui long nhap day du thong tin!")
        return
    
    try:
        diem = float(diem)
        
        if diem < 0 or diem > 10:
            mb.showerror("Loi", "Diem phai nam trong khoang 0-10!")
            return
    
    except ValueError:
        mb.showerror("Loi", "Vui long nhap so hop le!")
        return
    
    for dong in bangSinhVien.get_children():
        duLieu = bangSinhVien.item(dong, "values")
        
        if duLieu[0] == ma:
            mb.showerror("Loi", "Ma sinh vien da ton tai!")
            return
        
    if ngay > date.today():
        mb.showerror("Loi", "Ngay sinh khong duoc lon hon ngay hien tai!")
        return
    
    bangSinhVien.insert("", tk.END, values=(ma, ten, ngayChuoi, lop, diem))
    mb.showinfo("Thong bao", "Them thanh cong!")
    
    nhapMa.delete(0, tk.END)
    nhapHoTen.delete(0, tk.END)
    
    nhapNgaySinh.set_date(date.today())
    
    nhapLop.delete(0, tk.END)
    nhapDiem.delete(0, tk.END)
        
def chonSinhVien(event):
    luaChon = bangSinhVien.selection()
    
    if not luaChon:
        return
    
    duLieu = bangSinhVien.item(luaChon[0], "values")
    
    nhapMa.delete(0, tk.END)
    nhapHoTen.delete(0, tk.END)
    # nhapNgaySinh.set_date(date.today())
    nhapLop.delete(0, tk.END)
    nhapDiem.delete(0, tk.END)
    
    nhapMa.insert(0, duLieu[0])
    nhapHoTen.insert(0, duLieu[1])
    nhapNgaySinh.set_date(duLieu[2])
    nhapLop.insert(0, duLieu[3])
    nhapDiem.insert(0, duLieu[4])
    
def suaSinhVien():
    luaChon = bangSinhVien.selection()
    
    if not luaChon:
        mb.showerror("Loi", "Vui long chon sinh vien!")
        return
    
    ma = nhapMa.get().strip()
    ten = nhapHoTen.get().strip()
    ngay = nhapNgaySinh.get_date()
    ngayChuoi = ngay.strftime("%d/%m/%Y")
    lop = nhapLop.get().strip()
    diem = nhapDiem.get().strip()
    
    if not ma or not ten or not lop or not diem:
        mb.showerror("Loi", "Vui long nhap day du thong tin!")
        return
    
    try:
        diem = float(diem)
        
        if diem < 0 or diem > 10:
            mb.showerror("Loi", "Diem phai nam trong khoang 0-10!")
            return
    
    except ValueError:
        mb.showerror("Loi", "Vui long nhap so hop le!")
        return
    
    for dong in bangSinhVien.get_children():
        duLieu = bangSinhVien.item(dong, "values")
        
        if dong != luaChon[0] and duLieu[0] == ma:
            mb.showerror("Loi", "Ma sinh vien da ton tai!")
            return
        
    if ngay > date.today():
        mb.showerror("Loi", "Ngay sinh khong duoc lon hon ngay hien tai!")
        return
    
    bangSinhVien.item(luaChon[0], values=(ma, ten, ngayChuoi, lop, diem))
    mb.showinfo("Thong bao", "Sua sinh vien thanh cong!")
    
    nhapMa.delete(0, tk.END)
    nhapHoTen.delete(0, tk.END)
    nhapNgaySinh.set_date(date.today())
    nhapLop.delete(0, tk.END)
    nhapDiem.delete(0, tk.END)
        
    
def xoaSinhVien():
    luaChon = bangSinhVien.selection()
    
    if not luaChon:
        mb.showerror("Loi", "Vui long chon sinh vien!")
        return
    
    xacNhan = mb.askyesno("Xac nhan", "Ban co chac muon xoa sinh vien nay!")
    
    if xacNhan:
        bangSinhVien.delete(luaChon[0])
        mb.showinfo("Thong bao", "Xoa sinh vien thanh cong!")
        
        nhapMa.delete(0, tk.END)
        nhapHoTen.delete(0, tk.END)
        nhapNgaySinh.set_date(date.today())
        nhapLop.delete(0, tk.END)
        nhapDiem.delete(0, tk.END)
     
def luuJson():
    danhSach = []
    
    for dong in bangSinhVien.get_children():
        duLieu = bangSinhVien.item(dong, "values")
        
        sinhVien = {
            "ma": duLieu[0],
            "ten": duLieu[1],
            "ngay": duLieu[2],
            "lop": duLieu[3],
            "diem": float(duLieu[4])
        }
        
        danhSach.append(sinhVien)
    
    try:
        with open("danhsach.json", "w", encoding="utf-8") as f:
            json.dump(danhSach, f, ensure_ascii=False, indent=4)
        
        mb.showinfo("Thong bao", "Luu file thanh cong!")
    
    except (OSError, json.JSONDecodeError, ValueError):
        mb.showerror("Loi", "Khong the luu file!")
        
def docJson():
    try:
        with open("danhsach.json", "r", encoding="utf-8") as f:
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
                    sinhVien["ngay"],
                    sinhVien["lop"],
                    sinhVien["diem"]
                )
            )
        mb.showinfo("Thong bao", "Doc file json thanh cong!")
    
    except FileNotFoundError:
        mb.showerror("Loi", "Khong tim thay file json!")
        
    except json.JSONDecodeError:
        mb.showerror("Loi", "Loi mo file json!")
        
def timKiemSinhVien():
    tuKhoa = nhapTuKhoa.get().strip().lower()
    
    if not tuKhoa:
        mb.showerror("Loi", "Vui long nhap thong tin!")
        return
    
    for dong in bangSinhVien.get_children():
        duLieu = bangSinhVien.item(dong, "values")
        
        if tuKhoa in duLieu[0].lower() or tuKhoa in duLieu[1].lower():
            bangSinhVien.selection_set(dong)
            bangSinhVien.see(dong)
            return
            
    mb.showerror("Loi", "Khong tim thay sinh vien!")
    return

def sapXepSinhVienTheoDiem():
    danhSach = []
    
    for dong in bangSinhVien.get_children():
        duLieu = bangSinhVien.item(dong, "values")
        
        diem = float(duLieu[4])
        danhSach.append((diem, dong))
        
    danhSach.sort(reverse=True)
    
    for viTri, (diem, dong) in enumerate(danhSach):
        bangSinhVien.move(dong, "", viTri)
        
    mb.showinfo("Thong bao", "Sap xep sinh vien thanh cong!")
        
root = tk.Tk()
root.title("Quan ly sinh vien")
root.geometry("1000x600")

khungTimKiem = tk.Frame(root)
khungTimKiem.pack(pady=10)

tk.Label(khungTimKiem, text="Tim kiem sinh vien:").grid(row=0, column=0, padx=10, pady=10)
nhapTuKhoa = tk.Entry(khungTimKiem, width=30)
nhapTuKhoa.grid(row=0, column=1, padx=10, pady=10)

tk.Button(khungTimKiem, text="Tim kiem", width=10, command=timKiemSinhVien).grid(row=0, column=2)

bangSinhVien = ttk.Treeview(root, columns=("Ma", "HoTen", "NgaySinh", "Lop", "Diem"), show="headings")

bangSinhVien.heading("Ma", text="Ma sinh vien")
bangSinhVien.heading( "HoTen", text="Ho Ten")
bangSinhVien.heading("NgaySinh", text="Ngay sinh")
bangSinhVien.heading("Lop", text="Lop")
bangSinhVien.heading("Diem", text="Diem")

bangSinhVien.pack(fill="both", expand=True, padx=10, pady=10)

khungThongTin = tk.Frame(root)
khungThongTin.pack(pady=10)

tk.Label(khungThongTin, text="Ma sinh vien:").grid(row=0, column=0, padx=10, pady=10)
nhapMa = tk.Entry(khungThongTin, width=30)
nhapMa.grid(row=0, column=1)

tk.Label(khungThongTin, text="Ho ten:").grid(row=1, column=00, padx=10, pady=10)
nhapHoTen = tk.Entry(khungThongTin, width=30)
nhapHoTen.grid(row=1, column=1)

tk.Label(khungThongTin, text="Ngay sinh:").grid(row=2, column=0, padx=10, pady=10)
nhapNgaySinh = DateEntry(khungThongTin, width=30, date_pattern="dd/mm/yyyy")
nhapNgaySinh.grid(row=2, column=1)

tk.Label(khungThongTin, text="Lop:").grid(row=3, column=0, padx=10, pady=10)
nhapLop = tk.Entry(khungThongTin, width=30)
nhapLop.grid(row=3, column=1)

tk.Label(khungThongTin, text="Diem:").grid(row=4, column=0, padx=10, pady=10)
nhapDiem = tk.Entry(khungThongTin, width=30)
nhapDiem.grid(row=4, column=1)

khungNut = tk.Frame(root)
khungNut.pack(pady=10)

tk.Button(khungNut, text="Them", width=10, command=themSinhVien).grid(row=0, column=0, padx=10)
tk.Button(khungNut, text="Sua", width=10, command=suaSinhVien).grid(row=0, column=1, padx=10)
tk.Button(khungNut, text="Xoa", width=10, command=xoaSinhVien).grid(row=0, column=2, padx=10)
tk.Button(khungNut, text="Sap xep", width=10, command=sapXepSinhVienTheoDiem).grid(row=0, column=3, padx=10)
tk.Button(khungNut, text="Luu JSON", width=10, command=luuJson).grid(row=0, column=4, padx=10)
tk.Button(khungNut, text="Doc JSON", width=10, command=docJson).grid(row=0, column=5, padx=10)


bangSinhVien.bind("<<TreeviewSelect>>", chonSinhVien)

root.mainloop()