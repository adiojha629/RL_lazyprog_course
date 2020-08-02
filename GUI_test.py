# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 14:33:43 2020
Making some buttons for tic,tac,toe
@author: Aditya Ojha
"""
import tkinter as tk
from tkinter import messagebox
window = tk.Tk()
window.geometry("1000x1000")
def sayHello():
    messagebox.showinfo("Hello Python","Hello World")
def click():
    myLabel = tk.Label(window,text = "I clicked a button")
    myLabel.pack()
h = 25
w = 25
button = tk.Button(window,text = "Press Me!!!",command = sayHello,padx=h,pady=w)
button2 = tk.Button(window,text = "PRESSS MEEEEEE",command = click,bg="blue",fg="red")
button.pack()
button2.pack()
window.mainloop()