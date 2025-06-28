from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Setting up main Window
root = Tk()
root.title('Denomination Counter')
root.configure(bg='light blue')
root.geometry('650x480')

# Adding Image and Labels in the Main Window
upload = Image.open("tally.img")
# Resize the image using resize() method
upload = upload.resize((300, 308))
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg='light blue')
label.place(x=180, y=20)

label1 = Label(root, text="HEY User! Welcome to Denomination Counter Application"
               bg='light blue'    )
label1.placeplace(relx=3.5, y=340, anchor=CENTER )

# Function to display a messagebox and proceed if OK is clicked
def msg():
    MsgBox = messagebox.showinfo(
        "Alert". "Do you want to calculate the denomination count?"
    )
    if Msgbox == 'ok':
        topwin()

# Adding Buttons to the main window
button1 = Button(root,
                 text="Let's get started.",
                 command=msg,
                 bg='brown',
                 fg='white'
)

# Function for opening new/top window
def topwin():
    top = Toplevel()
    top.title("Denominations Calculator")
    top.configure(bg='light grey')
    top.geometry("680x350+50+50")

    label = Label(top, text="Enter total amount,")