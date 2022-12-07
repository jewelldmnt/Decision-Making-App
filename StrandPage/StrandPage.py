from tkinter import *
from pathlib import Path
import pygame


# Frame for strand page
class StrandPage(Frame):
    # constants
    pygame.mixer.init()
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")

    # start page class init method
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # creating the whole canvas of the frame
        self.canvas = Canvas(self, bg="#B5E2FA", height=800, width=1360, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

        # creating the background design for strand page
        self.image_bg = PhotoImage(file=self.relative_to_assets("bg.png"))
        self.canvas.create_image(685.0, 442.0, image=self.image_bg)

        # image for ABM
        self.image_ABM_bg = PhotoImage(file=self.relative_to_assets("image_ABM_bg.png"))

        # image for STEM
        self.image_STEM_bg = PhotoImage(file=self.relative_to_assets("image_STEM_bg.png"))

        # image for GAS
        self.image_GAS_bg = PhotoImage(file=self.relative_to_assets("image_GAS_bg.png"))

        # image for HUMSS
        self.image_HUMSS_bg = PhotoImage(file=self.relative_to_assets("image_HUMSS_bg.png"))

        # image for ICT
        self.image_ICT_bg = PhotoImage(file=self.relative_to_assets("image_ICT_bg.png"))


        # calling of the strand image
        self.show_strand(controller)

        # creating the white wavy top background
        self.image_top_bg = PhotoImage(file=self.relative_to_assets("image_top_bg.png"))
        self.canvas.create_image(681.0, 68.0, image=self.image_top_bg)

        # creating the back to home button
        self.button_imgHome = PhotoImage(file=self.relative_to_assets("button_home.png"))
        button_home = Button(self, image=self.button_imgHome, borderwidth=0, highlightthickness=0,
                             command=lambda: controller.show_frame("HomePage", controller.name, controller.strand), relief="flat")
        button_home.place(x=131.0, y=35.0, width=225.0, height=42.0)

        # creating the image for sound
        self.is_on = True
        self.on = PhotoImage(file=self.relative_to_assets("button_SoundsOn.png"))
        self.off = PhotoImage(file=self.relative_to_assets("button_SoundsOff.png"))

        # creating the button for sound
        self.button_Sound = Button(self, image=self.on, bd=0, command=self.switch, relief="flat")
        self.button_Sound.place(x=1155.0, y=35.0, width=174.0, height=48.0)

        self.play()

    # function for the right path
    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    def show_strand(self, controller):
        strand = controller.strand
        if strand == "ABM":
            self.canvas.create_image(134.0, 442.0, image=self.image_ABM_bg)
        elif strand == "STEM":
            self.canvas.create_image(1226.0, 442.0, image=self.image_STEM_bg)
        elif strand == "GAS":
            self.canvas.create_image(408.01043701171875, 442.0, image=self.image_GAS_bg)
        elif strand == "HUMSS":
            self.canvas.create_image(682.96728515625, 442.0, image=self.image_HUMSS_bg)
        elif strand == "ICT":
            self.canvas.create_image(959.0, 442.0, image=self.image_ICT_bg)

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
