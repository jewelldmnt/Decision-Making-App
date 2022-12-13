from tkinter import *
from pathlib import Path
import pygame


# Frame for start page
class Fourth(Frame):
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

        # creating the background design for 6 to 10 page
        self.image_bg = PhotoImage(file=self.relative_to_assets("bg4.png"))
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

        # creating the back button
        self.button_imgBack = PhotoImage(file=self.relative_to_assets("button_Back.png"))
        button_Back = Button(self, image=self.button_imgBack, borderwidth=0, highlightthickness=0,
                             command=lambda: controller.show_frame("First", controller.name), relief="flat")
        button_Back.place(x=538.0, y=706.0, width=95.0, height=46.0)

        # creating the next button
        self.button_imgNext = PhotoImage(file=self.relative_to_assets("button_Next.png"))
        button_Next = Button(self, image=self.button_imgNext, borderwidth=0, highlightthickness=0,
                             command=lambda: controller.show_frame("Tenth", controller.name), relief="flat")
        button_Next.place(x=761.0, y=704.0, width=95.0, height=46.0)

        # creating c1r1 strong disagree button
        button_c1r1 = Button(self, image=self.button_imgStronglyDisagree, borderwidth=0, highlightthickness=0,
                             command=lambda: self.strongly_disagree(button_c1r1, "c1r1", controller, "ICT", "Innovative"), relief="flat")
        button_c1r1.place(x=422.0, y=85.0, width=70.0, height=68.0)

        # creating c2r1 disagree button
        button_c2r1 = Button(self, image=self.button_imgDisagree, borderwidth=0, highlightthickness=0,
                             command=lambda: self.disagree(button_c2r1, "c2r1", controller, "ICT", "Innovative"), relief="flat")
        button_c2r1.place(x=561.0, y=95.0, width=50.0, height=48.0)

        # creating c3r1 neutral button
        button_c3r1 = Button(self, image=self.button_imgNeutral, borderwidth=0, highlightthickness=0,
                             command=lambda: self.neutral(button_c3r1, "c3r1", controller, "ICT", "Innovative"), relief="flat")
        button_c3r1.place(x=680.0, y=103.0, width=35.0, height=33.0)

        # creating c4r1 agree button
        button_c4r1 = Button(self, image=self.button_imgAgree, borderwidth=0, highlightthickness=0,
                             command=lambda: self.agree(button_c4r1, "c4r1", controller, "ICT", "Innovative"), relief="flat")
        button_c4r1.place(x=784.0, y=95.0, width=50.0, height=48.0)

        # creating c5r1 strongly agree button
        button_c5r1 = Button(self, image=self.button_imgStronglyAgree, borderwidth=0, highlightthickness=0,
                             command=lambda: self.strongly_agree(button_c5r1, "c5r1", controller, "ICT", "Innovative"),relief="flat")
        button_c5r1.place(x=903.0, y=85.0, width=70.0, height=68.0)

        # creating c1r2 strongly disagree button
        button_c1r2 = Button(self, image=self.button_imgStronglyDisagree, borderwidth=0, highlightthickness=0,
                             command=lambda: self.strongly_disagree(button_c1r2, "c1r2", controller, "ABM", "Business Communication"),relief="flat")
        button_c1r2.place(x=422.0, y=216.0, width=70.0, height=68.0)

        # creating c2r2 disagree button
        button_c2r2 = Button(self, image=self.button_imgDisagree, borderwidth=0, highlightthickness=0,
                             command=lambda: self.disagree(button_c2r2, "c2r2", controller, "ABM", "Business Communication"), relief="flat")
        button_c2r2.place(x=561.0, y=226.0, width=50.0, height=48.0)

        # creating c3r2 neutral button
        button_c3r2 = Button(self, image=self.button_imgNeutral, borderwidth=0, highlightthickness=0,
                             command=lambda: self.neutral(button_c3r2, "c3r2", controller, "ABM", "Business Communication"), relief="flat")
        button_c3r2.place(x=680.0, y=234.0, width=35.0, height=33.0)

        # creating c4r2 agree button
        button_c4r2 = Button(self, image=self.button_imgAgree, borderwidth=0, highlightthickness=0,
                             command=lambda: self.agree(button_c4r2, "c4r2", controller, "ABM", "Business Communication"), relief="flat")
        button_c4r2.place(x=784.0, y=226.0, width=50.0, height=48.0)

        # creating c5r2 strongly agree button
        button_c5r2 = Button(self, image=self.button_imgStronglyAgree, borderwidth=0, highlightthickness=0,
                             command=lambda: self.strongly_agree(button_c5r2, "c5r2", controller, "ABM", "Business Communication"),relief="flat")
        button_c5r2.place(x=903.0, y=216.0, width=70.0, height=68.0)

        # creating c1r3 strongly disagree button
        button_c1r3 = Button(self, image=self.button_imgStronglyDisagree, borderwidth=0, highlightthickness=0,
                             command=lambda: self.strongly_disagree(button_c1r3, "c1r3", controller, "GAS", "Presentation"), relief="flat")
        button_c1r3.place(x=422.0, y=347.0, width=70.0, height=68.0)

        # creating c2r3 disagree button
        button_c2r3 = Button(self, image=self.button_imgDisagree, borderwidth=0, highlightthickness=0,
                             command=lambda: self.disagree(button_c2r3, "c2r3", controller, "GAS", "Presentation"), relief="flat")
        button_c2r3.place(x=561.0, y=357.0, width=50.0, height=48.0)

        # creating c3r3 neutral button
        button_c3r3 = Button(self, image=self.button_imgNeutral, borderwidth=0, highlightthickness=0,
                             command=lambda: self.neutral(button_c3r3, "c3r3", controller, "GAS", "Presentation"), relief="flat")
        button_c3r3.place(x=680.0, y=365.0, width=35.0, height=33.0)

        # creating c4r3 agree button
        button_c4r3 = Button(self, image=self.button_imgAgree, borderwidth=0, highlightthickness=0,
                             command=lambda: self.agree(button_c4r3, "c4r3", controller, "GAS", "Presentation"), relief="flat")
        button_c4r3.place(x=784.0, y=357.0, width=50.0, height=48.0)

        # creating c5r3 strongly agree button
        button_c5r3 = Button(self, image=self.button_imgStronglyAgree, borderwidth=0, highlightthickness=0,
                             command=lambda: self.strongly_agree(button_c5r3, "c5r3", controller, "GAS", "Presentation"), relief="flat")
        button_c5r3.place(x=903.0, y=347.0, width=70.0, height=68.0)

        # creating c1r4 strongly disagree button
        button_c1r4 = Button(self, image=self.button_imgStronglyDisagree, borderwidth=0, highlightthickness=0,
                             command=lambda: self.strongly_disagree(button_c1r4, "c1r4", controller, "HUMSS", "Creativity"), relief="flat")
        button_c1r4.place(x=422.0, y=479.0, width=70.0, height=68.0)

        # creating c2r4 disagree button
        button_c2r4 = Button(self, image=self.button_imgDisagree, borderwidth=0, highlightthickness=0,
                             command=lambda: self.disagree(button_c2r4, "c2r4", controller, "HUMSS", "Creativity"), relief="flat")
        button_c2r4.place(x=561.0, y=489.0, width=50.0, height=48.0)

        # creating c3r4 neutral button
        button_c3r4 = Button(self, image=self.button_imgNeutral, borderwidth=0, highlightthickness=0,
                             command=lambda: self.neutral(button_c3r4, "c3r4", controller, "HUMSS", "Creativity"), relief="flat")
        button_c3r4.place(x=680.0, y=497.0, width=35.0, height=33.0)

        # creating c4r4 agree button
        button_c4r4 = Button(self, image=self.button_imgAgree, borderwidth=0, highlightthickness=0,
                             command=lambda: self.agree(button_c4r4, "c4r4", controller, "HUMSS", "Creativity"), relief="flat")
        button_c4r4.place(x=784.0, y=489.0, width=50.0, height=48.0)

        # creating c5r4 strongly agree button
        button_c5r4 = Button(self, image=self.button_imgStronglyAgree, borderwidth=0, highlightthickness=0,
                             command=lambda: self.strongly_agree(button_c5r4, "c5r4", controller, "HUMSS", "Creativity"), relief="flat")
        button_c5r4.place(x=903.0, y=479.0, width=70.0, height=68.0)

        # creating c1r5 strongly disagree button
        button_c1r5 = Button(self, image=self.button_imgStronglyDisagree, borderwidth=0, highlightthickness=0,
                             command=lambda: self.strongly_disagree(button_c1r5, "c1r5", controller, "GAS", "Adaptability"),relief="flat")
        button_c1r5.place(x=422.0, y=610.0, width=70.0, height=68.0)

        # creating c2r5 disagree button
        button_c2r5 = Button(self, image=self.button_imgDisagree, borderwidth=0, highlightthickness=0,
                             command=lambda: self.disagree(button_c2r5, "c2r5", controller, "GAS", "Adaptability"), relief="flat")
        button_c2r5.place(x=561.0, y=620.0, width=50.0, height=48.0)

        # creating c3r5 neutral button
        button_c3r5 = Button(self, image=self.button_imgNeutral, borderwidth=0, highlightthickness=0,
                             command=lambda: self.neutral(button_c3r5, "c3r5", controller, "GAS", "Adaptability"), relief="flat")
        button_c3r5.place(x=680.0, y=628.0, width=35.0, height=33.0)

        # creating c4r5 agree button
        button_c4r5 = Button(self, image=self.button_imgAgree, borderwidth=0, highlightthickness=0,
                             command=lambda: self.agree(button_c4r5, "c4r5", controller, "GAS", "Adaptability"), relief="flat")
        button_c4r5.place(x=784.0, y=620.0, width=50.0, height=48.0)

        # creating c5r5 strongly agree button
        button_c5r5 = Button(self, image=self.button_imgStronglyAgree, borderwidth=0, highlightthickness=0,
                             command=lambda: self.strongly_agree(button_c5r5, "c5r5", controller, "GAS", "Adaptability"), relief="flat")
        button_c5r5.place(x=903.0, y=610.0, width=70.0, height=68.0)

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
    def strongly_disagree(self, button_pos, controller, strand, skill):
        # controller.strands_ratings[strand] += 1
        # controller.skills[strand][skill] += 1
        button_pos["image"] = self.button_imgStronglyDisagree_on

    # function for disagree button
    def disagree(self, button_pos, controller, strand, skill):
        # controller.strands_ratings[strand] += 2
        # controller.skills[strand][skill] += 2
        button_pos["image"] = self.button_imgDisagree_on

    # function for neutral button
    def neutral(self, button_pos, controller, strand, skill):
        # controller.strands_ratings[strand] += 3
        # controller.skills[strand][skill] += 3
        button_pos["image"] = self.button_imgNeutral_on

    # function for agree button
    def agree(self, button_pos, controller, strand, skill):
        # controller.strands_ratings[strand] += 4
        # controller.skills[strand][skill] += 4
        button_pos["image"] = self.button_imgAgree_on

    # function for strongly disagree button
    def strongly_agree(self, button_pos, controller, strand, skill):
        # controller.strands_ratings[strand] += 5
        # controller.skills[strand][skill] += 5
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
