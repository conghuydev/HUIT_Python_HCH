import tkinter as tk
import tkinter.messagebox as mb

# Hien thi cac mon da chon
def confirm():
    subjects = []
    
    if varPython.get():
        subjects.append("Python")
        
    if varJava.get():
        subjects.append("Java")
        
    if varCpp.get():
        subjects.append("C++")
        
    if varWeb.get():
        subjects.append("Web")
        
    if not subjects:
        mb.showerror("Loi", "Vui long chon  it nhat 1 mon hoc!")
    else:
        mb.showinfo("Thong bao", f"Cac mon hoc yeu thich: {', '.join(subjects)}")
        
# Nhap lai
def reset():
    varPython.set(False)
    varJava.set(False)
    varCpp.set(False)
    varWeb.set(False)
    
root = tk.Tk()
root.title("Chon mon hoc yeu thich")
root.geometry("400x350")

tk.Label(root, text="Chon mon hoc yeu thich", font=("Arial", 15, "bold")).pack(pady=15)

varPython = tk.BooleanVar()
varJava = tk.BooleanVar()
varCpp = tk.BooleanVar()
varWeb = tk.BooleanVar()

tk.Checkbutton(root, text="Python", variable=varPython).pack(pady=5)
tk.Checkbutton(root, text="Java", variable=varJava).pack(pady=5)
tk.Checkbutton(root, text="C++", variable=varCpp).pack(pady=5)
tk.Checkbutton(root, text="Web", variable=varWeb).pack(pady=5)

tk.Button(root, text="Xac nhan", command=confirm).pack(pady=5)

tk.Button(root, text="Nhap lai", command=reset).pack(pady=5)

tk.Button(root, text="Dong", command=root.destroy).pack(pady=5)

root.mainloop()

