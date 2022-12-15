from tkinter import *
from tkinter.font import Font
from pathlib import Path
import pygame


# Frame for home page
class HomePage(Frame):
    # constants
    pygame.mixer.init()
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")

    # sign in page class init method
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # creating the whole canvas of the frame
        canvas = Canvas(self, bg="#B5E2FA", height=800, width=1360, bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x=0, y=0)

        # creating the background design for HomePage
        self.image_bg = PhotoImage(file=self.relative_to_assets("bg.png"))
        canvas.create_image(680.0, 400.0, image=self.image_bg)

        # creating the button for Take the Quiz
        self.button_imgTakeQuiz = PhotoImage(file=self.relative_to_assets("button_TakeQuiz.png"))
        button_TakeQuiz = Button(self, image=self.button_imgTakeQuiz, borderwidth=0, highlightthickness=0,
                                 command=lambda: controller.show_frame("InstructionsPage", controller.name),
                                 relief="flat")
        button_TakeQuiz.place(x=563.0, y=381.0, width=235.0, height=52.0)

        # creating the button for Take the Quiz
        self.button_imgExit = PhotoImage(file=self.relative_to_assets("button_Exit.png"))
        button_Exit = Button(self, image=self.button_imgExit, borderwidth=0, highlightthickness=0,
                             command=lambda: exit(), relief="flat")
        button_Exit.place(x=1308.0, y=0.0, width=51.0, height=33.0)

        # creating the button for ABM strand
        self.button_imgABM = PhotoImage(file=self.relative_to_assets("button_ABM.png"))
        button_ABM = Button(self, image=self.button_imgABM, borderwidth=0, highlightthickness=0,
                            command=lambda: controller.show_frame("StrandPage", controller.name, "ABM"), relief="flat")
        button_ABM.place(x=334.0, y=28.0, width=103.0, height=62.0)

        # creating the button for GAS strand
        self.button_imgGAS = PhotoImage(file=self.relative_to_assets("button_GAS.png"))
        button_GAS = Button(self, image=self.button_imgGAS, borderwidth=0, highlightthickness=0,
                            command=lambda: controller.show_frame("StrandPage", controller.name, "GAS"), relief="flat")
        button_GAS.place(x=477.0, y=28.0, width=123.0, height=50.0)

        # creating the button for HUMSS strand
        self.button_imgHUMSS = PhotoImage(file=self.relative_to_assets("button_HUMSS.png"))
        button_HUMSS = Button(self, image=self.button_imgHUMSS, borderwidth=0, highlightthickness=0,
                              command=lambda: controller.show_frame("StrandPage", controller.name, "HUMSS"),
                              relief="flat")
        button_HUMSS.place(x=632.0, y=28.0, width=148.0, height=50.0)

        # creating the button for ICT strand
        self.button_imgICT = PhotoImage(file=self.relative_to_assets("button_ICT.png"))
        button_ICT = Button(self, image=self.button_imgICT, borderwidth=0, highlightthickness=0,
                            command=lambda: controller.show_frame("StrandPage", controller.name, "ICT"), relief="flat")
        button_ICT.place(x=817.0, y=28.0, width=108.0, height=62.0)

        # creating the button for STEM strand
        self.button_imgSTEM = PhotoImage(file=self.relative_to_assets("button_STEM.png"))
        button_STEM = Button(self, image=self.button_imgSTEM, borderwidth=0, highlightthickness=0,
                             command=lambda: controller.show_frame("StrandPage", controller.name, "STEM"),
                             relief="flat")
        button_STEM.place(x=964.0, y=28.0, width=118.0, height=50.0)

        # creating the button for changing the user's name
        self.button_imgChangeName = PhotoImage(file=self.relative_to_assets("button_ChangeName.png"))
        button_ChangeName = Button(self, image=self.button_imgChangeName, borderwidth=0, highlightthickness=0,
                                   command=lambda: controller.show_frame("StartPage"), relief="flat")
        button_ChangeName.place(x=169.0, y=59.0, width=120.0, height=25.0)

        # creating the "Hi User" text
        self.myFont = Font(family="Nanum Pen", size=25 * -1)
        canvas.create_text(136.0, 33.0, anchor="nw", text=f"Hi, {controller.name}", fill="#000000", font=self.myFont)

        # creating the image for sound
        self.is_on = True
        self.on = PhotoImage(file=self.relative_to_assets("button_SoundsOn.png"))
        self.off = PhotoImage(file=self.relative_to_assets("button_SoundsOff.png"))

        # creating the button for sound
        self.button_Sound = Button(self, image=self.on, bd=0, command=self.switch, relief="flat")
        self.button_Sound.place(x=1155.0, y=35.0, width=174.0, height=48.0)

        self.play()

    # for the path to be right
    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    # for playing the sound
    def play(self):
        pygame.mixer.music.load("HomePage/assets/song.mp3")
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(loops=5)

    # for stopping the sound
    def stop(self):
        pygame.mixer.music.stop()

    def switch(self):
        if self.is_on:
            self.button_Sound.config(image=self.off)
            self.button_Sound.config(command=self.stop())
            self.is_on = False

        else:
            self.button_Sound.config(image=self.on)
            self.button_Sound.config(command=self.play())
            self.is_on = True
