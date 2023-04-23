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

        # Buttons with various predifined ammount of time
        self.button1 = tk.Button(self.root, text="30 min", command=lambda: shutdown(1800))
        self.button1.pack(pady=10)

        self.button2 = tk.Button(self.root, text="1 hour", command=lambda: shutdown(3600))
        self.button2.pack(pady=10)

        self.button3 = tk.Button(self.root, text="2 hours", command=lambda: shutdown(7200))
        self.button3.pack(pady=10)

        self.button4 = tk.Button(self.root, text="4 hours", command=lambda: shutdown(14400))
        self.button4.pack(pady=10)

        # An input field for the user to specify any ammount of time. Also a custom button
        self.custom_widget = tk.Entry(width=10)
        self.custom_widget.pack()
        self.button5 = tk.Button(self.root, text="Custom", command=lambda: shutdown(self.custom_widget.get()))
        self.button5.pack(pady=10)

        # The cancel button
        self.button6 = tk.Button(self.root, text="Cancel Shutdown", command=cancel_shutdown)
        self.button6.pack(pady=10)

        self.root.mainloop()

screen = Shutdown()
