import datetime
import threading
import tkinter as tk
import imageio
from PIL import ImageTk, Image
from tkvideo import tkvideo


class FrameNotifications:
    def __init__(self, master):
        self.master = master

        self.labelframe = tk.LabelFrame(self.master.master, text="  Notifications  ", font="Helvetica 11 bold", bd=3,
                                        labelanchor="n")
        self.labelframe.pack(fill="both", expand="yes", side="left", padx=5, pady=5)

        self.listBox = tk.Listbox(self.labelframe, font="Helvetica 10", bg="#EEEEEE", bd=0)
        self.listBox.pack(expand="1", fill="both", pady=10, side="left")

        self.scrollbar = tk.Scrollbar(self.labelframe, orient="vertical", command=self.listBox.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.listBox.config(yscrollcommand=self.scrollbar.set)

        self.listBox.insert(tk.END, " Hey, welcome! Let's fill your tasks for today. ")

        self.prevMouseCoords = 0, 0
        self.breakCounter()

        self.lastBreakTime = datetime.datetime.now()
        self.exerciseControl()

        self.video = imageio.get_reader("Tendon Gliding.mp4")

    def breakCounter(self):
        x, y = self.master.master.winfo_pointerxy()
        print((x, y))
        print(self.prevMouseCoords)
        if self.prevMouseCoords == (x, y):
            self.listBox.insert(tk.END, " You haven't been around for 20 seconds. How was your break?")
            self.lastBreakTime = datetime.datetime.now()

        self.prevMouseCoords = x, y
        self.master.master.after(20000, self.breakCounter)  # call again 20000ms later

    def exerciseControl(self):

        if (datetime.datetime.now() - self.lastBreakTime).seconds >= 30:
            self.listBox.insert(tk.END, " You have been working for 30 seconds.")
            self.listBox.insert(tk.END, " Let's exercise for your health. ")
            self.lastBreakTime = datetime.datetime.now()
            self.createNewWindow()
        self.master.master.after(1000, self.exerciseControl)  # call again 10000ms later

    def createNewWindow(self):
        newWindow = tk.Toplevel(self.master.master)
        labelHeading = tk.Label(newWindow, text="Tendon Gliding Exercise", font="Helvetica 20 bold")
        labelHeading.pack(side="top",padx=20, pady=20)
        label = tk.Label(newWindow, text="New Window")
        label.pack(side="top")
        labelInstructions = tk.Label(newWindow, text="Go through the sequence of \nfinger positions 10 times.\n Make "
                                                     "sure each movement flows\n into the next movement.",
                                     font="Helvetica 11")
        labelInstructions.pack(side="bottom", pady=20)
        player = tkvideo("Tendon Gliding.mp4", label, loop=1, size=(320, 450))
        player.play()
