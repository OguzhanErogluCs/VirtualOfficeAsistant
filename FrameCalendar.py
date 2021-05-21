import tkinter as tk
from tkinter import StringVar
from tkcalendar import Calendar


class FrameCalendar():

    def __init__(self, master):
        self.master = master

        self.dayTaskDict = {}

        self.previousDay = ""

        labelframe = tk.LabelFrame(self.master.master, text="Calendar")
        labelframe.pack(fill="x", side="bottom")

        self.tasks = tk.LabelFrame(labelframe, text="Tasks")
        self.tasks.pack(fill="both", expand="yes", side="left")

        self.staticText = StringVar(self.master.master, Calendar.date.today().strftime("%d/%m/%y"))

        self.cal = Calendar(labelframe, selectmode='day',
                            date_pattern='dd/mm/yy', textvariable=self.staticText)
        self.cal.pack(side="right")

        self.dynamic_label = tk.Label(self.tasks, textvariable=self.staticText, font=12).pack(side="top")

        self.TaskText = StringVar(self.tasks)

        self.taskEntry = tk.Entry(self.tasks, textvariable=self.TaskText)
        self.taskEntry.pack(fill="x", expand="yes", side="top")

        self.taskButton = tk.Button(self.tasks,
                                    text="Add Task",
                                    fg="black", command=self.taskButtonClicked)
        self.taskButton.pack(side="bottom")

        """self.showTasks = tk.Button(self.tasks,
                                   text="Show Tasks",
                                   fg="black", command=self.showTaskButtonClicked)
        self.showTasks.pack(anchor="s", side="right")"""

        self.taskLabel = tk.Label(self.tasks, text="")
        self.taskLabel.pack(fill="x", expand="yes", side="top")

        self.master.master.bind('<Button-1>', self.mouseClicked)

    def taskButtonClicked(self):

        theDay = self.staticText.get()
        self.TaskText.set(self.taskEntry.get())

        if theDay in self.dayTaskDict.keys():
            self.dayTaskDict[theDay].append(self.TaskText.get())

        else:
            self.dayTaskDict[theDay] = []
            self.dayTaskDict[theDay].append(self.TaskText.get())


        self.taskLabel.config(text=("\n".join(self.dayTaskDict[theDay])))

        self.taskEntry.delete(0, 'end')  # delete enrty after submitting it.



    def mouseClicked(self, event):
        print("mouse clicked")
        theDay = self.staticText.get()
        if self.previousDay != self.staticText.get():
            print("gun degisti")
            if theDay in self.dayTaskDict.keys():
                self.taskLabel.config(text=("\n".join(self.dayTaskDict[theDay])))
            else:
                self.taskLabel.config(text="")
        else:
            print("gun degismedi")

        self.previousDay = self.staticText.get()

"""    def showTaskButtonClicked(self):

        theDay = self.staticText.get()

        if theDay in self.dayTaskDict.keys():
            self.taskLabel = tk.Label(self.tasks, text=self.dayTaskDict[theDay])
            self.taskLabel.config(text=("\n".join(self.dayTaskDict[theDay])))"""