""" @Author(s): Andrea Failla
    @VersionID: 1.0
    @LastUpdated: 28 lug 2021, 02:15:50
"""
from tkinter import Tk
from gui import Window, center_window

def main():
    root = Tk()
    root.title('What Does The World Prefer?')
    root.resizable(False, False)
    center_window(root, 500, 150)
    app = Window(root)
    root.mainloop()

if __name__ == '__main__':
    main()