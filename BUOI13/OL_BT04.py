#----------------------------------------------------------------------------
# Yêu cầu đề bài
# - Đặt một Label ở chính giữa cửa sổ bằng relx, rely và anchor.
# - Đặt hai Button ở hai góc dưới của cửa sổ.
#----------------------------------------------------------------------------
import tkinter as tk

root = tk.Tk()
root.title("Dinh vi bang place")
root.geometry("500x350")

tk.Label(root, text="Hello").place(relx=0.5, rely=0.5, anchor="center")
tk.Button(root, text="Button trai").place(relx=0, rely=1, anchor="sw", x=10, y=-10)
tk.Button(root, text="Button phai").place(relx=1, rely=1, anchor="se", x=-10, y=-10)
root.mainloop()


# --------------------------------NOTE------------------------------------
# relx=0.5: 50% chiều rộng cửa sổ.
# rely=0.5: 50% chiều cao cửa sổ.
# anchor="center": Lấy tâm widget làm điểm neo.
#----------------------------------------------------------------------------





