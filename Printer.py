import sqlite3 as sql
import tkinter as tk
from tkinter import *
import random as rand
from Keypad import Keypad



root = tk.Tk()
root.geometry("500x500")
text_receipt = "Fatura ister misiniz?"
label_receipt = tk.Label(root, width=30, height=3, text=text_receipt, font="bold")
label_receipt.grid(row=0, column=0, padx=60, pady=1)
button = tk.Button(root, text="Evet", height=5, width=30)
button = tk.Button(root, text="Hayır", height=2, width=15)
button_evet = tk.Button(root, width=20, height=3, background="white", text="Evet", highlightthickness=3,highlightbackground="blue")
button_evet.grid(row=1, column=0, padx=50, pady=2)
button_hayır = tk.Button(root, width=20, height=3, background="white", text="Hayır",highlightthickness=3,highlightbackground="blue")
button_hayır.grid(row=2, column=0, padx=50, pady=3)


root.mainloop()


