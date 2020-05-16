import os
import time
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("message")
root.withdraw()

m = 0
s = 0

def continuation():
    x = messagebox.askquestion("timer","Do you wanna continue or log-off ?")
    if x == "yes" : 
        pass  
    else : 
        exit()

while s<=1200:
    time.sleep(1)
    s+=1
    if s==1200:
        continuation()
        m+=1
        s=0
    
