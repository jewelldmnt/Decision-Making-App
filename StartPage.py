from tkinter import *
from pathlib import Path
import pygame

# Frame for start page
class StartPage(Frame):
    # constants
    pygame.mixer.init()
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("StartPage_assets/assets")

    # start page class init method
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # image for error
        self.img_error = PhotoImage(file=self.relative_to_assets("error.png"))

        # creating the whole canvas of the frame
        canvas = Canvas(self, bg="#FFFFFF", height=800, width=1360, bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x=0, y=0)

        # creating the background design for start page
        self.image_bg = PhotoImage(file=self.relative_to_assets("bg.png"))
        canvas.create_image(680.0, 401.0, image=self.image_bg)

        # creating the background design for the name entry
        self.image_bgEntry = PhotoImage(file=self.relative_to_assets("bgEntry.png"))
        canvas.create_image(679.0, 276.0, image=self.image_bgEntry)

        # creating name of the user entry
        self.name = StringVar()
        self.name.trace("w", self.reset_bg1_border)
        self.entry_imgName = PhotoImage(file=self.relative_to_assets("entry_Name.png"))
        self.entry_img = Label(self, image=self.entry_imgName, bg="#D6EBF6")
        self.entry_img.place(x=425, y=390)
        self.entry_Name = Entry(self, textvariable=self.name, bd=0, bg="#D6EBF6", fg="#000716", highlightthickness=0)
        self.entry_Name.place(x=437.0, y=393.0, width=491.0, height=39.0)

        # creating the error message
        self.errorMsg = Label(canvas, anchor="nw", bg="#B5E2FA", fg="#FF0F0F", font=("Schoolbell Regular", 15 * -1))
        self.errorMsg.place(x=418, y=458)

        # creating the submit button
        self.button_imgSubmit = PhotoImage(file=self.relative_to_assets("Submit.png"))
        button_Submit = Button(self, image=self.button_imgSubmit, borderwidth=0, highlightthickness=0,
                               command=lambda: self.get_username(controller), relief="flat")
        button_Submit.place(x=638.0, y=469.0, width=113.0, height=40.0)

        # creating the image for sound
        self.is_on = True
        self.on = PhotoImage(file=self.relative_to_assets("button_SoundsOn.png"))
        self.off = PhotoImage(file=self.relative_to_assets("button_SoundsOff.png"))

        # creating the button for sound
        self.button_Sound = Button(self, image=self.on, bd=0, command=self.switch, relief="flat")
        self.button_Sound.place(x=871.0, y=269.0, width=101.0, height=28.0)

        self.play()

    # function for the right path
    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    # function for storing the user name
    def get_username(self, controller):
        name = self.entry_Name.get()
        if name == "":
            self.errorMsg["text"] = "This field is required."
            self.entry_img["image"] = self.img_error
            return
        controller.show_frame("HomePage", name)
        self.clear_entries()

    # function for clearing entries
    def clear_entries(self):
        self.entry_Name.delete(0, END)

    # function for clearing the error message
    def reset_bg1_border(self, *args):
        self.entry_img.configure(image=self.entry_imgName)
        self.errorMsg.configure(text="")

    # for playing the music
    def play(self):
        pygame.mixer.music.load("StartPage_assets/assets/song.mp3")
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
