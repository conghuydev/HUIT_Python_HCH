import tkinter as tk

root = tk.Tk()
root.title("Minh hoa Place")
root.geometry("400x300")

tk.Label(root, text="Label 1", bg="red").place(x=20, y=20, width=100, height=40)
tk.Label(root, text="Label 2", bg="green").place(x=100, y=100, width=100, height=40)
tk.Label(root, text="Label 3", bg="blue").place(x=200, y=180, width=100, height=40)

root.mainloop()