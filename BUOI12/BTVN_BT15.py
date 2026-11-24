import tkinter as tk
import tkinter.messagebox as mb
import random
import string

def taoMatKhau():
    try:
        doDai = int(nhapDoDai.get())
        
        if doDai <= 0:
            mb.showerror("Loi", "Do dai mat khau phai lon hon 0!")
            return
        
        kyTu = string.ascii_lowercase
        
        if chonSo.get():
            kyTu += string.digits
            
        if chonChuHoa.get():
            kyTu += string.ascii_uppercase
            
        if chonKyTuDacBiet.get():
            kyTu += "!@#$%" 
            
        matKhau = ""
        
        for i in range(doDai):
            # Chon mot ky tu ngau nhien
            chonKyTu = random.choice(kyTu)
            
            # Ghep ky tu do vao matKhau
            matKhau += chonKyTu
            
        # Xoa mat khau cu
        hienThiMatKhau.delete(0, tk.END)
        
        # Hien thi mat khau moi
        hienThiMatKhau.insert(tk.END, matKhau)
            
    except ValueError:
        mb.showerror("Loi", "Vui long nhap do dai hop le!")
        return
    
def saoChep():
    matKhau = hienThiMatKhau.get()
    
    if not matKhau:
        mb.showerror("Loi", "Vui long nhap mat khau truoc!")
        return
    
    # Xoa clipboard cu
    root.clipboard_clear()
    
    # Sao chep mat khau vao cliboard
    root.clipboard_append(matKhau)
    
    mb.showinfo("Thong bao", "Sao chep mat khau thanh cong!")


root = tk.Tk()
root.title("Nhap mat khau")
root.geometry("400x400")

tk.Label(root, text="Do dai mat khau:").pack(pady=5)

nhapDoDai = tk.Entry(root, width=30)
nhapDoDai.pack(pady=5)

nhapDoDai.insert(0, "8")

chonSo = tk.BooleanVar()
chonChuHoa = tk.BooleanVar()
chonKyTuDacBiet = tk.BooleanVar()

tk.Checkbutton(root, text="Bao gom chu so (0-9)", variable=chonSo).pack(pady=5)
tk.Checkbutton(root, text="Bao gom chu hoa (A-Z)", variable=chonChuHoa).pack(pady=5)
tk.Checkbutton(root, text="Bao gom ky tu dac biet", variable=chonKyTuDacBiet).pack(pady=5)

tk.Label(root, text="Mat khau duoc tao").pack(pady=5)
hienThiMatKhau = tk.Entry(root, width=30)
hienThiMatKhau.pack(pady=5)

tk.Button(root, text="Tao mat khau", command=taoMatKhau).pack(pady=5)
tk.Button(root, text="Sao chep", command=saoChep).pack(pady=5)
tk.Button(root, text="Dong", command=root.destroy).pack(pady=5)

root.mainloop()
