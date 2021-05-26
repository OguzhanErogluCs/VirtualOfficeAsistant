import tkinter as tk
from tkinter import StringVar
from tkcalendar import Calendar


from FrameCalendar import FrameCalendar
from FrameCamera import FrameCamera
from FrameNotifications import FrameNotifications


class MainWindow:

    def __init__(self, master):
        self.master = master

        master.title("Virtual Assistant")
        master.geometry("750x650")
        master.grid_rowconfigure(0, weight=1)
        master.grid_columnconfigure(0, weight=1)
        master.resizable(True, True)


if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)

    calendarframe = FrameCalendar(app)
    notificationsframe = FrameNotifications(app)
    cameraframe = FrameCamera(app)
    root.mainloop()
