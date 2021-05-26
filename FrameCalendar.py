import tkinter as tk
from tkinter import StringVar

from tkcalendar import Calendar


class FrameCalendar():

    def __init__(self, master):
        self.master = master

        self.dayTaskDict = {}

        self.previousDay = ""

        labelframe = tk.LabelFrame(self.master.master, text="  Calendar  ",font = "Helvetica 11 bold", bd= 3, labelanchor = "n")
        labelframe.pack(fill="x", side="bottom", padx=5, pady=5)

        self.tasks = tk.LabelFrame(labelframe, text=" Tasks ",font = "Helvetica 10 bold", labelanchor = "nw", bd= 3)
        self.tasks.pack(fill="both", expand="yes", side="left", padx=5, pady=5)

        self.staticText = StringVar(self.master.master, Calendar.date.today().strftime("%d/%m/%y"))

        self.cal = Calendar(labelframe, selectmode='day',
                            date_pattern='dd/mm/yy', textvariable=self.staticText)
        self.cal.pack(side="right", padx=10, pady=10)

        self.dynamic_label = tk.Label(self.tasks, textvariable=self.staticText, font = "Helvetica 15 bold").pack(side="top")

        self.TaskText = StringVar(self.tasks)

        self.taskEntry = tk.Entry(self.tasks, textvariable=self.TaskText)
        self.taskEntry.pack(fill="x", expand="yes", side="top", padx=20, pady=5)

        self.listBox = tk.Listbox(self.tasks)
        self.listBox.pack(pady=5, fill="both", padx=20)

        self.master.master.bind('<Button-1>', self.mouseClicked)

        self.taskButton = tk.Button(self.tasks,
                                    text=" + Add",
                                    fg="black", command=self.taskButtonClicked, font = "Helvetica 10 bold")
        self.taskButton.pack(anchor="s", side="left", padx=30, pady=10, ipadx=20)

        self.deleteTask = tk.Button(self.tasks,
                                    text=" - Delete",
                                    fg="black", command=self.deleteSelectedItem, font = "Helvetica 10 bold")
        self.deleteTask.pack(anchor="s", side="right", padx=30, pady=10, ipadx=20)

        """self.scrollbar = tk.Scrollbar(self.tasks, orient="vertical")
        self.scrollbar.config(command=self.listBox.yview)
        self.scrollbar.pack(anchor="ne",side="top", fill="y")

        self.listBox.config(yscrollcommand=self.scrollbar.set) """


    def taskButtonClicked(self):

        theDay = self.staticText.get()
        self.TaskText.set(self.taskEntry.get())
        if self.taskEntry.get() != "":
            if theDay in self.dayTaskDict.keys():
                self.dayTaskDict[theDay].append(self.TaskText.get())

            else:
                self.dayTaskDict[theDay] = []
                self.dayTaskDict[theDay].append(self.TaskText.get())

            self.insertListElements()
            self.taskEntry.delete(0, 'end')  # delete enrty after submitting it.

    def mouseClicked(self, event):
        # print("mouse clicked")
        theDay = self.staticText.get()

        if self.previousDay != self.staticText.get():
            #print("gun degisti")
            if theDay in self.dayTaskDict.keys():
                self.insertListElements()
            else:
                self.listBox.delete(0, 'end')
        #else:
            #print("gun degismedi")

        self.previousDay = self.staticText.get()

    def insertListElements(self):

        theDay = self.staticText.get()
        self.listBox.delete(0, 'end')
        for i in self.dayTaskDict[theDay]:
            self.listBox.insert(tk.END, i)

    def deleteSelectedItem(self):

        theDay = self.staticText.get()
        if (self.listBox.curselection()):
            self.dayTaskDict[theDay].remove(
                self.dayTaskDict[theDay][self.listBox.curselection()[0]])  # delete selected items from dict
            self.listBox.delete(tk.ANCHOR)  # delete selected items from listbox

