# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 20:04:47 2022

@author: turtl_4
"""

from tkinter import *

root = Tk()
root.title("ASCII Converter With Encrpt")

root.geometry("400x400")
root.configure(background = "light blue")

input_word = Entry(root)
input_word.place(relx=0.5, rely=0.4, anchor=CENTER)

label_output = Label(root, text = "ASCII value : ", bg = 'light green', fg = 'black')
label_encrpt = Label(root)

def convert_code():
    input_text = input_word.get()
    label_output["text"]  = ""
    
    for letter in input_text :
        label_output["text"] += str(ord(letter)) + " "
        ASCII = int(ord(letter))
        encrpt = ASCII - 1
        label_encrpt["text"] += str(chr(encrpt))
        
        

btn = Button(root,text = "Display the ASCII Code and Encrypted value", command = convert_code,bg = 'gold', fg = 'black')
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

label_output.place(relx=0.5, rely=0.6, anchor=CENTER)
label_encrpt.place(relx=0.5, rely=0.7, anchor=CENTER)

root.mainloop()