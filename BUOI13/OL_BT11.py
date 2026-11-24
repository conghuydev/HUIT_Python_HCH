# -----------------------------------------------------------------------------
# Chia cửa sổ thành 3 vùng: Tiêu đề, Nội dung và Nút chức năng.
# Mỗi vùng sử dụng phương thức bố trí phù hợp.
# Không trộn pack() và grid() trong cùng một vùng chứa.
# -----------------------------------------------------------------------------
import tkinter as tk
import tkinter.messagebox as mb

def luuThongTin():
    ten = nhapHoTen.get().strip()
    lop = nhapLop.get().strip()
    
    if not ten or not lop:
        mb.showerror("Lỗi", "Vui lòng nhập đầy đủ họ tên và lớp!")
        return
    
    mb.showinfo("Thông báo", "Đã lưu thông tin thành công!")

def thoat():
    xacNhan = mb.askyesno("Xác nhận", "Bạn có chắc chắn muốn thoát không?")
    root.destroy()
    
root = tk.Tk()
root.title("Frame và LabelFrame trong Tkinter")
root.geometry("500x400")

KhungTieuDe = tk.Frame(root)
KhungTieuDe.pack(fill="x", padx=10, pady=10)

tk.Label(KhungTieuDe, text="THÔNG TIN SINH VIÊN", font=("Arial", 16, "bold")).pack()

khungNoiDung = tk.LabelFrame(root, text="Thông tin cá nhân", font=("Arial", 10, "bold"))
khungNoiDung.pack(fill="x", padx=10, pady=10)

tk.Label(khungNoiDung, text="Họ tên:").grid(row=0, column=0)
nhapHoTen = tk.Entry(khungNoiDung, width=40)
nhapHoTen.grid(row=0,column=1,padx=10, pady=10)

tk.Label(khungNoiDung, text="Lớp:").grid(row=1, column=0)
nhapLop = tk.Entry(khungNoiDung, width=40)
nhapLop.grid(row=1,column=1,padx=10, pady=10)


khungNut = tk.Frame(root)
khungNut.pack(pady=15)

tk.Button(khungNut, text="Lưu", command=luuThongTin).pack(side="left", padx=5, pady=5)
tk.Button(khungNut, text="Thoát", command=thoat).pack(side="left", padx=5, pady=5)

root.mainloop()