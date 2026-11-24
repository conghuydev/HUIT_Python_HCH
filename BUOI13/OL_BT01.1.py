import tkinter as tk

root = tk.Tk()
root.title("Minh hoa Pack")
root.geometry("400x300")

tk.Label(root, text="Label 1", bg="red").pack(side="top", fill="x")
tk.Label(root, text="Label 2", bg="green").pack(side="left", fill="y")
tk.Label(root, text="Label 3", bg="blue").pack(side="right", fill="y")

root.mainloop()