##Step 1: Create a new Python file and import the necessary modules


from tkinter import *
from tkinter import messagebox as mb

##Step 2: Create a function to read the text from the file

def read_text(file_path):
    with open(file_path, 'r') as f:
        text = f.read()
    return text

##Step 3: Call the function to read the text from the file

text = read_text('words_of_kindness.txt')

##Step 4: Create a function to display a message box with the text


def show_message_box():
    mb.showinfo('Words of Kindness AlphaV', text)

##Step 5: Create a new window with a button to display the message box

root = Tk()
root.title('File text')

button = Button(root, text='Display text', command=show_message_box)
button.pack()

root.mainloop()


