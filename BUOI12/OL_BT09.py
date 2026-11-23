import tkinter as tk
import tkinter.messagebox as mb

def xemLuaChon():
    luaChon = listbox.curselection()
    dsTraiCay = []
    
    for index in luaChon:
        dsTraiCay.append(listbox.get(index))
        
    if not dsTraiCay:
        mb.showerror("Loi", "Vui long chon it nhat 1 loai trai cay!")
    else:
        mb.showinfo("Thong bao", f"Trai cay da lua chon: {', '.join(dsTraiCay)}")

def xoaLuaChon():
    listbox.select_clear(0, tk.END)
    
root = tk.Tk()
root.title("Chon trai cay yeu thich")
root.geometry("400x300")

listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
listbox.pack(pady=8)

# THEM MOT LOAI TRAI CAY
listbox.insert(tk.END, "Tao")
listbox.insert(tk.END, "Cam")
listbox.insert(tk.END, "Xoai")
listbox.insert(tk.END, "Chuoi")
listbox.insert(tk.END, "Dua hau")

tk.Button(root, text="Xem lua chon", command=xemLuaChon).pack(pady=5)
tk.Button(root, text="Xoa lua chon", command=xoaLuaChon).pack(pady=5)
tk.Button(root, text="Dong", command=root.destroy).pack(pady=5)

root.mainloop()