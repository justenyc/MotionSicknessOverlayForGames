class AppProperties:
    @property
    def radius(self):
        return self.app_radius

    @radius.setter
    def radius(self, newRadius):
        self.app_radius = newRadius

    @property
    def offsetx(self):
        return self.app_offsetx

    @offsetx.setter
    def offsetx(self, newOffsety):
        self.app_offsetx = newOffsety
    
    @property
    def offsety(self):
        return self.app_offsety

    @offsety.setter
    def offsety(self, newOffsety):
        self.app_offsety = newOffsety

    @property
    def screen_width(self):
        return self.app_screen_width

    @screen_width.setter
    def screen_width(self, newWidth):
        self.app_screen_width = newWidth

    @property
    def screen_height(self):
        return self.app_screen_height

    @screen_height.setter
    def screen_height(self, newHeight):
        self.app_screen_height = newHeight
        
    @property
    def screen_center(self):
        return self.app_screen_center

    @screen_center.setter
    def screen_center(self, newCenter):
        self.app_screen_center = newCenter

    @property
    def alpha(self):
        return self.app_alpha

    @alpha.setter
    def alpha(self, newAlpha):
        self.app_alpha = newAlpha

    @property
    def sensitivity(self):
        return self.app_sensitivity

    @sensitivity.setter
    def sensitivity(self, newSensitivity):
        self.app_sensitivity = newSensitivity

    @property
    def fade_speed(self):
        return self.app_fade_speed

    @fade_speed.setter
    def fade_speed(self, newFadeSpeed):
        self.app_fade_speed = newFadeSpeed