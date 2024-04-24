##Step 1: Create a new Python file and import the necessary modules

from tkinter import *
from tkinter import messagebox as mb
import random

##def read_lines(filename):
##    with open(filename, 'r') as file:
##        lines = file.readlines()
##    return lines


##Step 3: Call the function to read the text from the file

## lines = read_lines('words_of_kindness.txt')

lines=["The joy that you are lights up the world",
"You are brilliant",
"You are kind",
"You are fun",
"You are a pleasure to be around",
"Remember the sheer brilliance that you are",
"Your joy lights up the world",
"Your intelligence is needed",
"You are amazing",
"You are loving",
"You are strong",
"It's gonna be ok",
"You can do it",
"You are compassionate",
"Deep Breath"]

##Step 4: Create a function to display a message box with the text


def show_message_box():
    mb.showinfo('Words of Kindness AlphaV', random.choice(lines))

##Step 5: Create a new window with a button to display the message box

root = Tk()
root.title('File text')

button = Button(root, text='Start Kindness Game', command=show_message_box)
button.pack()

root.mainloop()
