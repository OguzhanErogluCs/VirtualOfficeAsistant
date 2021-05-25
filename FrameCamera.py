import tkinter as tk

class FrameCamera:
    def __init__(self, master):
        self.master = master

        self.labelframe = tk.LabelFrame(self.master.master, text="Camera")
        self.labelframe.pack(fill="both", expand="yes", side="right")
"""        self.tasks = tk.LabelFrame(self.labelframe, text="Tasks")
        self.tasks.pack(fill="both", expand="yes", side="right")"""