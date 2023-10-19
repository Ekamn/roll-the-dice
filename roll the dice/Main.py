# - one arm bandit 
# - Ekamneet Sandhu -
# March 2023

# - 
# -- Import Libraries --
import time
from tkinter import * 
from PIL import Image, ImageTK

dice1 = 0
dice2 = 0
animateRoll = True
diceimages1 = Image.open (str(dice1)+".jpg ")

def exitGUI():
    window.destroy()  # Closes main window

import random 

def roll():
    dice1 = random.randint(1,6) 
    dice2 = random.randint(1,6)
    print (dice1)
    print (dice2)
    

def displayImages(dice1, dice2):
    print()


def displayImages(dice1, dice2):
    #function code here
    print("this is a function")

if dice1 == 1 and dice2 == 1:
    message = "Snake Eyes"

elif dice1 == 6 and dice2 == 6:
    message = "Box Cars"

else: 
    if animateRoll:
        for num in range(3):
            diceimages1 = Image.open (str(dice1)+".jpg ")
            displayimage1 = ImageTK.PhotoImage(diceimages1)
        for Dice in range (6):
            print()

def displayImages():
 global image_1
 global ImageTk
 global lbl_dice1
 global lbl_dice2
 global image_2
 global display_image
 display_image1 = ImageTk.PhotoImage(image_1)
 lbl_dice1.config(image=display_image)
 lbl_dice1.image = display_image1

 display_image2 = ImageTk.PhotoImage(image_2)
 lbl_dice2.config(image=display_image)
 lbl_dice2.image = display_image2

# -- Define GUI --


# Build the Main Window
window = Tk()  # Creates a GUI window and gives it a name
window.title('one arm bandit  - Ekam')  # Window title bar text 
window.configure(bg='#afeeef')  # Window options
window.geometry('600x300')  # Sets the window size and position

# Create and Place Widgets
window.configure(bg='#afeeef')  # Window options
window.geometry('600x300')  # Sets the window size and position

# Labels
# Name, Style, Location

# -- Mainline --
window.configure(bg='#afeeef')  # Window options
window.geometry('600x300')  # Sets the window size and position

lblDice1 = Label(window,text = "",font=("default",14),fg = "black",bg="White" )
lblDice1.place(x=25, y=25, width=200,height=200)

lblDice2 = Label(window,text = "",font=("default",14),fg = "black",bg="White" )
lblDice2.place(x=25, y=25, width=200,height=200)
 
lblDice3 = Label(window,text = "",font=("default",14),fg = "black",bg="White" )
lblDice3.place(x=25, y=25, width=200,height=200)

lblDice4 = Label(window,text = "",font=('default',14),fg = "black",bg="White")
lblDice4.place(x=25, y=25, width=200,height=200)

lblDice5 = Label (window,text = "" ,font=('default',14),fg = "black",bg="White")

firstWheel = Image.open("1.jpg")
secondWheel = Image.open("2.jpg")
thirdWheel = Image.open("3.jpg")

def ChangeThisNameLater():
    global firstWheel, secondWheel, thirdWheel
    if((firstWheel == "CHERRY") and (secondWheel != "CHERRY")):
            win = 2
    elif((firstWheel == "CHERRY") and (secondWheel == "CHERRY") and (thirdWheel != "CHERRY")):
            win = 5
    elif((firstWheel == "CHERRY") and (secondWheel == "CHERRY") and (thirdWheel == "CHERRY")):
            win = 7
    elif((firstWheel == "ORANGE") and (secondWheel == "ORANGE") and ((thirdWheel == "ORANGE") or (thirdWheel == "BAR"))):
            win = 10
    elif((firstWheel == "PLUM") and (secondWheel == "PLUM") and ((thirdWheel == "PLUM") or (thirdWheel == "BAR"))):
            win = 14
    elif((firstWheel == "BELL") and (secondWheel == "BELL") and ((thirdWheel == "BELL") or (thirdWheel == "BAR"))):
            win = 20
    elif((firstWheel == "BAR") and (secondWheel == "BAR") and (thirdWheel == "BAR")):
            win = 25

btn_roll = Button(window)