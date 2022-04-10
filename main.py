import tkinter as tk
from tkinter import messagebox
from tkinter import Tk, Frame, Menu
import tkinter.font as font
from tkinter import *
import os
import texteditor as t    
root = tk.Tk()
root.title("Text Editor")
root.geometry("350x400")
app = t.TextEditor(root)
tk.mainloop()
