import tkinter as tk
import os


def shutdown(time):
    """Method that will shutdown the computer after a desired ammount of time"""
    return os.system(f"shutdown -s -t {time}")


def cancel_shutdown():
    """Stops the active shutdown log"""
    return os.system("shutdown -a")


class Shutdown:

    def __init__(self):

        self.root =tk.Tk()
        self.root.geometry("300x300")
        self.root.title("Shutdown App")

        self.root.mainloop()

screen = Shutdown()
