import tkinter as tk
import tkinter.messagebox as mb

def tinhBMI():
    try:
        canNang = float(nhapCanNang.get())
        chieuCao = float(nhapChieuCao.get())
        
        if canNang <= 0 or chieuCao <= 0:
            mb.showerror("Loi", "Can nang/Chieu cao phai lon hon 0")
            return
        
        bmi = canNang / (chieuCao * chieuCao)
        
        if bmi < 18.5:
            nhanXet = "Gay"
        elif bmi < 25:
            nhanXet = "Binh thuong"
        else:
            nhanXet = "Thua can"
            
        mb.showinfo("Thong bao", f"BMI: {bmi:.2f}\nNhan xet: {nhanXet}")
    
    except ValueError:
        mb.showerror("Loi", "Vui long nhap so hop le!")
        
def lamMoi():
    nhapCanNang.delete(0, tk.END)
    nhapChieuCao.delete(0, tk.END)
    
root = tk.Tk()
root.title("Tinh chi so BMI")
root.geometry("400x300")

tk.Label(root, text="Can nang: ").grid(row=0, column=0, padx=10, pady=10)
nhapCanNang = tk.Entry(root, width=30)
nhapCanNang.grid(row=0, column=1, pady=10)

tk.Label(root, text="Chieu cao: ").grid(row=1, column=0, padx=10, pady=10)
nhapChieuCao = tk.Entry(root, width=30)
nhapChieuCao.grid(row=1, column=1, pady=10)

tk.Button(root, text="Tinh BMI", width=10, command=tinhBMI).grid(row=2, column=0) 
tk.Button(root, text="Lam moi", width=10, command=lamMoi).grid(row=2, column=1)
tk.Button(root, text="Dong", command=root.destroy, width=10).grid(row=2, column=2, pady=10)

root.mainloop()