import tkinter as tk
import tkinter.messagebox as mb
from tkinter import ttk
import json
import re

tenFile = "taikhoan.json"

def xoaTrang():
    nhapHoTen.delete(0, tk.END)
    nhapTaiKhoan.delete(0, tk.END)
    nhapEmail.delete(0, tk.END)
    nhapSDT.delete(0, tk.END)
    nhapMatKhau.delete(0, tk.END)
    nhapXacNhan.delete(0, tk.END)
    
    gioiTinh.set("Nam")
    nhapQueQuan.current(0)
    
    docSach.set(0)
    theThao.set(0)
    amNhac.set(0)
    dongY.set(0)
    
def dangKy():
    hoTen = nhapHoTen.get().strip()
    taiKhoan = nhapTaiKhoan.get().strip()
    email = nhapEmail.get().strip()
    sdt = nhapSDT.get().strip()
    matKhau = nhapMatKhau.get()
    xacNhan = nhapXacNhan.get()
    gt = gioiTinh.get() # Radiobutton
    queQuan = nhapQueQuan.get()
    
    # Kiểm tra dữ liệu
    if not hoTen or not taiKhoan or not email or not sdt or not matKhau or not xacNhan:
        mb.showerror("Loi", "Vui long nhap day du!")
        return
    
    if re.search(r"\s", taiKhoan):
        mb.showerror("Loi", "Tai khoan khong duoc chua khoang trang!")
        return
    
    pattern = r"[^@\s]+@[^@\s]+\.[^@\s]+"
    if re.fullmatch(pattern, email):
        mb.showerror("Loi", "Email khong hop le!")
        return
    
    if re.fullmatch(r"[^0-9]{9}", sdt):
        mb.showerror("Loi", "SDT khong hop le!")
        return
    
    if len(matKhau) < 6:
        mb.showerror("Loi", "Mat khau phai co it nhat 6 ky tu!")
        return
    
    if matKhau != xacNhan:
        mb.showerror("Loi", "Mat khau khong khop!")
        return
    
    if dongY.get() == 0:
        mb.showerror("Loi", "Ban chua dong y dieu khoan!")
        return
    
    # Lấy sở thích
    soThich = []

    if docSach.get() == 1:
        soThich.append("Doc sach")

    if theThao.get() == 1:
        soThich.append("The thao")

    if amNhac.get() == 1:
        soThich.append("Am nhac")
        
    # Đọc danh sách tài khoản cũ
    try:
        with open(tenFile, "r", encoding="utf-8") as f:
            danhSachTaiKhoan = json.load(f)

    except FileNotFoundError:
        danhSachTaiKhoan = []

    except (OSError, json.JSONDecodeError):
        mb.showerror("Loi", "Khong the doc file!")
        return
    
    # Kiểm tra trùng tài khoản
    for item in danhSachTaiKhoan:
        if item["taiKhoan"].lower() == taiKhoan.lower():
            mb.showerror("Loi", "Tai khoan da ton tai!")
            return
        
    # Tạo tài khoản mới
    taiKhoanMoi = {
        "hoTen": hoTen,
        "taiKhoan": taiKhoan,
        "email": email,
        "sdt": sdt,
        "gioiTinh": gt,
        "queQuan": queQuan,
        "soThich": soThich
    }

    danhSachTaiKhoan.append(taiKhoanMoi)
    
    # Lưu JSON
    try:
        with open(tenFile, "w", encoding="utf-8") as f:
            json.dump(danhSachTaiKhoan, f, ensure_ascii=False, indent=4)
    
        mb.showinfo("Thong bao", "Dang ky thanh cong!")
        xoaTrang()
    
    except OSError:
        mb.showerror("Loi", "Luu file that bai!")   

def docJson():
    try:
        with open(tenFile, "r", encoding="utf-8") as f:
            danhSachTaiKhoan = json.load(f)

        noiDung = ""

        for item in danhSachTaiKhoan:
            noiDung += f"Ho ten: {item['hoTen']}\n"
            noiDung += f"Tai khoan: {item['taiKhoan']}\n"
            noiDung += f"Email: {item['email']}\n"
            noiDung += f"SDT: {item['sdt']}\n"
            noiDung += f"Gioi tinh: {item['gioiTinh']}\n"
            noiDung += f"Que quan: {item['queQuan']}\n"
            noiDung += f"So thich: {', '.join(item['soThich'])}\n"
            noiDung += "---------------------------\n"

        if not noiDung:
            noiDung = "Chua co tai khoan!"

        mb.showinfo("Danh sach tai khoan", noiDung)

    except FileNotFoundError:
        mb.showerror("Loi", "Khong tim thay file!")

    except (OSError, json.JSONDecodeError):
        mb.showerror("Loi", "Doc file that bai!") 
        
root = tk.Tk()
root.title("Dang ky tai khoan")
root.geometry("700x650")

tk.Label(
    root,
    text="DANG KY TAI KHOAN",
    font=("Arial", 20, "bold")
).pack(pady=15)

# Thông tin tài khoản
khungNhap = tk.LabelFrame(root, text="Thong tin tai khoan")
khungNhap.pack(padx=10, pady=10)

tk.Label(khungNhap, text="Ho ten:").grid(
    row=0, column=0, padx=10, pady=5, sticky="w"
)
nhapHoTen = tk.Entry(khungNhap, width=35)
nhapHoTen.grid(row=0, column=1, padx=10, pady=5)

tk.Label(khungNhap, text="Tai khoan:").grid(
    row=1, column=0, padx=10, pady=5, sticky="w"
)
nhapTaiKhoan = tk.Entry(khungNhap, width=35)
nhapTaiKhoan.grid(row=1, column=1, padx=10, pady=5)

tk.Label(khungNhap, text="Email:").grid(
    row=2, column=0, padx=10, pady=5, sticky="w"
)
nhapEmail = tk.Entry(khungNhap, width=35)
nhapEmail.grid(row=2, column=1, padx=10, pady=5)

tk.Label(khungNhap, text="So dien thoai:").grid(
    row=3, column=0, padx=10, pady=5, sticky="w"
)
nhapSDT = tk.Entry(khungNhap, width=35)
nhapSDT.grid(row=3, column=1, padx=10, pady=5)

tk.Label(khungNhap, text="Mat khau:").grid(
    row=4, column=0, padx=10, pady=5, sticky="w"
)
nhapMatKhau = tk.Entry(khungNhap, width=35, show="*")
nhapMatKhau.grid(row=4, column=1, padx=10, pady=5)

tk.Label(khungNhap, text="Xac nhan mat khau:").grid(
    row=5, column=0, padx=10, pady=5, sticky="w"
)
nhapXacNhan = tk.Entry(khungNhap, width=35, show="*")
nhapXacNhan.grid(row=5, column=1, padx=10, pady=5)

# Radiobutton
tk.Label(khungNhap, text="Gioi tinh").grid(row=6, column=0, padx=10, pady=5, sticky="w")

khungGioiTinh = tk.Frame(khungNhap)
khungGioiTinh.grid(row=6, column=1, sticky="w")

gioiTinh = tk.SringVar(value="Nam")

tk.Radiobutton(khungGioiTinh, text="Nam", variable=gioiTinh, value="Nam").pack(side="left")
tk.Radiobutton(khungGioiTinh, text="Nu", variable=gioiTinh, value="Nu").pack(side="left")

# Combobox
tk.Label(khungNhap, text="Que quan:").grid(row=17, column=0, padx=10, pady=5, sticky="w")

nhapQueQuan = ttk.Combobox(khungNhap, values=["TH.HCM","Ha Noi", "Da Nang", "Khac"], state="readonly", width=32)
#     row=7, column=0, padx=10, pady=5, sticky="w"
# )
nhapQueQuan.grid(row=7, column=1, padx=10, pady=5)
nhapQueQuan.current(0)

# Checkbutton
tk.Label(khungNhap, text="So thich:").grid(
    row=8, column=0, padx=10, pady=5, sticky="w"
)

khungSoThich = tk.Frame(khungNhap)
khungSoThich.grid(row=8, column=1, sticky="w")

docSach = tk.IntVar(value=0)
theThao = tk.IntVar(value=0)
amNhac = tk.IntVar(value=0)

tk.Checkbutton(
    khungSoThich, text="Doc sach", variable=docSach
).pack(side="left")

tk.Checkbutton(
    khungSoThich, text="The thao", variable=theThao
).pack(side="left")

tk.Checkbutton(
    khungSoThich, text="Am nhac", variable=amNhac
).pack(side="left")

# Điều khoản
dongY = tk.IntVar(value=0)

tk.Checkbutton(
    root,
    text="Toi dong y voi dieu khoan su dung",
    variable=dongY
).pack(pady=10)

# Chức năng
khungNut = tk.Frame(root)
khungNut.pack(pady=10)

tk.Button(
    khungNut, text="Dang ky",
    width=15, command=dangKy
).grid(row=0, column=0, padx=10)

tk.Button(
    khungNut, text="Xoa trang",
    width=15, command=xoaTrang
).grid(row=0, column=1, padx=10)

tk.Button(
    khungNut, text="Doc JSON",
    width=15, command=docJson
).grid(row=0, column=2, padx=10)

root.mainloop()