from cProfile import label
from tkinter import *
from functools import partial
import random

class Start:
    def __init__(self,parent):

        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()
        
        #mystery box label
        self.mystery_box_label = Label(self.start_frame, text="Mystery Box Game", font= "Arial 19 bold")
        self.mystery_box_label.grid(row=1)
        
        #entry box
        self.start_entry = Entry(self.start_frame, font="Arial 16")
        self.start_entry.grid(row=2)
        
        #low stakes button
        self.low_stakes = Button(text="Low ($5)", command=lambda: self.to_game (1))
        self.low_stakes.grid(row=3, pady=10)

    def to_game(self, stakes):
        start_balance = self.start_entry.get()
        Game(self, stakes, start_balance)

class Game:
    def __init__(self, partner, stakes, start_balance):
        print(stakes)
        print(start_balance)
        
        partner.lowstakes_button.config(state=DISABLED)
        
        #initialise variables
        self.balance = IntVar()

        #set start balance
        self.balance.set(start_balance)

        #game box
        self.game_box = Toplevel()
        self.game_frame = Frame(self.game_box)
        self.game_frame.grid()
        
        #heading row
        self.heading_label = Label(self.game_frame, text="Heading", font="arial 12 bold", padx=10, pady=10)
        self.heading_label.grid(row=0)

        #balance label
        self.balance_label = Label(self.game_frame, text="balance", font="arial 12 bold", padx=10, pady=10)
        self.balance_label.grid(row=2)

        #play button
        self.play_button = Button(self.game_frame, text="Gain", padx=10, pady=10, command=self.show_boxes)
        self.play_button.grid(row=4)

    def show_boxes(self):
        current_balance = self.balance.get
        current_balance += 2

# main routine
    if __name__ == "__main__":
        root = Tk()
        root.title("title goes here")
        something = Start(root)
        root.mainloop()
