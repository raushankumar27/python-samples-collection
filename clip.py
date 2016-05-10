import tkinter as tk
import time
import threading
r=tk.Tk("hello")
text=''
ptext=''
while(True):
	time.sleep(1)
	try:
		text=r.clipboard_get()
	except:
		print("clipboard empty")
	if(ptext!=text):
		print(text)
		ptext=text