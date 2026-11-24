# -----------------------------------------------------------------------------
# Yêu cầu đề bài
# - Nhập hai số bằng Entry.
# - Có bốn nút Cộng, Trừ, Nhân, Chia.
# - Hiển thị kết quả trong Label.
# - Dùng try/except xử lý nhập sai và phép chia cho 0.
# -----------------------------------------------------------------------------
import tkinter as tk
import tkinter.messagebox as mb

def tinhCong():
    try:
        a = float(nhapSoThuNhat.get())
        b = float(nhapSoThuHai.get())
        
        ketQua = a + b
        
        nhanKetQua.config(text=f"Ket qua: {ketQua}")
        
    except ValueError:
        mb.showerror("Loi", "Vui long nhap so hop le!")
        
def tinhTru():
    try:
        a = float(nhapSoThuNhat.get())
        b = float(nhapSoThuHai.get())
        
        ketQua = a - b
        
        nhanKetQua.config(text=f"Ket qua: {ketQua}")
        
    except ValueError:
        mb.showerror("Loi", "Vui long nhap so hop le!")
        
def tinhNhan():
    try:
        a = float(nhapSoThuNhat.get())
        b = float(nhapSoThuHai.get())
        
        ketQua = a * b
        
        nhanKetQua.config(text=f"Ket qua: {ketQua}")
        
    except ValueError:
        mb.showerror("Loi", "Vui long nhap so hop le!")
        
def tinhChia():
    try:
        a = float(nhapSoThuNhat.get())
        b = float(nhapSoThuHai.get())
        
        if b == 0:
            mb.showerror("Loi", "Khong the chia cho 0! Vui long nhap so khac!")
            return
        
        ketQua = a / b
        
        nhanKetQua.config(text=f"Ket qua: {ketQua}")
        
    except ValueError:
        mb.showerror("Loi", "Vui long nhap so hop le!")
    
    

root = tk.Tk()
root.title("May tinh hai so")
root.geometry("600x450")

tk.Label(root, text="MAY TINH HAI SO").grid(row=0, column=0, columnspan=2, sticky="nsew", pady=15)
tk.Label(root, text="So thu nhat:").grid(row=1, column=0, pady=10)
nhapSoThuNhat = tk.Entry(root, width=30)
nhapSoThuNhat.grid(row=1, column=1)

tk.Label(root, text="So thu hai:").grid(row=2, column=0, pady=10)
nhapSoThuHai = tk.Entry(root, width=30)
nhapSoThuHai.grid(row=2, column=1)

khungPhepTinh = tk.Frame(root)
khungPhepTinh.grid(row=3, column=0, columnspan=2, pady=15)

tk.Button(khungPhepTinh, text="+", command=tinhCong).grid(row=0, column=0, padx=5)
tk.Button(khungPhepTinh, text="-", command=tinhTru).grid(row=0, column=1, padx=5)
tk.Button(khungPhepTinh, text="*", command=tinhNhan).grid(row=0, column=2, padx=5)
tk.Button(khungPhepTinh, text="/", command=tinhChia).grid(row=0, column=3, padx=5)

nhanKetQua = tk.Label(root, text="Ket qua: ", font=("Arial", 14))
nhanKetQua.grid(row=4, column=0, columnspan=2, pady=15)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

root.mainloop()