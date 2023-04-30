class Button:
    def __init__(self, button_mode=None, button_color=None):
        if button_mode is not None:
            self.mode = button_mode
            self.color = button_color
        else:
            pass

    def get_mode(self):
        return self.mode

    def get_color(self):
        return self.color

    def set_mode(self, button_mode):
        self.mode = button_mode

    def set_color(self, button_color):
        self.color = button_color