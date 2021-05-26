import datetime
import tkinter as tk
import win32api


class FrameNotifications:
    def __init__(self, master):
        self.master = master

        self.labelframe = tk.LabelFrame(self.master.master, text="  Notifications  ", font="Helvetica 11 bold", bd=3,
                                        labelanchor="n")
        self.labelframe.pack(fill="both", expand="yes", side="left", padx=5, pady=5)

        self.listBox = tk.Listbox(self.labelframe, font="Helvetica 10",bg = "#EEEEEE", bd =0)
        self.listBox.pack(expand="1", fill="both", pady=10, side="left")

        self.scrollbar = tk.Scrollbar(self.labelframe, orient="vertical", command=self.listBox.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.listBox.config(yscrollcommand=self.scrollbar.set)

        self.listBox.insert(tk.END, " Hey, welcome! Let's fill your tasks for today. ")

        self.prevMouseCoords = 0, 0
        self.breakCounter()

        self.lastBreakTime = datetime.datetime.now()
        self.exerciseControl()


    def breakCounter(self):
        x, y = self.master.master.winfo_pointerxy()
        print((x, y))
        print(self.prevMouseCoords)
        if self.prevMouseCoords == (x, y):
            self.listBox.insert(tk.END, " You haven't been around for 10 seconds. How was your break?")
            self.lastBreakTime = datetime.datetime.now()

        self.prevMouseCoords = x, y
        self.master.master.after(10000, self.breakCounter)  # call again 10000ms later

    def exerciseControl(self):
        print(type(datetime.datetime.now()))
        print((datetime.datetime.now() - self.lastBreakTime).seconds)
        if (datetime.datetime.now() - self.lastBreakTime).seconds >= 15:
            self.listBox.insert(tk.END, " You have been working for 15 seconds. Let's exercise for your health.")
            self.listBox.insert(tk.END, " Let's exercise for your health. ")
            self.lastBreakTime = datetime.datetime.now()

        self.master.master.after(1000, self.exerciseControl)  # call again 10000ms later

