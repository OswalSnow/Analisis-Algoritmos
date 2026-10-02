import tkinter as tk
import matplotlib.pyplot as plt
import benchmark

root = tk.Tk()
root.title("Brute Force Algorithms Comparation")

width_screen = root.winfo_screenwidth()
height_screen = root.winfo_screenheight()

width_root = 375
height_root = 300
x_coordinate = (width_screen - width_root)//2
y_coordinate = (height_screen - height_root)//2

root.geometry(f"{width_root}x{height_root}+{x_coordinate}+{y_coordinate}")

lb1 = tk.Label(root, text="Many algorithms comparation", foreground="gray")
lb1.pack(pady=8)

bu1 = tk.Button(root, text="Show me stats!", command=benchmark.Showing_Plot)
bu1.pack(pady=10)

bu1 = tk.Button(root, text="Show me Stooge Sort stats!", command=benchmark.Showing_StoogePlot)
bu1.pack(pady=10)

root.mainloop()


