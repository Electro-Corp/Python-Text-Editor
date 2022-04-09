import tkinter as tk
from tkinter import messagebox
from tkinter import Tk, Frame, Menu
import tkinter.font as font
import os
class TextEditor:
  def __init__(self,root):
    #info needed 
    self.currentfont = 'Arial'
    # Window Details
    self.hello = tk.Label(text="Text Editor")
    self.hello.pack()
    #Main Text Box
    self.box = tk.Text(root,height=15,width=30)  
    self.box.configure(font = 'Arial')
    self.box.pack()
    #Save as textbox
    self.saveas = tk.Text(root,height=1,width=10)
    self.saveas.pack()
    #buttons
    self.button = tk.Button(command=self.save,text="Save")
    self.button.pack()
    self.open = tk.Button(command=self.read,text="Open")
    self.open.pack()
    #tool bar for font changes and the such
    menubar = Menu(root)
    root.config(menu=menubar)
    fileMenu = Menu(menubar)
    fileMenu.add_command(label="Times New Roman", command=lambda: self.changeFont('Times New Roman') )
    fileMenu.add_command(label="Courier", command=lambda: self.changeFont('Courier'))
    #Georgia
    fileMenu.add_command(label="Arial", command=lambda: self.changeFont('Arial'))
    #Platino Linotype
    fileMenu.add_command(label="Platino Linotype", command=lambda: self.changeFont('Platino Linotype'))
    menubar.add_cascade(label="Font", menu=fileMenu)
  #Change font
  def save(self):  
    b = self.saveas.get("1.0",'end-1c')
    try:
      extension = b.split(".",1)[1]
    except IndexError:
      b = b+".tex"
      messagebox.showerror(title="No extension", message="Automaticly Saving with .tex")
    if (extension == "tex"):
      try:
        open(b,'x')
      except FileExistsError:  
        open(b,'w')
      with open(b,'w') as f:
        c = self.box.get("1.0",'end-1c')
        f.write("FONT\n")
        f.write(self.currentfont+'\n')
        f.write("TEXT\n")
        f.write(c)
    else:
      try:
        open(b,'x')
      except FileExistsError:  
        open(b,'w')
      with open(b,'w') as f:
        c = self.box.get("1.0",'end-1c')
        f.write(c)
  def read(self):
    b = self.saveas.get("1.0",'end-1c')
    filename, extensio = os.path.splitext(b)
    if (extensio == ".tex"):
      try:
        with open(b,'r') as f:
          try:
            thelines = f.readlines()
          except UnicodeDecodeError:
            messagebox.showerror(title="Formatting Error", message="Cannot Decode file.")
          self.box.delete("1.0", tk.END)
          a = 0
          main = []
          for line in thelines:
            if a == 1:
              font = line.rstrip()
            if a > 2:
              main.append(line)
            a = a+1
          self.changeFont(str(font))
          print(font)
          for i in range(len(main)):
            self.box.insert("1.0",main[i])
      except FileNotFoundError:
        messagebox.showerror(title="File Not found!", message="File not found. :(")
    else:
      try:
        with open(b,'r') as f:
          try:
            thelines = f.readlines()
          except UnicodeDecodeError:
            messagebox.showerror(title="Formatting Error", message="Cannot Decode file.")
          self.box.delete("1.0", tk.END)
          a = 0
          main = []
          for line in thelines:
            main.append(line)
          for i in range(len(main)):
            self.box.insert("1.0",main[i])
      except FileNotFoundError:
        messagebox.showerror(title="File Not found!", message="File not found. :(")
  def changeFont(self,thecurrentfont):
    thefont = font.Font(family=thecurrentfont)
    self.box.configure(font = thefont)
    self.currentfont = thecurrentfont
root = tk.Tk()
root.title("Text Editor")
root.geometry("350x400")
app = TextEditor(root)
tk.mainloop()
