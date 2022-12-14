import sys
from tkinter import *
import matplotlib.pyplot as plt
from StartPage.StartPage import StartPage
from HomePage.HomePage import HomePage
from StrandPage.StrandPage import StrandPage
from InstructionsPage.InstructionsPage import InstructionsPage
from Statements.First import First
from Statements.Second import Second
from Statements.Third import Third
from Statements.Fourth import Fourth
from Statements.Fifth import Fifth
from Statements.Sixth import Sixth
from Statements.Seventh import Seventh
from Statements.Eighth import Eighth
from Statements.Ninth import Ninth
from Statements.Tenth import Tenth
from ResultPage.STEM.STEM import STEM
from ResultPage.ABM.ABM import ABM
from ResultPage.HUMSS.HUMSS import HUMSS
from ResultPage.GAS.GAS import GAS
from ResultPage.ICT.ICT import ICT


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

        # ratings per strands
        self.strands_ratings = {"STEM": 0,
                                "ABM": 0,
                                "HUMSS": 0,
                                "ICT": 0,
                                "GAS": 0}

        # skills for STEM
        self.skills = {
            "STEM": {"Problem-Solving": 0,
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
                    "Marketing and Video-Editing": 0},

            "GAS": {"Adaptability": 0,
                    "Presentation": 0,
                    "Technical": 0}
        }

        self.result_strand = ''
        self.result_skills = ''
        # the user's name
        self.name = ''
        # variable for strand page
        self.strand = ''

        # calling the first screen
        self.show_frame("ABM")

    def __setitem__(self, key, value):
        self.strands_ratings[key] += value

    def __getitem__(self, item):
        return self.strands_ratings[item]

    def results(self):
        # getting the strand with the highest rating
        self.result_strand = max(self.strands_ratings, key=self.strands_ratings.get)
        # making a copy of skills of the resulting strand
        skills_copy = self.skills[self.result_strand]

        # getting the skills with the highest rating
        self.result_skills = [key for key, value in skills_copy.items() if value == max(skills_copy.values())]

    def graph(self):
        colors = ['green', 'blue', 'purple', 'teal', 'orange']
        ratings = list(self.strands_ratings.values())
        x_axis = ["STEM", "ABM", "HUMSS", "ICT", "GAS"]
        y_axis = ratings
        plt.ylim(-15, 70)
        plt.bar(x_axis, y_axis, color=colors)
        for idx, val in enumerate(ratings):
            plt.text(idx, val + 1, val, ha="center")

        plt.title("StrGuide Result")
        plt.text(2, -8, "Dito ilalagay yung skills description. \nTriny ko ilabas sa box kaso hindi siya nababasa", ha="center")
        plt.xlabel("Strands", fontsize=8)
        plt.ylabel("Ratings", fontsize=8)
        plt.show()

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


# initialize main window app
window = MainFrame()
window.title("StrGuide")
icon = PhotoImage(file='icon.png')
window.iconphoto(True, icon)
window.mainloop()
