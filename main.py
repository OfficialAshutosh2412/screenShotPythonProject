# for functioning of the screenshot module.
import pyautogui

# for gui creation.

# import tkinter as tk
from tkinter.filedialog import *
from tkinter import *
# function for taking screenshot


def screenshot():
    snaptaker = pyautogui.screenshot()
    save_path = asksaveasfilename()
    snaptaker.save(save_path+'screenshot.png')


root = Tk()
root.geometry("300x300+350+40")
btn = Button(root, text='take snapshot', command = screenshot, font = 10)
btn.pack()
root.mainloop()
