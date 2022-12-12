from tkinter import *
from pathlib import Path
import pygame
from data import strand, skills

# Frame for start page
class second(Frame):
    # constants
    pygame.mixer.init()
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./middle assets")

    # start page class init method
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # creating the whole canvas of the frame
        canvas = Canvas(self, height=800, width=1360, bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x=0, y=0)

        # creating the background design for start page
        self.image_bg = PhotoImage(file=self.relative_to_assets("bg.png"))
        canvas.create_image(680.0000000000001, 400.0, image=self.image_bg)

        # button image for strongly disagree button
        self.button_imgStronglyDisagree = PhotoImage(file=self.relative_to_assets("button_StronglyDisagree.png"))
        self.button_imgStronglyDisagree_on = PhotoImage(file=self.relative_to_assets("button_StronglyDisagree_on.png"))

        # button image for disagree button
        self.button_imgDisagree = PhotoImage(file=self.relative_to_assets("button_Disagree.png"))
        self.button_imgDisagree_on = PhotoImage(file=self.relative_to_assets("button_Disagree_on.png"))

        # button image for neutral button
        self.button_imgNeutral = PhotoImage(file=self.relative_to_assets("button_Neutral.png"))
        self.button_imgNeutral_on = PhotoImage(file=self.relative_to_assets("button_Neutral_on.png"))

        # button image for agree button
        self.button_imgAgree = PhotoImage(file=self.relative_to_assets("button_Agree.png"))
        self.button_imgAgree_on = PhotoImage(file=self.relative_to_assets("button_Agree_on.png"))

        # button image for strongly agree button
        self.button_imgStronglyAgree = PhotoImage(file=self.relative_to_assets("button_StronglyAgree.png"))
        self.button_imgStronglyAgree_on = PhotoImage(file=self.relative_to_assets("button_StronglyAgree_on.png"))

        #back button
        self.button_imgBack = PhotoImage(file=self.relative_to_assets("button_Back.png"))
        button_Back = Button(image=self.button_imgBack, borderwidth=0, highlightthickness=0,
        command=lambda: print("button_1 clicked"), relief="flat")
        button_Back.place(x=538.0,y=706.0,width=95.0,height=46.0)

        #next button
        self.button_imgNext = PhotoImage(file=self.relative_to_assets("button_Next.png"))
        button_Next = Button(image=self.button_imgNext, borderwidth=0, highlightthickness=0, 
        command=lambda: print("button_2 clicked"), relief="flat")
        button_Next.place(x=761.0, y=704.0, width=95.0, height=46.0)

        #c1r1
        button_c1r1 = Button(image=self.button_imgStronglyDisagree, borderwidth=0, highlightthickness=0,
                        command=lambda: self.strongly_disagree(controller, button_c1r1, None, None),
                        relief="flat")
        button_c1r1.place(x=422.0, y=85.0, width=70.0, height=68.0)

        #c2r1
        button_c2r1 = Button(image=self.button_imgDisagree, borderwidth=0, highlightthickness=0,
                        command=lambda: self.disagree(controller, button_c2r1), relief="flat")
        button_c2r1.place(x=561.0, y=95.0, width=50.0, height=48.0)
    

        # creating the image for sound
        self.is_on = True
        self.on = PhotoImage(file=self.relative_to_assets("button_SoundsOn.png"))
        self.off = PhotoImage(file=self.relative_to_assets("button_SoundsOff.png"))

        # creating the button for sound
        self.button_Sound = Button(self, image=self.on, bd=0, command=self.switch, relief="flat")
        self.button_Sound.place(x=1167.0, y=0.0, width=193.0, height=91.0)

        self.play()

    # function for the right path
    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    # function for strongly disagree button
    def strongly_disagree(self, controller, button_pos, key, skill):
        strand[key] += 1
        skills[key][skill] += 1
        button_pos["image"] = self.button_imgStronglyDisagree_on

    # function for disagree button
    def disagree(self, controller, button_pos, key, skill):
        strand[key] += 1
        skills[key][skill] += 1
        button_pos["image"] = self.button_imgDisagree_on

    # function for neutral button
    def neutral(self, controller, button_pos, key, skill):
        strand[key] += 1
        skills[key][skill] += 1
        button_pos["image"] = self.button_imgNeutral_on

    # function for agree button
    def agree(self, controller, button_pos, key, skill):
        strand[key] += 1
        skills[key][skill] += 1
        button_pos["image"] = self.button_imgAgree_on

    # function for strongly disagree button
    def strongly_agree(self, controller, button_pos, key, skill):
        strand[key] += 1
        skills[key][skill] += 1
        button_pos["image"] = self.button_imgStronglyAgree_on

    # for playing the music
    def play(self):
        pygame.mixer.music.load("StartPage/assets/song.mp3")
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(loops=5)

    # for stopping the music
    def stop(self):
        pygame.mixer.music.stop()

    # on/off of the music
    def switch(self):
        if self.is_on:
            self.button_Sound.config(image=self.off)
            self.button_Sound.config(command=self.stop())
            self.is_on = False

        else:
            self.button_Sound.config(image=self.on)
            self.button_Sound.config(command=self.play())
            self.is_on = True
