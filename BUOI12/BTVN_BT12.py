import tkinter as tk
import tkinter.messagebox as mb
from tkinter import ttk

def doiTien():
    try:
        soTien = float(nhapVND.get())
        ngoaiTe = comboNgoaiTe.get()
        
        if soTien <= 0:
            mb.showerror("Loi", "So tien phai lon hon 0!")
            return
        
        if not ngoaiTe:
            mb.showerror("Loi", "Vui long chon ngoai te!")
            return
        
        if ngoaiTe == "USD":
            tyGia = 25000
        elif ngoaiTe == "EUR":
            tyGia = 27000
        else:
            tyGia = 170
        
        ketQua = soTien / tyGia
        
        mb.showinfo("Thong bao", f"So tien sau khi chuyen doi: {ketQua:.2f} {ngoaiTe}")
        
    except ValueError:
        mb.showerror("Loi", "Vui long nhap so tien hop le!")
    

root = tk.Tk()
root.title("Chuyen doi tien te")
root.geometry("400x300")

tk.Label(root, text="NHAP SO TIEN CAN DOI (VND)").pack(pady=10)
nhapVND = tk.Entry(root, width=30)
nhapVND.pack(pady=10)

dsNgoaiTe = ["USD", "EUR", "JPY"]
comboNgoaiTe = ttk.Combobox(root, values=dsNgoaiTe, state="readonly", width=30)
comboNgoaiTe.pack(pady=10)

tk.Button(root, text="Doi", width=10, command=doiTien).pack(pady=10)
tk.Button(root, text="Dong", command=root.destroy, width=10).pack(pady=10)

root.mainloop()