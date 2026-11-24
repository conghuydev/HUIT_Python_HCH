# -----------------------------------------------------------------------------
# Tạo biểu mẫu gồm:
# - Radiobutton: Chọn giới tính.
# - Checkbutton: Chọn sở thích.
# - Combobox: Chọn lớp.
# - Button: Hiển thị tổng hợp thông tin đã chọn bằng messagebox.
# -----------------------------------------------------------------------------
import tkinter as tk
import tkinter.messagebox as mb
from tkinter import ttk

def hienThiThongTin():
    gt = gioiTinh.get()
    lop = chonLop.get()
    
    if not gt or not lop:
        mb.showerror("Loi", "Vui long chon day du thong tin!")
        return
    
    dsSoThich = []
    
    if chonDocSach.get():
        dsSoThich.append("Doc sach")
    elif chonNgheNhac.get():
        dsSoThich.append("Nghe nhac")
    elif chonTheThao.get():
        dsSoThich.append("The thao")
    else:
        dsSoThich.append("Khong co")
        
     
    mb.showinfo("Thong bao", f"Gioi tinh: {gt}\nLop: {lop}\nSo thich: {', '.join(dsSoThich)}")
    
root = tk.Tk()
root.title("Bieu mau chon thong tin")
root.geometry("500x450")

tk.Label(root, text="BIEU MAU THONG TIN").pack(pady=10)
nhanGioiTinh = tk.Label(root, text="Gioi tinh")
nhanGioiTinh.pack(pady=10)

gioiTinh = tk.StringVar(value="")
tk.Radiobutton(root, text="Nam", variable=gioiTinh, value="Nam").pack()
tk.Radiobutton(root, text="Nu", variable=gioiTinh, value="Nu").pack()
tk.Radiobutton(root, text="Khac", variable=gioiTinh, value="Khac").pack()

nhanSoThich = tk.Label(root, text="So thich")
nhanSoThich.pack(pady=10)
chonDocSach = tk.BooleanVar()
tk.Checkbutton(root, text="Doc sach", variable=chonDocSach).pack()
chonNgheNhac = tk.BooleanVar()
tk.Checkbutton(root, text="Nghe nhac", variable=chonNgheNhac).pack()
chonTheThao = tk.BooleanVar()
tk.Checkbutton(root, text="The thao", variable=chonTheThao).pack()

nhanLop = tk.Label(root, text="Lop")
nhanLop.pack(pady=10)
chonLop = ttk.Combobox(root, values=["16DHTH01", "16DHTH02", "16DHTH08"], state="readonly")
chonLop.pack()

tk.Button(root, text="Hien thi thong tin", command=hienThiThongTin).pack(pady=10)

root.mainloop()