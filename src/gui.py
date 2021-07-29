from tkinter import Button, Entry, Frame, Label, Toplevel
from tkinter.constants import END
from sentiment import compare_sentiment

class LabeledEntry(Entry):
    def __init__(self, master=None, label="Search", **kwargs):
        Entry.__init__(self, master, **kwargs)
        self.label = label
        self.on_exit()
        self.bind('<FocusIn>', self.on_entry)
        self.bind('<FocusOut>', self.on_exit)

    def on_entry(self, event=None):
        if self.get() == self.label:
            self.delete(0, END)

    def on_exit(self, event=None):
        if not self.get():
            self.insert(0, self.label)
            
class PopupWindow(object):
    """
    A simple popup window including an 'Ok' button that shuts it down
    """
    
    def __init__(self,master, msg=''):
        top=self.top=Toplevel(master)
        center_window(top, 300,50)
        self.l=Label(top,text=msg)
        self.l.pack()
        self.b=Button(top,text='Ok',command=self.cleanup)
        self.b.pack()
    def cleanup(self):
        self.top.destroy()

class Window(object):
    """
    Main window, including a text label, two input fields,
    and a 'Run' button
    """

    def __init__(self, master):
        self.master = master
        frame = Frame(master)
        frame.pack()
        self.label = Label(frame, text='Welcome!')
        self.label.pack()
       
        self.first_field = LabeledEntry(frame, width=35, borderwidth=5, label='Type a word here...')
        self.first_field.pack()
        self.second_field = LabeledEntry(frame, width=35, borderwidth=5, label="Type another here...")
        self.second_field.pack()

        self.button = Button(frame, text='Run', command=self.button_click)
        self.button.pack()
    

    def button_click(self):
        """Handles button click event, calls compare_sentiment from sentiment.py"""
        first_thing = self.first_field.get()
        second_thing = self.second_field.get()
        frame = Frame()
        res = compare_sentiment(first_thing, second_thing)
        PopupWindow(frame, msg=f'The world prefers {res}! :)')

def center_window(root, width=300, height=200):
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        root.geometry('%dx%d+%d+%d' % (width, height, x, y))

    