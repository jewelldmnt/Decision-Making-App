# importing the required libraries/modules
from tkinter import *
from pathlib import Path


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def get_username():
    Name = entry_Name.get()
    #if Name is '':
    clear_entries()

def clear_entries():
    entry_Name.delete(0, END)


# class for the main frame

# path file for the assets
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./Start page/assets")

# initialize main window app
window = Tk()
window.geometry("1360x800")
window.configure(bg="#FFFFFF")

# creating the whole canvas of the frame
canvas = Canvas(window, bg="#FFFFFF", height=800, width=1360, bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)

# creating the background design for start page
image_bg = PhotoImage(file=relative_to_assets("bg.png"))
canvas.create_image(680.0, 401.0, image=image_bg)

# creating the background design for the name entry
image_bgEntry = PhotoImage(file=relative_to_assets("bgEntry.png"))
canvas.create_image(679.0, 276.0, image=image_bgEntry)

# creating name of the user entry
entry_imgName = PhotoImage(file=relative_to_assets("entry_Name.png"))
canvas.create_image(682.5, 420.5, image=entry_imgName)
entry_Name = Entry(bd=0, bg="#D6EBF6", fg="#000716", highlightthickness=0)
entry_Name.place(x=437.0, y=400.0, width=491.0, height=39.0)

# creating the submit button
button_imgSubmit = PhotoImage(file=relative_to_assets("Submit.png"))
button_Submit = Button(image=button_imgSubmit, borderwidth=0, highlightthickness=0,
                       command=lambda: get_username(), relief="flat")
button_Submit.place(x=638.0, y=469.0, width=113.0, height=40.0)

window.resizable(False, False)
window.mainloop()


