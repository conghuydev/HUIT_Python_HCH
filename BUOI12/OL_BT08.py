import tkinter as tk
import tkinter.messagebox as mb

def confirm():
    selected = gender.get()
    
    if not selected:
        mb.showerror("Loi", "Vui long chon gioi tinh!")
    else:
        mb.showinfo("Thong bao", f"Gioi tinh da chon: {selected}")
        
def reset():
    gender.set("")  # Bo chon cac RadioButton
    

root = tk.Tk()
root.title("Chon gioi tinh")
root.geometry("400x300")

tk.Label(root, text="Chon gioi tinh").pack(pady=15)

gender = tk.StringVar(value="") # Ban dau chua chon gioi tinh nao

tk.Radiobutton(root, text="Nam", variable=gender, value="Nam").pack(pady=5)
tk.Radiobutton(root, text="Nu", variable=gender, value="Nu").pack(pady=5)
tk.Radiobutton(root, text="Khac", variable=gender, value="Khac").pack(pady=5)

tk.Button(root, text="Xac nhan", command=confirm).pack(pady=5)

tk.Button(root, text="Nhap lai", command=reset).pack(pady=5)

tk.Button(root, text="Dong", command=root.destroy).pack(pady=5)
root.mainloop()