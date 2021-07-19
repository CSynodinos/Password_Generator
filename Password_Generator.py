# Generates random passwords and stores them in a .csv file named Generated_Passwords.csv.

import random
import os
import pandas as pd
import tkinter.messagebox
from tkinter import ttk
from tkinter import *
import os

def Password():
    """Function that extracts the inputs. By assignin the inputs as globals, they get extracted from the function and 
    can be used in the while loop and in the .to_csv method."""
    
    password_len_temp = e1.get()
    password_description = e2.get()
        
    
    if password_len_temp.isnumeric():   # Check numeric.
        password_len = int(password_len_temp)
    else:
        tkinter.messagebox.showerror("Error", "Please insert numbers only!")
            
    if password_len > 0:    # Natural numbers.
        pass
    else:
        tkinter.messagebox.showerror("Error", "Please insert Natural numbers only!")

        
    # Password characters
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!#$%^&*()"

    while True: # Generates the passwords. 
        password= ""
        for x in range(0, password_len):
            password_character = random.choice(characters)  # pick randomly from characters.
            password  = password + password_character
        break
        
    Passwords_Save = pd.DataFrame([[password_description, password]])   # Output in Dataframe.
    Column_Titles = ['Description', 'Password']
    File_Name = 'Generated_Passwords.csv'

    
    if os.path.isfile(File_Name):   # Check if .csv for passwords exists.
        with open(File_Name) as f:
            Passwords_Save.to_csv('Generated_Passwords.csv', mode= 'a', index=False, header=None)
            f.close()
    else:
        Passwords_Save.to_csv('Generated_Passwords.csv', mode= 'a', index=False, header=Column_Titles)

    tkinter.messagebox.showinfo("Status", "Password has been generated successfully!")

    return Passwords_Save


def on_closing():
    """Pop-up window if the close button (X) is pressed."""
    
    if tkinter.messagebox.askokcancel("Exit", "Do you want to quit?"):
        root.destroy()
        exit()
    else:
        pass

if __name__=="__main__":
    root = Tk()
    root.title("Password Generator")

    # Input 1.
    labelText1=StringVar()
    labelText1.set("Password character size")
    labelDir=Label(root, textvariable=labelText1, height=2)
    labelDir.pack()
    directory1=StringVar(None)
    e1=Entry(root,textvariable=directory1,width=50)
    e1.pack()

    # Input 2.
    labelText2=StringVar()
    labelText2.set("Password Description")
    labelDir=Label(root, textvariable=labelText2, height=2)
    labelDir.pack()
    directory2=StringVar(None)
    e2=Entry(root,textvariable=directory2,width=50)
    e2.pack()
    
    # Run button.
    myButton = Button(root, text = "GENERATE", command = lambda: Password())

    myButton.pack()
    
    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()