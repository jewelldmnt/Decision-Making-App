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

        # skills ratings for STEM
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

        # description for each skill
        self.skills_description = {
            "STEM": {"Problem-Solving": "You have the ability to recognize the problem by thinking \n"
                                        "outside the box and come up with different alternative \n"
                                        "approaches that would help you to take the appropriate \n"
                                        "course of action in a certain problem.",

                     "Math-Science": "You want being challenged by solving different math equations \n"
                                     "and it is also fundamental in understanding science which you \n"
                                     "also enjoy.",

                     "Innovative": "You have knowledge and abilities you use to create and adapt to \n"
                                   "change, this will allow you to use your existing knowledge to \n"
                                   "discover original ideas that benefit you and your team."},

            "ABM": {"Business Communication": "You can build relationships by carefully listening \n"
                                              "to others, has a good judgement, and confident to \n"
                                              "speak clearly with your audience comfortably. ",
                    "Financial Management": " You are able to manage your perosonal finances and \n"
                                            "able to apply neccesary skills to spend your own money \n"
                                            "wisely.",
                    "Business": "You can think of opportunities to earn and able to \n"
                                "lead a group that has the same goals."},

            "HUMSS": {"Communication": "You are confident to speak out your thoughts, and you \n"
                                       "can easily communicate and resonate with people easily. ",
                      "Creativity": "With the constant change in circumstances, you frequently \n"
                                    "come up with fresh (creative) solutions to specific difficulties, \n"
                                    "thus creatively expressing yourself in that way. ",
                      "Social and Cultural Awareness": "You have sensitivity and respect for differences among \n"
                                                       "people you interact with, thus, being willing to objectively \n"
                                                       "examine the values, beliefs, traditions, and perceptions \n"
                                                       "within your own and other cultures."},

            "ICT": {"Innovative": "You have the capacity to think critically about \n"
                                  "the best solution to a given problem and picture \n"
                                  "situations from several points of view. ",
                    "Computer": "You can utilize computers and other associated \n"
                                "technologies because you have the knowledge and \n"
                                "skills necessary.",
                    "Marketing and Video-Editing": "You can creatively create videos that entertain \n"
                                                   "audiences or have an interest to make videos that \n"
                                                   "captures people's attention."},

            "GAS": {"Adaptability": "You seem uncertain and confused on what specific \n"
                                    "path you would take and you still want to weigh \n"
                                    "your options.",
                    "Presentation": "You like to communicate and create ideas to \n"
                                    "help other people.",
                    "Technical": "You are flexible enough to take any strand in \n"
                                 "Senior High School because of your eagerness to \n"
                                 "learn different subjects."}
        }

        # initializes the result_strand
        self.result_strand = ''
        # initializes the result skills
        self.result_skills = ''
        # the user's name
        self.name = ''
        # variable for strand page
        self.strand = ''

        # calling the first screen
        self.show_frame("StartPage")

    # getting the strand and skill result
    def results(self):
        # getting the strand with the highest rating
        self.result_strand = max(self.strands_ratings, key=self.strands_ratings.get)
        # making a copy of skills of the resulting strand
        skills_copy = self.skills[self.result_strand]

        # getting the skills with the highest rating
        self.result_skills = max(skills_copy, key=skills_copy.get)

    # graphing the result
    def graph(self):
        colors = ['green', 'blue', 'purple', 'teal', 'orange']
        ratings = list(self.strands_ratings.values())
        x_axis = ["STEM", "ABM", "HUMSS", "ICT", "GAS"]
        y_axis = ratings
        plt.ylim(-20, 70)
        plt.bar(x_axis, y_axis, color=colors)
        for idx, val in enumerate(ratings):
            plt.text(idx, val + 1, val, ha="center")

        plt.title("StrGuide Result")
        plt.text(2, -18, self.skills_description[self.result_strand][self.result_skills], ha="center")
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
