import tkinter as tk
import tkinter.messagebox as mb
from tkinter import ttk
import json

danhSachSinhVien = []
tenFile = "sinhvien.json"

def tinhDTB(python, csdl, mmt):
    return round((python + csdl + mmt) / 3, 2)

def xepLoai(dtb):
    if dtb >= 8:
        return "Gioi"
    elif dtb >= 6.5:
        return "Kha"
    elif dtb >= 5:
        return "Trung binh"
    else:
        return "Yeu"
    
def xoaTrang():
    nhapMa.delete(0, tk.END)
    nhapTen.delete(0, tk.END)
    nhapLop.delete(0, tk.END)
    nhapPython.delete(0, tk.END)
    nhapCSDL.delete(0, tk.END)
    nhapMMT.delete(0, tk.END)

def themSinhVien():
    ma = nhapMa.get().strip()
    ten = nhapTen.get().strip()
    lop = nhapLop.get().strip()

    if not ma or not ten or not lop:
        mb.showerror("Loi", "Vui long nhap day du!")
        return
    
    try:
        python = float(nhapPython.get())
        csdl = float(nhapCSDL.get())
        mmt = float(nhapMMT.get())
        
        if not (0 <= python <= 10 and 0 <= csdl <= 10 and 0 <= mmt <= 10):
        
            mb.showerror("Loi", "Vui long nhap tu 0-10!")
            return
    except ValueError:
        mb.showerror("Loi", "Vui long nhap so hop le!")
        return
    
    for dong in bangSinhVien.get_children():
        duLieu = bangSinhVien.item(dong, "values")
        
        if duLieu[0] == ma:
            mb.showerror("Loi", "Ma sinh vien da ton tai!")
            return
        
    dtb = tinhDTB(python, csdl, mmt)
    loai = xepLoai(dtb)
    
    bangSinhVien.insert("", tk.END, values=(ma, ten, lop, python, csdl, mmt, dtb, loai))
    mb.showinfo("Thong bao", "Them sinh vien thanh cong!")
    
    xoaTrang()
    
def chonSinhVien(event):
    luaChon = bangSinhVien.selection()
    
    if not luaChon:
        return
    
    duLieu = bangSinhVien.item(luaChon[0], "values")
    
    xoaTrang()
    
    nhapMa.insert(0, duLieu[0])
    nhapTen.insert(0, duLieu[1])
    nhapLop.insert(0, duLieu[2])
    nhapPython.insert(0, duLieu[3])
    nhapCSDL.insert(0, duLieu[4])
    nhapMMT.insert(0, duLieu[5])

def xoaSinhVien():
    luaChon = bangSinhVien.selection()
    
    if not luaChon:
        mb.showerror("Loi", "Vui long chon sinh vien!")
        return
    
    xacNhan = mb.askyesno("Xac nhan", "Ban co chac muon xoa sinh vien nay!")
    
    if xacNhan:
        bangSinhVien.delete(luaChon[0])
        mb.showinfo("Loi", "Xoa thanh cong!")
        
        xoaTrang()
        
def suaSinhVien():
    luaChon = bangSinhVien.selection()
    
    if not luaChon:
        mb.showerror("Loi", "Vui long chon sinh vien!")
        return 
    
    ma = nhapMa.get().strip()
    ten = nhapTen.get().strip()
    lop = nhapLop.get().strip()

    if not ma or not ten or not lop:
        mb.showerror("Loi", "Vui long nhap day du!")
        return
    
    try:
        python = float(nhapPython.get())
        csdl = float(nhapCSDL.get())
        mmt = float(nhapMMT.get())
        
        if not (0 <= python <= 10 and 0 <= csdl <= 10 and 0 <= mmt <= 10):
        
            mb.showerror("Loi", "Vui long nhap tu 0-10!")
            return
    except ValueError:
        mb.showerror("Loi", "Vui long nhap so hop le!")
        return
    
    for dong in bangSinhVien.get_children():
        duLieu = bangSinhVien.item(dong, "values")
        
        if dong != luaChon[0] and duLieu[0] == ma:
            mb.showerror("Loi", "Ma sinh vien da ton tai!")
            return
        
    dtb = tinhDTB(python, csdl, mmt)
    loai = xepLoai(dtb)
    
    bangSinhVien.item(luaChon[0], values=(ma, ten, lop, python, csdl, mmt, dtb, loai))
    mb.showinfo("Thong bao", "Sua thanh cong!")
    
    xoaTrang()
   
def timKiemSinhVien():
    tuKhoa = nhapTuKhoa.get().strip().lower()
    
    if not tuKhoa:
        mb.showerror("Loi", "Vui long nhap tu khoa!")
        return
    
    for dong in bangSinhVien.get_children():
        duLieu = bangSinhVien.item(dong, "values")
        
        if tuKhoa in duLieu[0].lower() or tuKhoa in duLieu[1].lower():
            bangSinhVien.selection_set(dong)
            bangSinhVien.see(dong)
            return
        
    mb.showerror("Loi", "Khong tim thay!")
    return

def luuJson():
    danhSachSinhVien = []
    
    for dong in bangSinhVien.get_children():
        duLieu = bangSinhVien.item(dong, "values")
        
        sinhVien = {
            "ma": duLieu[0],
            "ten": duLieu[1],
            "lop": duLieu[2],
            "python": duLieu[3],
            "csdl": duLieu[4],
            "mmt": duLieu[5],
            "dtb": duLieu[6],
            "loai": duLieu[7]
        }
        danhSachSinhVien.append(sinhVien)
    try:
        with open(tenFile, "w", encoding="utf-8") as f:
            json.dump(danhSachSinhVien, f, ensure_ascii=False, indent=4)
            
        mb.showinfo("Thong bao", "Luu thanh cong!")
        
    except (OSError, ValueError):
        mb.showerror("Loi", "Luu that bai!")
        return
    
def docJson():
    try:
        with open(tenFile, "r", encoding="utf-8") as f:
            danhSachSinhVien = json.load(f)
            
        for dong in bangSinhVien.get_children():
            bangSinhVien.delete(dong)
            
        for sinhVien in danhSachSinhVien:
            bangSinhVien.insert(
                "",
                tk.END,
                values=(
                    sinhVien["ma"],
                    sinhVien["ten"],
                    sinhVien["lop"],
                    sinhVien["python"],
                    sinhVien["csdl"],
                    sinhVien["mmt"],
                    sinhVien["dtb"],
                    sinhVien["loai"]
                )
            )
        mb.showinfo("Thong bao", "Them thanh cong!")
        
    except FileNotFoundError:
        mb.showerror("Loi", "Khong tim thay file!")
        return
    
    except json.JSONDecodeError:
        mb.showerror("Loi", "Loi mo file!")
        return
    
def thongKe():
    gioi = 0
    kha = 0
    trungBinh = 0
    yeu = 0
    
    for dong in bangSinhVien.get_children():
        duLieu = bangSinhVien.item(dong, "values")
        
        if duLieu[7] == "Gioi":
            gioi += 1 
        elif duLieu[7] == "Kha":
            kha += 1
        elif duLieu[7] == "Trung binh":
            trungBinh += 1
        elif duLieu[7] == "Yeu":
            yeu += 1
            
    maxSL = max(gioi, kha, trungBinh, yeu, 1)
    
    caoGioi = gioi / maxSL * 80
    caoKha = kha / maxSL * 80
    caoTrungBinh = trungBinh / maxSL * 80
    caoYeu = yeu / maxSL * 80
    
    bieuDo.delete("all")

    # Cot gioi
    bieuDo.create_rectangle(100, 100 - caoGioi, 200, 100, fill="green")
    bieuDo.create_text(150, 115, text="Gioi")
    bieuDo.create_text(150, 90 - caoGioi, text=gioi)            
    
    bieuDo.create_rectangle(350, 100 - caoKha, 450, 100, fill="blue")
    bieuDo.create_text(400, 115, text="Kha")
    bieuDo.create_text(400, 90 - caoKha, text=kha)      
    
    bieuDo.create_rectangle(600, 100 - caoTrungBinh, 700, 100, fill="orange")
    bieuDo.create_text(650, 115, text="Trung binh")
    bieuDo.create_text(650, 90 - caoTrungBinh, text=trungBinh)      
    
    bieuDo.create_rectangle(850, 100 - caoYeu, 950, 100, fill="green")
    bieuDo.create_text(900, 115, text="Yeu")
    bieuDo.create_text(900, 90 - caoYeu, text=yeu)      
            
root = tk.Tk()
root.title("Quan ly diem sinh vien")
root.geometry("1200x800")

# Thong tin
khungNhap = tk.LabelFrame(root, text="Thong tin sinh vien")
khungNhap.pack(padx=10, pady=10)

tk.Label(khungNhap, text="Ma:").grid(row=0, column=0, padx=10, pady=10)
nhapMa = tk.Entry(khungNhap, width=30)
nhapMa.grid(row=0, column=1, padx=10, pady=10)

tk.Label(khungNhap, text="Ten:").grid(row=0, column=2, padx=10, pady=10)
nhapTen = tk.Entry(khungNhap, width=30)
nhapTen.grid(row=0, column=3, padx=10, pady=10)

tk.Label(khungNhap, text="Lop:").grid(row=0, column=4, padx=10, pady=10)
nhapLop = tk.Entry(khungNhap, width=30)
nhapLop.grid(row=0, column=5, padx=10, pady=10)

tk.Label(khungNhap, text="Diem Python:").grid(row=1, column=0, padx=10, pady=10)
nhapPython = tk.Entry(khungNhap, width=30)
nhapPython.grid(row=1, column=1, padx=10, pady=10)

tk.Label(khungNhap, text="Diem CSDL:").grid(row=1, column=2, padx=10, pady=10)
nhapCSDL = tk.Entry(khungNhap, width=30)
nhapCSDL.grid(row=1, column=3, padx=10, pady=10)

tk.Label(khungNhap, text="Diem MMT:").grid(row=1, column=4, padx=10, pady=10)
nhapMMT = tk.Entry(khungNhap, width=30)
nhapMMT.grid(row=1, column=5, padx=10, pady=10)

# Tim kiem
khungTimKiem = tk.Frame(root)
khungTimKiem.pack(padx=10, pady=10)

tk.Label(khungTimKiem, text="Tim kiem:").grid(row=0, column=0, padx=10, pady=10)
nhapTuKhoa = tk.Entry(khungTimKiem, width=30)
nhapTuKhoa.grid(row=0, column=1, padx=10, pady=10)
tk.Button(khungTimKiem, text="Tim kiem", width=10, command=timKiemSinhVien).grid(row=0, column=2, padx=10, pady=10)

# Chuc nang
khungNut = tk.Frame(root)
khungNut.pack(padx=10, pady=10)

tk.Button(khungNut, text="Them", width=10, command=themSinhVien).grid(row=0, column=0, padx=10, pady=10)
tk.Button(khungNut, text="Sua", width=10, command=suaSinhVien).grid(row=0, column=1, padx=10, pady=10)
tk.Button(khungNut, text="Xoa", width=10, command=xoaSinhVien).grid(row=0, column=2, padx=10, pady=10)
tk.Button(khungNut, text="Doc JSON", width=10, command=docJson).grid(row=0, column=3, padx=10, pady=10)
tk.Button(khungNut, text="Luu JSON", width=10, command=luuJson).grid(row=0, column=4, padx=10, pady=10)
tk.Button(khungNut, text="Thong ke", width=10, command=thongKe).grid(row=0, column=5, padx=10, pady=10)

# Bang 
khungBang = tk.LabelFrame(root, text="Danh sach sinh vien")
khungBang.pack(fill="both", expand=True, padx=10, pady=10)

bangSinhVien = ttk.Treeview(khungBang, columns=("Ma", "Ten", "Lop", "Python", "CSDL", "MMT", "DTB", "Loai"), show="headings")

bangSinhVien.heading("Ma", text="Ma sinh vien")
bangSinhVien.heading("Ten", text="Ho ten")
bangSinhVien.heading("Lop", text="Lop")
bangSinhVien.heading("Python", text="Diem Python")
bangSinhVien.heading("CSDL", text="Diem CSDL")
bangSinhVien.heading("MMT", text="Diem MMT")
bangSinhVien.heading("DTB", text="DTB")
bangSinhVien.heading("Loai", text="Loai")

bangSinhVien.column("Ma", width=100, anchor="center")
bangSinhVien.column("Ten", width=170)
bangSinhVien.column("Lop", width=100, anchor="center")
bangSinhVien.column("Python", width=80, anchor="center")
bangSinhVien.column("CSDL", width=80, anchor="center")
bangSinhVien.column("MMT", width=80, anchor="center")
bangSinhVien.column("DTB", width=80, anchor="center")
bangSinhVien.column("Loai", width=100, anchor="center")

# Thanh Cuon
thanhCuon = tk.Scrollbar(khungBang, orient="vertical", command=bangSinhVien.yview)
bangSinhVien.config(yscrollcommand=thanhCuon.set)
thanhCuon.pack(side="right", fill="y")
bangSinhVien.pack(fill="both", expand=True)

# Thong ke
# Thong ke
khungThongKe = tk.LabelFrame(root, text="Thong ke")
khungThongKe.pack(padx=10, pady=10)

bieuDo = tk.Canvas(khungThongKe, width=1100, height=130, bg="white")
bieuDo.pack(padx=10, pady=10)

bangSinhVien.bind("<<TreeviewSelect>>", chonSinhVien)


root.mainloop()

