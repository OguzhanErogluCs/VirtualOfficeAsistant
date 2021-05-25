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
                                    text=" + Add",
                                    fg="black", command=self.taskButtonClicked)
        self.taskButton.pack(anchor="s",side="left")

        self.deleteTask = tk.Button(self.tasks,
                                   text=" - Delete",
                                   fg="black", command=self.deleteSelectedItem)
        self.deleteTask.pack(anchor="s",side="right")


        self.listBox = tk.Listbox(self.tasks)
        self.listBox.pack(pady=15,fill="both",padx = 10)
        self.master.master.bind('<Button-1>', self.mouseClicked)

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
        #print("mouse clicked")
        theDay = self.staticText.get()

        if self.previousDay != self.staticText.get():
            print("gun degisti")
            if theDay in self.dayTaskDict.keys():
                self.insertListElements()
            else:
                self.listBox.delete(0,'end')
        else:
            print("gun degismedi")

        self.previousDay = self.staticText.get()


    def insertListElements(self):

        theDay = self.staticText.get()
        self.listBox.delete(0, 'end')
        for i in self.dayTaskDict[theDay]:
            self.listBox.insert(tk.END, i)

    def deleteSelectedItem(self):

        theDay = self.staticText.get()
        if(self.listBox.curselection()):
            self.dayTaskDict[theDay].remove(self.dayTaskDict[theDay][self.listBox.curselection()[0]]) # delete selected items from dict
            self.listBox.delete(tk.ANCHOR) # delete selected items from listbox
