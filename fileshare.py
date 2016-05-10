import tkinter as tk
from tkinter import filedialog
root=tk.Tk()
root.withdraw()
file_path=tk.filedialog.askopenfilename()
print(file_path)
file=open(file_path,"r")
print(file.read())