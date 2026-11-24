# -----------------------------------------------------------------------------
# Thêm phần tử vào Listbox từ ô nhập Entry.
# Xóa phần tử đã chọn.
# Có thanh cuộn Scrollbar.
# Không cho phép thêm giá trị rỗng hoặc trùng lặp.
# -----------------------------------------------------------------------------
import tkinter as tk
import tkinter.messagebox as mb

def themPhanTu():
    phanTu = nhapPhanTu.get().strip()
    
    dsPhanTu = danhSach.get(0, tk.END)
    
    if not phanTu:
        mb.showerror("Loi", "Vui long nhap phan tu!")
        return
    
    if phanTu in dsPhanTu:
        mb.showerror("Loi", "Phan tu da ton tai!")
        return
        
    danhSach.insert(tk.END, phanTu)
    nhapPhanTu.delete(0, tk.END)
    
def xoaPhanTu():
    viTri = danhSach.curselection()
    
    if not viTri:
        mb.showerror("Loi", "Vui long chon phan tu!")
        return
    
    danhSach.delete(viTri[0])
    
root = tk.Tk()
root.title("Qua ly danh sach")
root.geometry("500x450")


tk.Label(root, text="Quan ly danh sach").pack(pady=10)

khungNhapPhanTu= tk.Frame(root)
khungNhapPhanTu.pack(pady=10)

tk.Label(khungNhapPhanTu, text="Nhap phan tu").grid(row=0, column=0, padx=5, pady=5)

nhapPhanTu = tk.Entry(khungNhapPhanTu, width=30)
nhapPhanTu.grid(row=1, column=0)

khungNut = tk.Frame(root)
khungNut.pack(pady=10)

tk.Button(khungNut, text="Them", width=10, command=themPhanTu).pack(side="left", padx=5)
tk.Button(khungNut, text="Xoa", width=10, command=xoaPhanTu).pack(side="left", padx=5)

khungDanhSach = tk.Frame(root)
khungDanhSach.pack(pady=10)

danhSach = tk.Listbox(khungDanhSach, width=35, height=10)
danhSach.pack(side="left")

thanhCuon = tk.Scrollbar(khungDanhSach)
thanhCuon.pack(side="right", fill="y")

danhSach.config(yscrollcommand=thanhCuon.set)
thanhCuon.config(command=danhSach.yview)

root.mainloop()