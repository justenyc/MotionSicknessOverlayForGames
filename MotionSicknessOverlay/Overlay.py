#https://www.youtube.com/watch?v=75jbNpc8vN4&t=168s&ab_channel=Codemy.com

from tkinter import *
import threading
import time
import logging
import InputManager
import FileHelper as fh
import Constants as c
import GuiHelper as gh

class App(Frame):
    savedSettings = {}
    screenData = {}

    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.master = master
        savedProperties = fh.get_saved_data()
        App.savedSettings["radius"] = float(savedProperties["radius"])
        App.savedSettings["offsetx"] = float(savedProperties["offsetx"])
        App.savedSettings["offsety"] = float(savedProperties["offsety"])
        App.savedSettings["sensitivity"] = float(savedProperties["sensitivity"])
        App.savedSettings["fade_speed"] = float(savedProperties["fade_speed"])
        App.savedSettings["control_type"] = savedProperties["control_type"]

    def init_root(self, root):
        root.state('zoomed')
        root.attributes('-fullscreen', True)
        root.attributes('-topmost', 1)
        root.config(bg="#add123")
        root.wm_attributes('-transparentcolor','#add123')
        App.screenData["screen_width"] = root.winfo_screenwidth()
        App.screenData["screen_height"] = root.winfo_screenheight()
        App.screenData["screen_center"] = (App.screenData["screen_width"]/2, App.screenData["screen_height"]/2)
        App.screenData["alpha"] = 1

    def draw_circle(self, x, y, radius, draw_canvas):
        draw_canvas.create_oval(
            x - radius,
            y - radius,
            x + radius,
            y + radius,
            width = 3,
            fill="#add123"
        )
    
    def init_canvas(self, root):
        rootCanvas = Canvas(root, bg="black")
        rootCanvas.pack(fill=BOTH, expand=True)
        return rootCanvas

    def apply_app_alpha(self, newAlpha, overlay_window):
        if newAlpha < overlay_window.attributes('-alpha'):
            if App.savedSettings["control_type"] == "Mouse & Keyboard":
                time.sleep(1/60)
            newAlpha = overlay_window.attributes('-alpha') - 1/60
        overlay_window.attributes('-alpha', newAlpha)

def begin():
    try:
        foundGamepad = InputManager.get_gamepad()
    except:
        notification = Tk()
        notification.configure(background=c.BG_COLOUR)
        label = gh.create_label(notification, "Control Type is set to Gamepad, but no gamepad was found")
        label.pack()
        button_close = gh.create_button(notification, "Whoops", quit)
        button_close.pack()
        return

    root = Tk()
    app = App(root)
    app.init_root(root)
    mainCanvas = app.init_canvas(root)

    app.draw_circle(
        App.screenData["screen_center"][0] + App.savedSettings["offsetx"], 
        App.screenData["screen_center"][1] - App.savedSettings["offsety"], 
        App.savedSettings["radius"], 
        mainCanvas)

    InputManager.attach_listeners()
    control_type = app.savedSettings["control_type"]

    while True:
        #time.sleep(1/60)
        if control_type == "Mouse & Keyboard":
            InputManager.update_mouse_position()
            app.apply_app_alpha(InputManager.mouseMagnitude, root)            
        else:
            InputManager.gamepad_input()
            #print(InputManager.gamepadMagnitude)
            app.apply_app_alpha(InputManager.gamepadMagnitude, root)
        root.update_idletasks()
        root.update()
        #mainCanvas.delete("all")
    root.mainloop()