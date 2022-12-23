import sqlite3 as sql
import tkinter as tk
from tkinter import CENTER

class Keypad():
    def __init__(self, frame):
        framee= tk.Frame(frame)
        framee.pack()

        button1 = tk.Button(frame, text="1", width=5, height=2, command=self.button1).grid(row=0, column=0)
        button2 = tk.Button(frame, text="2", width=5, height=2, command=self.button2).grid(row=0, column=1)
        button3 = tk.Button(frame, text="3", width=5, height=2, command=self.button3).grid(row=0, column=2)
        button4 = tk.Button(frame, text="4", width=5, height=2, command=self.button4).grid(row=1, column=0)
        button5 = tk.Button(frame, text="5", width=5, height=2, command=self.button5).grid(row=1, column=1)
        button6 = tk.Button(frame, text="6", width=5, height=2, command=self.button6).grid(row=1, column=2)
        button7 = tk.Button(frame, text="7", width=5, height=2, command=self.button7).grid(row=2, column=0)
        button8 = tk.Button(frame, text="8", width=5, height=2, command=self.button8).grid(row=2, column=1)
        button9 = tk.Button(frame, text="9", width=5, height=2, command=self.button9).grid(row=2, column=2)
        button0 = tk.Button(frame, text="0", width=5, height=2, command=self.button0).grid(row=3, column=1)
    def button1(self):
        return 1

    def button2(self):
        return 2

    def button3(self):
        return 3

    def button4(self):
        return 4

    def button5(self):
        return 5

    def button6(self):
        return 6

    def button7(self):
        return 7

    def button8(self):
        return 8

    def button9(self):
        return 9

    def button0(self):
        return 0

    #root = tk.Tk()

    #frame = tk.Frame(width=500, height=200)


    #root.mainloop()