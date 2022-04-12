import tkinter as tk
from tkinter import messagebox
from tkinter import Tk, Frame, Menu
import tkinter.font as font
from tkinter import *
import os
python = {
  "print" : "purple",
  "if": "orange",
  "True": "blue",
  "else": "orange",
  "False": "blue",
  "print(" : "purple",
  "if": "orange",
  "True:": "blue",
  "else:": "orange",
  "False:": "blue",
  "import":"blue"
}
cpp = {
  "if":"blue",
  "include":"blue",
  "cout":"red",
  "if(":"blue",
  "#include":"blue",
  "std::cout":"red",
  "int":"blue",
  "#define":"orange",
  "float": "blue",
  "unsigned":"green",
  "signed": "green",
  "using":"blue",
  "namespace": "blue",
  '""':"green",
  "=":"red",
  "<<":"red"
}
remove = [':',"(","<<"]
class Terminal:
  def __init__(self,d):
    self.fullout = []
    self.bruh = tk.Label(d,text="Terminal")
    self.bruh.pack()
    self.output = tk.Text(d,height=10,width=30) 
    self.d = tk.Text(d,height=3,width=10) 
    self.c = tk.Button(d,command=lambda:self.send(),text="Send Command")
    self.output.pack()
    self.d.pack()
    self.c.pack()
  def send(self):
    c = os.popen(self.d.get("1.0",'end-1c')).read()
    self.fullout.append(c)
    self.output.insert("1.0", c)
class TextEditor:
  def __init__(self,root):
    #info needed 
    self.currentfont = 'Arial'
    os.system('fluxbox')
    #
    top = Frame(root)
    bottom = Frame(root)
    top.pack(side=TOP)
    bottom.pack(side=BOTTOM, fill=BOTH, expand=True)
    # Window Details
    self.hello = tk.Label(text="Text Editor")
    self.hello.pack()
    #Main Text Box
    self.scrollbar = Scrollbar(root)
 
    self.box = tk.Text(root,height=10,width=30,yscrollcommand=self.scrollbar.set)  
    self.box.configure(font = 'Arial')
    for key in python:
      self.box.tag_configure(key, background="white", foreground=python[key])
    for key in cpp:
      self.box.tag_configure(key, background="white", foreground=cpp[key])
    self.scrollbar.config(command=self.box.yview)
    self.scrollbar.pack(side=RIGHT, fill=Y)
    self.box.pack()
    #Save as textbox
    self.saveas = tk.Text(root,height=1,width=10)
    self.saveas.pack(in_=bottom,side=LEFT)

    #buttons
    self.button = tk.Button(command=self.save,text="Save")
    self.button.pack(in_=bottom,side=LEFT)
    self.open = tk.Button(command=self.read,text="Open")
    self.open.pack(in_=bottom,side=LEFT)
    #create toolbar thing
    menubar = Menu(root)
    root.config(menu=menubar)
    #file menu (lol)
    
    #code highlighting
    codeMenu = Menu(menubar)
    codeMenu.add_command(label="[Python] Refresh Syntax Highlighting ",command=lambda: self.syntaxHighlight('Python'))
    codeMenu.add_command(label="[C++] Refresh Syntax Highlighting ",command=lambda: self.syntaxHighlight('C++'))
    menubar.add_cascade(label="Syntax", menu=codeMenu)
    #basic text editor stuff
    editMenu = Menu(menubar)
    editMenu.add_command(label="Bold",command=lambda: self.bold())
    menubar.add_cascade(label="Edit", menu=editMenu)
    #bold
    self.box.tag_config("bt",font=(self.currentfont, "12", "bold"))
    #submeny of edit
    fileMenu = Menu(menubar)
    fileMenu.add_command(label="Times New Roman", command=lambda: self.changeFont('Times New Roman') )
    fileMenu.add_command(label="Courier", command=lambda: self.changeFont('Courier'))
    #Georgia
    fileMenu.add_command(label="Arial", command=lambda: self.changeFont('Arial'))
    #Platino Linotype
    fileMenu.add_command(label="Platino Linotype", command=lambda: self.changeFont('Platino Linotype'))
    editMenu.add_cascade(label="Font", menu=fileMenu)
    #compile
    compileMenu = Menu(menubar)
    compileMenu.add_command(label="Compile C++",command=lambda: self.compilecpp())
    compileMenu.add_command(label="Compile Python",command=lambda: self.compilepython())
    menubar.add_cascade(label="Compile", menu=compileMenu)
    #median tasks
    taskMenu = Menu(menubar)
    taskMenu.add_command(label="Open Terminal",command=lambda: self.terminal())
    menubar.add_cascade(label="Tasks", menu=taskMenu)

    #help menu
    helpMenu = Menu(menubar)
    helpMenu.add_command(label="About",command=lambda:self.about())
    menubar.add_cascade(label="Help",menu=helpMenu)
    #self.box.tag_config("new",font=(self.currentfont, "14", "default"))
  #Change font
  def bold(self):
    self.box.tag_add("bt", "sel.first", "sel.last")
  def size(self):
    self.box.tag_add("fontsize","sel.first", "sel.last")
  def save(self):  
    b = self.saveas.get("1.0",'end-1c')
    try:
      extension = b.split(".",1)[1]
    except IndexError:
      b = b+".rbtf"
      messagebox.showerror(title="No extension", message="Automaticly Saving with .rbtf")
      extension = "rbtf"
    if (extension == "rbtf"):
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
    if (extensio == ".rbtf"):
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
            self.box.insert("1.0",main[len(main)-(i+1)])
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
            print(len(main)-(i+1))
            self.box.insert("1.0",main[len(main)-(i+1)])
      except FileNotFoundError:
        messagebox.showerror(title="File Not found!", message="File not found. :(")
  def changeFont(self,thecurrentfont):
    thefont = font.Font(family=thecurrentfont)
    self.box.configure(font = thefont)
    self.currentfont = thecurrentfont
  def syntaxHighlight(self,language):
    lines = self.box.get("1.0",'end-1c')
    newlines = lines.split()
    syntax = []
    #word = self.box.selection_get()
    pos_start = "1.0"
    print(newlines)
    if language == "Python":
      syntax = python
    elif language == "C++":
      syntax = cpp 
    for line in newlines:
      for item in remove:
        sep = item
        word = line.split(sep, 1)[0]
      print("Word:",word) 
      offset = '+%dc' % len(word)
      print(offset)
      prevpos_start = pos_start
      pos_start = self.box.search(word, prevpos_start, 'end')
      pos_end = pos_start + offset
      print("Final: "+word)
      #print(pos_start)
     #print(pos_end)
      # index = self.box.search(line, "insert", backwards=True, regexp=True)
      # if index == "":
      #   index ="1.0"
      # else:
      #   index = self.box.index("%s+1c" % index)
      #word = self.text.get(index, "insert")
      if word in syntax:
        print(word+"is in syntax")
        #self.box.tag_add(word, "sel.first", "sel.last")
        #self.box.tag_add(line, index, "%s+%dc" % (index, len(line)))
        self.box.tag_add(word, pos_start, pos_end)
    #thecolor = color.Color(rncolor)
    #self.box.configure = (color = thecolor)
  def compilecpp(self):
    self.save()
    d = self.saveas.get("1.0",'end-1c')
    o = os.popen('g++ '+d).read()
    #o = os.system('g++ '+d).read
    messagebox.showerror(title="G++ output", message="Compilation Finished. Press OK")
    #print(output)
    output = os.popen('./a.out').read()
    messagebox.showerror(title="Compile Output", message=output)
    print(output)
  def compilepython(self):
    self.save()
    d = self.saveas.get("1.0",'end-1c')
    o = os.popen('python3 '+d).read()
    messagebox.showerror(title="Compile Output", message=o)
  def terminal(self):
    e = tk.Tk()
    e.title("Terminal")
    e.geometry("350x300")
    app = Terminal(e)
    tk.mainloop()

  def about(self):
    messagebox.showerror(title="About", message="Text Editor, 0.10")
