# Bài 3 — Thanh công cụ (Toolbar)
# Yêu cầu đề bài
# Tạo thanh công cụ gồm 5 nút:
# - Mới
# - Mở
# - Lưu
# - Xóa
# - Thoát
# Mỗi nút phải gọi một hàm xử lý riêng. Nút Thoát cần có hộp thoại xác nhận.
#----------------------------------------------------------------------------
import tkinter as tk
import tkinter.messagebox as mb

def thoat():
    xacNhan = mb.askyesno("Xac nhan", "Ban co muon thoat khong?")
    
    if xacNhan:
        root.destroy()

def taoMoi():
    mb.showinfo("Thong bao", "Da tao moi!")
    
def moFile():
    mb.showinfo("Thong bao", "Da mo file!")
    
def luuFile():
    mb.showinfo("Thong bao", "Da luu file!")
    
def xoa():
    mb.showinfo("Thong bao", "Da xoa!")

root = tk.Tk()
root.title("Thanh cong cu")
root.geometry("500x300")

thanhCongCu = tk.Frame(root)
thanhCongCu.pack(side="top", fill="x")

tk.Button(thanhCongCu, text="New", command=taoMoi).pack(side="left", padx=5, pady=5)
tk.Button(thanhCongCu, text="Open", command=moFile).pack(side="left", padx=5, pady=5)
tk.Button(thanhCongCu, text="Save", command=luuFile).pack(side="left", padx=5, pady=5)
tk.Button(thanhCongCu, text="Delete", command=xoa).pack(side="left", padx=5, pady=5)
tk.Button(thanhCongCu, text="Exit", command=thoat).pack(side="left", padx=5, pady=5)

root.mainloop()