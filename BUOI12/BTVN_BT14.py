import tkinter as tk
import tkinter.messagebox as mb
import json
import os

tenFile = "tasks.json"

def docCongViec():
    if not os.path.exists(tenFile):
        return []
    try:
        with open(tenFile, "r", encoding="utf-8") as f:
            dsCongViec = json.load(f)
        
        if not isinstance(dsCongViec, list):
            raise ValueError
            
        return dsCongViec
    except (OSError, json.JSONDecodeError, ValueError):
        mb.showerror("Loi", "Khong the doc du lieu cong viec!")
        return None
    
def luuCongViec(dsCongViec):
    with open(tenFile, "w", encoding="utf-8") as f:
        json.dump(dsCongViec, f, ensure_ascii=False, indent=4)

def themViec():
    congViec = nhapCongViec.get().strip()
    
    if not congViec:
        mb.showerror("Loi", "Vui long nhap cong viec!")
        return 
    
    # Doc danh sach tu file JSON
    dsCongViec = docCongViec()
    
    if dsCongViec is None:
        return 
    
    # THEM CONG VIEC VAO DANH SACH
    dsCongViec.append(congViec)
    
    # LUU DANH SACH VAO FILE JSON
    luuCongViec(dsCongViec)
    
    listboxTask.insert(tk.END, congViec)
    nhapCongViec.delete(0, tk.END)
    
def hienThiCongViec():
    dsCongViec = docCongViec()
    
    if dsCongViec is None:
        return
    
    for congViec in dsCongViec:
        listboxTask.insert(tk.END, congViec)
        
        
def xoaViec():
    luaChon = listboxTask.curselection()
    
    if not luaChon:
        mb.showerror("Loi", "Vui long chon cong viec!")
        return 
    
    # DOC DANH SACH CONG VIEC TU FILE JSON
    dsCongViec = docCongViec()
    
    if dsCongViec is None:
        return
    
    # XOA CONG VIEC O VI TRI viTri bang pop()
    viTri = luaChon[0]
    dsCongViec.pop(viTri)
    
    # LUU DANH SACH MOI VAO JSON
    luuCongViec(dsCongViec)
    
    listboxTask.delete(luaChon[0])
    
def xoaTatCa():   
    dsCongViec = docCongViec()
    
    if dsCongViec is None:
        return
    
    xacNhan = mb.askyesno("Xac nhan", "Ban co chac chan muon xoa tat ca cong viec!")
    
    
    if not xacNhan:
        return
    
    luuCongViec([])
  
    listboxTask.delete(0, tk.END)
    
root = tk.Tk()
root.title("To-Do List")
root.geometry("450x450")

tk.Label(root, text="Nhap cong viec").pack(padx=10, pady=10)
nhapCongViec = tk.Entry(root, width=30)
nhapCongViec.pack(pady=10)

listboxTask = tk.Listbox(root, width=45,height=10)
listboxTask.pack(pady=10)

tk.Button(root, text="Them viec", width=10, command=themViec).pack(padx=10, pady=10)
tk.Button(root, text="Xoa viec", width=10, command=xoaViec).pack(padx=10, pady=10)
tk.Button(root, text="Xoa tat ca", width=10, command=xoaTatCa).pack(padx=10, pady=10)
tk.Button(root, text="Dong", width=10, command=root.destroy).pack(padx=10, pady=10)

hienThiCongViec()

root.mainloop()
