import tkinter as tk

class FrameCamera:
    def __init__(self, master):
        self.master = master

        self.labelFrame = tk.LabelFrame(self.master.master, text="  Camera  ",font = "Helvetica 11 bold", bd= 3, labelanchor = "n")
        self.labelFrame.pack(fill="both", expand="yes", side="right", padx=5, pady=5)
