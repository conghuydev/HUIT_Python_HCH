#----------------------------------------------------------------------------
# Yêu cầu đề bài:Tạo thanh MenuBar gồm ba menu chính: File, Edit, Help.
#----------------------------------------------------------------------------
import tkinter as tk
import tkinter.messagebox as mb

def thoat():
    xacNhan = mb.askyesno("Xac nhan", "Ban co muon thoat khong!")
    
    if xacNhan:
        root.destroy()
        
def taoMoi():
    mb.showinfo("Thong bao", "Da tao moi!")
    
def moFile():
    mb.showinfo("Thong bao", "Da mo file!")
    
def luuFile():
    mb.showinfo("Thong bao", "Da luu file!")
    
def gioiThieu():
    mb.showinfo("Thong bao", "Day la ung dung!")
    
def copy():
    mb.showinfo("Thong bao", "Da sao chep!")
    
def paste():
    mb.showinfo("Thong bao", "Da dan!")

root = tk.Tk()
root.title("Menu co ban")
root.geometry("500x350")

menuBar = tk.Menu(root)

menuFile = tk.Menu(menuBar, tearoff=0)
menuFile.add_command(label="New", command=taoMoi)
menuFile.add_command(label="Open", command=moFile)
menuFile.add_command(label="Save", command=luuFile)
menuFile.add_separator()
menuFile.add_command(label="Exit", command=thoat)

menuEdit = tk.Menu(menuBar, tearoff=0)
menuEdit.add_command(label="Copy", command=copy)
menuEdit.add_command(label="Paste", command=paste)

menuHelp = tk.Menu(menuBar, tearoff=0)
menuHelp.add_command(label="About", command=gioiThieu)

menuBar.add_cascade(label="File", menu=menuFile)
menuBar.add_cascade(label="Edit", menu=menuEdit)
menuBar.add_cascade(label="Help", menu=menuHelp)

root.config(menu=menuBar)

root.mainloop()