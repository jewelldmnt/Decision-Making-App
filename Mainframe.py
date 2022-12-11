import sys
from tkinter import *
from StartPage.StartPage import StartPage
from HomePage.HomePage import HomePage
from StrandPage.StrandPage import StrandPage
from Statements.first import first


# class for the main frame
class MainFrame(Tk):
    # init method of the class Mainframe
    def __init__(self, *args, **kwargs):
        # init method of the tk class
        Tk.__init__(self, *args, **kwargs)

        # setting the default screen size
        self.geometry("1360x800")
        self.resizable(False, False)

        # creating a container for all
        self.container = Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.name = ''
        self.strand = ''

        # initial total scores per strand
        self.strand = {"STEM": 0,
                       "ABM": 0,
                       "HUMSS": 0,
                       "ICT": 0,
                       "GAS": 0}

        # skills for STEM
        self.skills = {
                        "STEM": {"Problem Solving": 0,
                                 "Math-Science": 0,
                                 "Innovative": 0},

                        "ABM": {"Business Communication": 0,
                                "Financial Management": 0,
                                "Business": 0},

                        "HUMSS": {"Communication": 0,
                                  "Creativity": 0,
                                  "Social and Cultural Awareness": 0},

                        "ICT": {"Innovative": 0,
                                "Computer": 0,
                                "Marketing and Video Editing": 0},

                        "GAS": {"Adaptability": 0,
                                "Presentation": 0,
                                "Technical": 0}
                    }

        # calling the first screen
        self.show_frame("StartPage")

    # showing the current frame above everything
    def show_frame(self, page_name, name=None, strand=None):
        self.name = name
        self.strand = strand

        # converting the page_name str into class
        f = getattr(sys.modules[__name__], page_name)

        # raising a specific frame
        frame = f(self.container, self)
        frame.grid(row=0, column=0, sticky="NSEW")
        frame.tkraise()

    def rate_strand(self, key, skills, rate):
        self.strand[key] += rate


# initialize main window app
window = MainFrame()
window.title("StrGuide")
icon = PhotoImage(file='icon.png')
window.iconphoto(True, icon)
window.mainloop()
