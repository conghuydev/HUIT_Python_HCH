import tkinter as tk
import tkinter.messagebox as mb

def dangNhap():
    tenDangNhap = nhapTenDangNhap.get().strip()
    matKhau = nhapMatKhau.get()
    
    if not tenDangNhap or not matKhau:
        mb.showerror("Loi", "Vui llong nhap pday du thong tin!")
        return

    mb.showinfo("Thong bao", "Dang nhap thanh cong!")
    
root = tk.Tk()
root.title("Bieu mau dang nhap")
root.geometry("400x350")

tk.Label(root, text="DANG NHAP").grid(row=0, column=0, columnspan=2, sticky="ew", pady=15)

tk.Label(root, text="Ten dang nhap:").grid(row=1, column=0, padx=15, pady=15)
nhapTenDangNhap = tk.Entry(root, width=30)
nhapTenDangNhap.grid(row=1, column=1)

tk.Label(root, text="Mat khau:").grid(row=2, column=0, padx=15, pady=15)
nhapMatKhau = tk.Entry(root, width=30, show="*")
nhapMatKhau.grid(row=2, column=1)

tk.Button(root, text="Dang nhap", command=dangNhap).grid(row=3, column=0, columnspan=2, pady=15)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.mainloop()