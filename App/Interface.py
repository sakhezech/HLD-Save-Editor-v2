from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.messagebox import showerror

class Interface():
    """
    GUI manager
    """

    # file -> load
    def load(self, event=None):
        try:
            filename = filedialog.askopenfilename(initialdir=self.app.savefile_path)
            self.editor.load(filename)
        except Exception as e:
            showerror(title=type(e), message=e)


    # file -> save
    def save(self, event=None):
        try:
            filename = self.editor.filename
            if filename is None:
                filename = filedialog.asksaveasfilename(initialdir=self.app.savefile_path, defaultextension=".hlds", filetypes=[("HLDS File", "*.hlds")])
            self.editor.save(filename)
        except Exception as e:
            showerror(title="Error", message=e)


    # file -> save as
    def saveas(self):
        try:
            filename = filedialog.asksaveasfilename(initialdir=self.app.savefile_path, defaultextension=".hlds", filetypes=[("HLDS File", "*.hlds")])
            self.editor.save(filename)
        except Exception as e:
            showerror(title="Error", message=e)

    
    # file -> export
    def export(self, slot):
        self.editor.export(slot)
    

    def __init__(self, editor, app):
        self.editor = editor
        self.app = app
        self.tk = Tk(screenName="Editor")
        self.tk.option_add('*tearOff', FALSE)
        
        # menu
        self.menu = Menu(self.tk)
        self.filemenu = Menu(self.menu)
        self.exportmenu = Menu(self.filemenu)
        self.menu.add_cascade(label="File", menu=self.filemenu)

        self.filemenu.add_command(label="Load", command=self.load, accelerator="Ctrl+L")
        self.filemenu.add_command(label="Save", command=self.save, accelerator="Ctrl+S")
        self.filemenu.add_command(label="Save As", command=self.saveas)
        self.filemenu.add_cascade(label="Export", menu=self.exportmenu)
        self.exportmenu.add_command(label="Slot 1", command=lambda: self.export(1), accelerator="Ctrl+1")
        self.exportmenu.add_command(label="Slot 2", command=lambda: self.export(2), accelerator="Ctrl+2")
        self.exportmenu.add_command(label="Slot 3", command=lambda: self.export(3), accelerator="Ctrl+3")
        self.exportmenu.add_command(label="Slot 4", command=lambda: self.export(4), accelerator="Ctrl+4")

        self.tk.bind("<Control-KeyPress-1>", lambda x: self.export(1))
        self.tk.bind("<Control-KeyPress-2>", lambda x: self.export(2))
        self.tk.bind("<Control-KeyPress-3>", lambda x: self.export(3))
        self.tk.bind("<Control-KeyPress-4>", lambda x: self.export(4))
        self.tk.bind("<Control-l>", self.load)
        self.tk.bind("<Control-s>", self.save)
        self.tk.config(menu=self.menu)

