from tkinter import *
from HomePage import HomePage as hp
from StartPage import StartPage as sp


# class for the main frame
class MainFrame(Tk):
    # init method of the class Mainframe
    def __init__(self, *args, **kwargs):
        # init method of the tk class
        Tk.__init__(self, *args, **kwargs)

        self.geometry("1360x800")
        self.resizable(False, False)

        # creating a container for all
        self.container = Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # creating a dictionary for page objects
        self.frames = {}
        self.name = ''

        # looping in every page/class and creating an object of it
        # then storing the class name as the key
        # and the object of it as the value
        for f in {sp.StartPage, hp.HomePage}:
            page_name = f.__name__
            self._frame = f(self.container, self)
            self._frame.grid(row=0, column=0, sticky="NSEW")
            self.frames[page_name] = self._frame
        self.show_frame("StartPage")

    # showing the current frame above everything
    def show_frame(self, page_name, name=None):
        self.name = name
        if page_name == "HomePage":
            pg = hp.HomePage.__name__
            self._frame = hp.HomePage(self.container, self)
            self._frame.grid(row=0, column=0, sticky="NSEW")
            self.frames[pg] = self._frame
        self.frames[page_name].tkraise()


# initialize main window app
window = MainFrame()
window.title("StrGuide")
window.mainloop()
