from tkinter import *
from tkinter import ttk
import Overlay
import GuiHelper as gh
import Constants as c
import FileHelper as fh

class SettingsWindow:
    settingsToSave = fh.get_saved_data()

    def save_settings(self):
        try:
            save_string = fh.get_json_string(SettingsWindow.settingsToSave)
            fh.write_to_file(save_string)
            notification = Tk()
            notification.configure(background=c.BG_COLOUR)
            label = gh.create_label(notification, "Successful Save was successful")
            label.pack()
            button_close = gh.create_button(notification, "Cool", notification.destroy)
            button_close.pack()
        except:
            notification = Tk()
            notification.configure(background=c.BG_COLOUR)
            label = gh.create_label(notification, "Save Failed")
            label.pack()
            button_close = gh.create_button(notification, "Lame", notification.destroy)
            button_close.pack()
            return

    def update_radius(self, event):
        SettingsWindow.settingsToSave["radius"] = self.slider_radius.get()
        print(SettingsWindow.settingsToSave)

    def update_offset_x(self, event):
        SettingsWindow.settingsToSave["offsetx"] = self.slider_offsetx.get()
        print(SettingsWindow.settingsToSave)

    def update_offset_y(self, event):
        SettingsWindow.settingsToSave["offsety"] = self.slider_offsety.get()
        print(SettingsWindow.settingsToSave)

    def update_sensitivity(self, event):
        SettingsWindow.settingsToSave["sensitivity"] = self.slider_sensitivity.get()
        print(SettingsWindow.settingsToSave)

    def update_fade_speed(self, event):
        SettingsWindow.settingsToSave["fade_speed"] = self.slider_fade_speed.get()
        print(SettingsWindow.settingsToSave)

    def update_control_type(self, event):
        SettingsWindow.settingsToSave["control_type"] = self.combobox_controlType.get()
        print(SettingsWindow.settingsToSave)

    def check_save_data(self):
        data = fh.get_saved_data()
        return data

    def __init__(self):
        window_settings = Tk()
        window_settings.title("Settings")
        window_settings.configure(background=c.BG_COLOUR)

        for ii in range(10):
            gh.create_label(window_settings, " ").grid(row=0, column=ii)
            gh.create_label(window_settings, " ").grid(row=ii, column=0)

        data = self.check_save_data()

        label_title = gh.create_label(window_settings, "Settings").grid(row=1, column=5, columnspan=2)

        label_controlType = gh.create_label(window_settings, "Control Type").grid(row=2, column=5)
        self.combobox_controlType = ttk.Combobox(window_settings, state='readonly', width=11)
        self.combobox_controlType['values'] = ("Mouse & Keyboard", "Gamepad")
        self.combobox_controlType.current(1)
        self.combobox_controlType.bind('<<ComboboxSelected>>', self.update_control_type)
        self.combobox_controlType.grid(row=2, column=6, pady=4)
        self.combobox_controlType.set(data["control_type"])
        
        label_radius_slider = gh.create_label(window_settings, "Radius").grid(row=3, column=5)
        self.slider_radius = gh.create_slider(window_settings, 100, window_settings.winfo_screenwidth()/2, HORIZONTAL, self.update_radius)
        self.slider_radius.grid(row=3, column=6, pady=4)
        self.slider_radius.set(data["radius"])

        label_offsetx_slider = gh.create_label(window_settings, "Offset X").grid(row=4, column=5)
        self.slider_offsetx = gh.create_slider(window_settings, -window_settings.winfo_screenwidth()/2, window_settings.winfo_screenwidth()/2, HORIZONTAL, self.update_offset_x)
        self.slider_offsetx.grid(row=4, column=6, pady=4)
        self.slider_offsetx.set(data["offsetx"])

        label_offsety_slider = gh.create_label(window_settings, "Offset Y").grid(row=5, column=5)
        self.slider_offsety = gh.create_slider(window_settings, window_settings.winfo_screenheight()/-2, window_settings.winfo_screenheight()/2, HORIZONTAL, self.update_offset_y)
        self.slider_offsety.grid(row=5, column=6, pady=4)
        self.slider_offsety.set(data["offsety"])

        label_sensitivity_slider = gh.create_label(window_settings, "Sensitivity").grid(row=6, column=5)
        self.slider_sensitivity = gh.create_slider(window_settings, 1, 10, HORIZONTAL, self.update_sensitivity)
        self.slider_sensitivity.grid(row=6, column=6, pady=4)
        self.slider_sensitivity.set(data["sensitivity"])

        label_fade_speed_slider = gh.create_label(window_settings, "Fade Speed").grid(row=7, column=5)
        self.slider_fade_speed = gh.create_slider(window_settings, 0, 10, HORIZONTAL, self.update_fade_speed)
        self.slider_fade_speed.grid(row=7, column=6, pady=4)
        self.slider_fade_speed.set(data["fade_speed"])

        button_save = gh.create_button(window_settings, "Save", self.save_settings).grid(row=8, column=5, padx=4, pady=4)
        button_cancel = gh.create_button(window_settings, "Close", window_settings.destroy).grid(row=8, column=6, padx=4, pady=4)

        window_settings.mainloop()

#c = SettingsWindow()