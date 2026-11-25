import tkinter as tk 
import tkinter.messagebox as mb

def themCongViec():
    congViec = nhapCongViec.get().strip()
    
    if not congViec:
        mb.showerror("Loi", "Vui long nhap cong viec!")
        return
    
    for cv in bangCongViec.get(0, tk.END):
        if cv[4:].lower() == congViec.lower():
            mb.showerror("Loi", "Cong viec da ton tai!")
            return
        
    bangCongViec.insert(tk.END, "[ ] " + congViec)
    nhapCongViec.delete(0, tk.END)
    
    mb.showinfo("Thong bao", "Them thanh cong!")
    
def xoaCongViec():
    luaChon = bangCongViec.curselection()
    
    if not luaChon:
        mb.showerror("Loi", "Vui long chon cong viec!")
        return
    
    if mb.askyesno("Xac nhan", "Ban co chac muon xoa!"):
        bangCongViec.delete(luaChon[0])
        mb.showinfo("Thong bao", "Xoa thanh cong!")
        
def hoanThanh():
    luaChon = bangCongViec.curselection()
    
    if not luaChon:
        mb.showerror("Loi", "Vui long chon cong viec!")
        return
    
    viTri = luaChon[0]
    congViec = bangCongViec.get(viTri)
        
    bangCongViec.delete(viTri)
    bangCongViec.insert(viTri, "[X] " + congViec[4:])
        
        

root = tk.Tk()
root.title("Quan ly cong viec")
root.geometry("800x400")

khungNhap = tk.Frame(root)
khungNhap.pack(pady=10)

tk.Label(khungNhap, text="Cong viec:").grid(row=0, column=0, padx=10, pady=10)
nhapCongViec = tk.Entry(khungNhap, width=30)
nhapCongViec.grid(row=0, column=1, padx=10, pady=10)

khungNut = tk.Frame(root)
khungNut.pack(pady=10)

tk.Button(khungNut, text="Them", width=10, command=themCongViec).grid(row=0, column=0, padx=10)
tk.Button(khungNut, text="Xoa", width=10, command=xoaCongViec).grid(row=0, column=1, padx=10)
tk.Button(khungNut, text="Hoan thanh", width=10, command=hoanThanh).grid(row=0, column=2, padx=10)

khungDanhSach = tk.LabelFrame(root, text="Danh sach cong viec")
khungDanhSach.pack(anchor="center", pady=10)

bangCongViec = tk.Listbox(khungDanhSach, width=50, height=12)
bangCongViec.pack(pady=10)

root.mainloop()