import tkinter as tk


class FrameNotifications:
    def __init__(self, master):
        self.master = master

        self.labelframe = tk.LabelFrame(self.master.master, text="Notifications")
        self.labelframe.pack(fill="both", expand="yes", side="left")
