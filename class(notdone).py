import tkinter as tk
from tkinter import *
import random
class RandomSeatingClass:
    def __init__(self, name):
        self.name = name
        name.title = "Hello random chỗ ngồi nè!!"
        self.student = []
        self.seatingFrame = tk.Frame(name)
        self.seatingFrame.pack(padx=10, pady=10)
        self.seatingTable()
        self.student_label = tk.Label(name, text=self.name)
        self.student_label.pack(pady=10)

        self.random_button = tk.Button(name, text="Random học sinh", command=self.randomSeating)
        self.random_button.pack()
        
    def seatingTable(self):
        for i in range(12):
            for j in range(6):
                label = tk.Label(self.seatingFrame, bg = "pink", padx = 15, pady = 15, borderwidth = 1,relief="solid")
                label.grid(row = j,column = i, padx=5, pady=5)
                if j == 1 or 2 and i == 2 or 9:
                    label.destroy([j for j in label])
                elif j in range(3,6) and i == 2 or i in range(5,7) or i == 9:
                    label.destroy([j for j in label])
                
        
            
            
    
    def randomSeating(self):
        randomSeating = random.choice(self.students)
        self.student_label.config(text=randomSeating)

root = tk.Tk()
app = RandomSeatingClass(root)
root.mainloop()
        
        
        