#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 21:48:25 2019

@author: robert
"""

from tkinter import *

def ceasar (text, code=3):
    new_text = ""
    for letter in text:
        if ("a" <= letter and letter <= "z"):
            number = ord(letter)
            new_number = number + code
            if new_number > ord("z"):
                new_number = new_number - ord("z") + ord("a") -1
                
            new_text += chr(new_number)
            
            
        elif ("A" <= letter and letter <= "Z"):
            number = ord(letter)
            new_number = number + code
            if new_number > ord("Z"):
                new_number = new_number - ord("Z") + ord("A") -1
                
            new_text += chr(new_number)
        
        else:
            new_text += chr(new_number)
            
    return new_text            


def coding():
    code = codeChoice.get()
    text = textBox.get(1.0, END)
    newTextBox.config(state=NORMAL)
    newTextBox.delete(1.0, END)
    newTextBox.insert(END, ceasar(text, code))
    newTextBox.config(state=DISABLED)
    
    
def encode():
    code = codeChoice.get()
    text = textBox.get(1.0, END)
    newTextBox.config(state=NORMAL)
    newTextBox.delete(1.0, END)
    newTextBox.insert(END, ceasar(text, 26-code))
    newTextBox.config(state=DISABLED)
    
window = Tk()

window.title("Caesar Coding")
window.resizable(width=False, height=False)

header = Label(window, pady=5, font="Arial, 16", text= "Caesar Coding")

header.pack()

textFrame = LabelFrame(window, text ="Text", padx=5, pady=5)
textFrame.pack(padx=10, pady=10, fill=BOTH)
textBox= Text(textFrame, height=6, width=50)
textBox.pack(fill=BOTH)

adjustedFrame = Frame(window)
adjustedFrame.pack()

codeChoice = Scale(adjustedFrame, label = "Code:", orient=HORIZONTAL, from_ = 0, to=26, length=200)

codeChoice.set(3)

codeChoice.pack(side=TOP)

# code for producing the buttons
codeButton = Button(adjustedFrame, text= "Code", command=coding)
codeButton.pack(side=LEFT, padx=10, pady=10)
encodeButton = Button(adjustedFrame, text= "Encode", command=encode)
encodeButton.pack(side=LEFT, padx=10, pady=10)


newTextFrame =LabelFrame(window, text= "Encoded or coded Text", padx=5, pady=5)
newTextFrame.pack(padx=10, pady=10, fill=BOTH)
newTextBox = Text(newTextFrame, height=6, width=50, state=DISABLED)
newTextBox.pack(fill=BOTH)


window.mainloop()






















               
               
               
               
               
               
               
            
    
    
    
