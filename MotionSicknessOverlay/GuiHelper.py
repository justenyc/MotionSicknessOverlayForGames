from tkinter import *
import Constants as c

def create_button(_window, _text, _command):
    new_button = Button(_window, text=_text, command=_command, height=c.BUTTON_HEIGHT, width=c.BUTTON_WIDTH, activebackground=c.BUTTON_PRESS, bg=c.BUTTON_COLOUR, fg=c.FG_COLOUR)
    return new_button

def create_label(_window, _text):
    new_label = Label(_window, text=_text, bg=c.BG_COLOUR, fg=c.FG_COLOUR, bd=2)
    new_label.configure(highlightbackground=c.FG_COLOUR)
    return new_label

def create_slider(_window, _from, _to, _orient, _command):
    new_slider = Scale(_window, from_=_from, to=_to, orient=_orient, bg=c.BUTTON_COLOUR, fg=c.FG_COLOUR, activebackground=c.BUTTON_PRESS)
    new_slider.bind("<ButtonRelease-1>", _command)
    return new_slider