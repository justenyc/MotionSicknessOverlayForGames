from tkinter import *
import GuiHelper as gh
import Constants as c
import SettingsGUI as settings
import Overlay

class WelcomeGUI:
    def start_app(self):
        self.window_welcome.destroy()
        Overlay.begin()

    def open_settings(self):
        settingWindow = settings.SettingsWindow()

    def __init__(self):
        self.window_welcome = Tk()
        self.window_welcome.title("Motion Sickness Helper")
        self.window_welcome.configure(background=c.BG_COLOUR)

        for ii in range(9):
            gh.create_label(self.window_welcome, " ").grid(row=0, column=ii)
            gh.create_label(self.window_welcome, " ").grid(row=ii, column=0)

        label_title = gh.create_label(self.window_welcome, "Justen's Motion Sickness Overlay Helper").grid(row=1, column=4)
        label_description = gh.create_label(self.window_welcome, "Hello!\n\n If you get motion sickness while playing games with a third person camera like my wife does then I hope that this can help you out! \n We are still in beta testing so please let me know if you encounter any problems.").grid(row=3, column=4)
        label_instructions = gh.create_label(self.window_welcome, "Please set your game to *borderless windowed* to ensure that this application displays on top of it.\n\n This application is set to react to Gamepad by default. \n\nPlease go to \"Settings\" if you want to switch to Mouse & Keyboard").grid(row=5, column=4)

        button_start = gh.create_button(self.window_welcome, "Start", self.start_app).grid(row=7, column=4, pady=4)
        button_settings = gh.create_button(self.window_welcome, "Settings", self.open_settings).grid(row=8, column=4, pady=4)
        button_Cancel = gh.create_button(self.window_welcome, "Cancel", quit).grid(row=9, column=4, pady=4)

        self.window_welcome.mainloop()

w = WelcomeGUI()