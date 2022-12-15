from tkinter import *
from pathlib import Path
from tkVideoPlayer import TkinterVideo
import pygame


# Frame for ICT page
class ICT(Frame):
    # constants
    pygame.mixer.init()
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")

    # ICT page class init method
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # creating the whole canvas of the frame
        canvas = Canvas(self, height=800, width=1360, bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x=0, y=0)

        # creating the background design for ICT page
        self.videoplayer = TkinterVideo(master=self, scaled=True)
        self.videoplayer.load("ResultPage/ICT/assets/ict.mp4")
        self.videoplayer.pack(expand=True, fill="both")
        self.videoplayer.play()

        # creating the see graph button
        self.button_imgSeeGraph = PhotoImage(file=self.relative_to_assets("button_SeeGraph.png"))
        button_SeeGraph = Button(self, image=self.button_imgSeeGraph, borderwidth=0, highlightthickness=0,
                                 command=lambda: controller.graph(), relief="flat")
        button_SeeGraph.place(x=1042.5, y=417.0, width=172.0, height=41.0)

        # creating the go back to home button
        self.button_imgHome = PhotoImage(file=self.relative_to_assets("button_Home.png"))
        button_Home = Button(self, image=self.button_imgHome, borderwidth=0, highlightthickness=0,
                             command=lambda: controller.show_frame("HomePage", controller.name), relief="flat")
        button_Home.place(x=1042.5, y=488.0, width=172.0, height=41.0)

        # creating the image for sound
        self.is_on = True
        self.on = PhotoImage(file=self.relative_to_assets("button_SoundsOn.png"))
        self.off = PhotoImage(file=self.relative_to_assets("button_SoundsOff.png"))

        # creating the button for sound
        self.button_Sound = Button(self, image=self.on, bd=0, command=self.switch, relief="flat")
        self.button_Sound.place(x=1168.0, y=0.0, width=192.0, height=91.0)

        self.play()

    # function for the right path
    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    # for playing the music
    def play(self):
        pygame.mixer.music.load("ResultPage/ICT/assets/song.mp3")
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
