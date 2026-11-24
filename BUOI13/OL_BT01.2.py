import tkinter as tk

root = tk.Tk()
root.title("Minh hoa Grid")
root.geometry("400x300")

tk.Label(root, text="Label 1", bg="red").grid(row=0, column=0, sticky="nsew")
tk.Label(root, text="Label 2", bg="green").grid(row=1, column=0, sticky="nsew")
tk.Label(root, text="Label 3", bg="blue").grid(row=0, column=1, sticky="nsew")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

root.mainloop()
