import tkinter as tk
import tkinter.messagebox as mb
from tkinter import ttk

def tinhTien():
    try:
        tongTienHD = float(nhapTongTien.get())
        soNguoiChia = int(nhapSoNguoiChia.get())
        tips = comboTip.get()
        
        if tongTienHD <= 0 or soNguoiChia <= 0:
            mb.showerror("Loi", "Tong tien/So nguoi chia phai lon hon 0!")
            return 
        
        if not tips:
            mb.showerror("Loi", "Vui long chon tip!")
            return
        
        if tips == "0%":
            tip = 0
        elif tips == "5%":
            tip = 5 
        elif tips == "10%":
            tip = 10
        else:
            tip = 15
        
        tongTien = tongTienHD + tongTienHD * (tip /100 )
        tienMoiNguoi = tongTien / soNguoiChia
        
        mb.showinfo("Thong bao", f"Tong tien: {tongTien:.2f}\nSo tien moi nguoi: {tienMoiNguoi:.2f}")
        
    except ValueError:
        mb.showerror("Loi", "Vui long nhap so hop le!")
        
            
root = tk.Tk()
root.title("Chia tien an uong")
root.geometry("400x350")

tk.Label(root, text="Tong tien hoa don:").pack(pady=10)
nhapTongTien = tk.Entry(root, width=30)
nhapTongTien.pack(pady=10)

tk.Label(root, text="Tong so nguoi chia:").pack(pady=10)
nhapSoNguoiChia = tk.Entry(root, width=30)
nhapSoNguoiChia.pack(pady=10)

dsTip = ["0%", "5%", "10%", "15%"]
comboTip = ttk.Combobox(root, values=dsTip, state="readonly")
comboTip.pack(pady=10)

tk.Button(root, text="Tinh tien", command=tinhTien).pack(pady=10)
tk.Button(root, text="Dong", command=root.destroy).pack(pady=10)
root.mainloop()

