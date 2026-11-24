# -----------------------------------------------------------------------------
# - Đếm số lần người dùng nhấp chuột.
# - Hiển thị phím vừa được nhấn.
# - Có nút Đặt lại bộ đếm.
# - Sử dụng phương thức bind()
# -----------------------------------------------------------------------------

import tkinter as tk
soLanClick = 0

def xuLyChuot(event):
    global soLanClick   
    soLanClick += 1   
    nhanSoLanClick.config(text=f"Số lần nhấp chuột: {soLanClick}")
    
def xuLyPhim(event):
    phim = event.keysym
    nhanPhim.config(text=f"Phím vừa nhấn: {phim}")
    
def datLaiBoDem():
    global soLanClick
    
    soLanClick = 0
    nhanSoLanClick.config(text="Số lần nhấp chuột: 0")
    nhanPhim.config(text="Phím vừa nhấn: Chưa có")
    
root = tk.Tk()
root.title("Su kien chuot va ban phim")
root.geometry("500x350")

nhanTieuDe = tk.Label(root, text="SƯ KIỆN CHUỘT VÀ BÀN PHÍM", font=("Arial", 16, "bold"))
nhanTieuDe.pack(pady=5)

nhanSoLanClick = tk.Label(root, text="Số lần nhấp chuột: 0")
nhanSoLanClick.pack(pady=5)

nhanPhim = tk.Label(root, text="Phím vừa nhấn: Chưa có")
nhanPhim.pack(pady=5)

tk.Button(root, text="Đặt lại bộ đếm", command=datLaiBoDem).pack(pady=5)

root.bind("<Button-1>", xuLyChuot)
root.bind("<KeyPress>", xuLyPhim)

root.mainloop()