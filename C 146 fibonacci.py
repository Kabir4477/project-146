# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 15:21:13 2023

@author: drsau
"""

from tkinter import *

root=Tk()

root.title("Fibonacci")
root.geometry("1000x400")

number = Entry(root)
label_series = Label(root, text = "Fibonacci Series: ")
label_flower = Label(root)
label_spiral = Label(root)

def Fibonacci():
    label_series["text"] =  "Fibonacci Series: "

    num = int(number.get())
    first_no = 0
    second_no = 1
    sum = 0
    counter = 1
    while (counter <= num):
        label_series["text"] += str(sum) + " "
        counter = counter + 1
        first_no = second_no
        second_no = sum
        sum = first_no + second_no
    
    label_spiral["text"] =   " Febonacci sum:  " + str(first_no) + "  +  "  +str(second_no) +  "  =  "  + str(sum)

btn = Button(root , text="Show Fibonacci Series", command=Fibonacci)
btn.pack()
number.pack()
label_series.pack()
label_flower.pack()
label_spiral.pack()

root.mainloop()
