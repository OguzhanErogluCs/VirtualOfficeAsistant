import datetime
import tkinter as tk
from tkvideo import tkvideo
import time


class FrameNotifications:
    def __init__(self, master):
        self.master = master

        self.labelframe = tk.LabelFrame(self.master.master, text="  Notifications  ", font="Helvetica 11 bold", bd=3,
                                        labelanchor="n")
        self.labelframe.pack(fill="both", expand="yes", side="left", padx=5, pady=5)

        self.listBox = tk.Listbox(self.labelframe, font="Helvetica 10 bold", bg="#EEEEEE", bd=0)
        self.listBox.pack(expand="1", fill="both", padx=10, pady=10, side="left")

        self.scrollbar = tk.Scrollbar(self.labelframe, orient="vertical", command=self.listBox.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.listBox.config(yscrollcommand=self.scrollbar.set)

        self.listBox.insert(tk.END,
                            time.strftime('%H:%M') + " --- " + " Hey, welcome! Let's fill your tasks for today. ")

        self.prevMouseCoords = 0, 0
        self.breakCounter()

        self.lastBreakTime = datetime.datetime.now()
        self.exerciseControl()

    def breakCounter(self):
        x, y = self.master.master.winfo_pointerxy()
        #print((x, y))
        #print(self.prevMouseCoords)
        if self.prevMouseCoords == (x, y):
            self.listBox.insert(tk.END, time.strftime('%H:%M') + " --- " + " You haven't been around for 10 seconds. ")
            self.listBox.insert(tk.END, "              How was your break? ")
            self.lastBreakTime = datetime.datetime.now()

        self.prevMouseCoords = x, y
        self.master.master.after(10000, self.breakCounter)  # call again 10000ms later

    def exerciseControl(self):


        if ((datetime.datetime.now() - self.lastBreakTime).seconds % 30) == 0 and ((datetime.datetime.now() - self.lastBreakTime).seconds >= 30):
            self.listBox.insert(tk.END, time.strftime('%H:%M') + " --- " + " Drinking water helps maintain the balance of body. ")
            self.listBox.insert(tk.END, "              Let's balance them. ")

        if (datetime.datetime.now() - self.lastBreakTime).seconds >= 60:
            self.listBox.insert(tk.END, time.strftime('%H:%M') + " --- " + " You have been working for 60 seconds.")
            self.listBox.insert(tk.END, "              Let's exercise for your health. ")
            self.lastBreakTime = datetime.datetime.now()
            self.exercisePopup()

        self.master.master.after(1000, self.exerciseControl)  # call again 1000ms later

    def exercisePopup(self):

        newWindow = tk.Toplevel(self.master.master)
        labelHeading = tk.Label(newWindow, text="Which exercise do you want to do?", font="Helvetica 20 bold")
        labelHeading.pack(side="top", padx=20, pady=20)

        tendonButton = tk.Button(newWindow,
                                 text=" Tendon Gliding Exercise ",
                                 fg="black", command=self.tendonPopup, font="Helvetica 10 bold")
        tendonButton.pack(anchor="s", side="left", padx=30, pady=10, ipadx=20)

        neckButton = tk.Button(newWindow,
                               text=" Neck Stretching Exercise ",
                               fg="black", command=self.neckPopup, font="Helvetica 10 bold")
        neckButton.pack(anchor="s", side="right", padx=30, pady=10, ipadx=20)

    def tendonPopup(self):

        newWindow = tk.Toplevel(self.master.master)
        labelHeading = tk.Label(newWindow, text="Tendon Gliding Exercise", font="Helvetica 20 bold")
        labelHeading.pack(side="top", padx=20, pady=20)
        label = tk.Label(newWindow)
        label.pack(side="top")
        labelInstructions = tk.Label(newWindow, text="Go through the sequence of \nfinger positions 10 times.\n Make "
                                                     "sure each movement flows\n into the next movement.",
                                     font="Helvetica 11 bold")
        labelInstructions.pack(side="bottom", pady=20)
        player = tkvideo("Tendon Gliding.mp4", label, loop=1, size=(320, 450))
        player.play()

        self.listBox.insert(tk.END, time.strftime('%H:%M') + " --- " + " Great! You have completed Tendon Gliding Exercise. ")

    def neckPopup(self):

        newWindow = tk.Toplevel(self.master.master)

        labelHeading = tk.Label(newWindow, text="Neck Stretching Exercise", font="Helvetica 20 bold")
        labelHeading.pack(side="top", padx=20, pady=20)

        label = tk.Label(newWindow)
        label.pack(side="top")

        player = tkvideo("Neck Pain.mp4", label, loop=1, size=(320, 420))
        player.play()

        self.listBox.insert(tk.END, time.strftime('%H:%M') + " --- " + " Cool! You have completed Neck Stretching Exercise.")
