# for functioning of the screenshot module.
import pyautogui

# for gui creation.

# import tkinter as tk
from tkinter.filedialog import *

# function for taking screenshot


def screenshot():
    snaptaker = pyautogui.screenshot()
    save_path = asksaveasfilename()
    snaptaker.save(save_path+'screenshot.png')


root = tk.Tk()
screen = tk.Canvas(root, width = 300, height = 300)
screen.pack()
btn = tk.Button(root, text='take snapshot', command = screenshot, font = 10)
btn.pack()
root.mainloop()