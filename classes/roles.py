class Roles:
    def __init__(self, role_id=None, role_name=None, role_button=None):
        if role_id is not None:
            self.role_id = role_id
            self.role_name = role_name
            self.role_button = role_button
        else:
            pass

    def get_role_id(self):
        return self.role_id

    def get_role_name(self):
        return self.role_name

    def get_role_button(self):
        return self.role_button

    def set_role_id(self, role_id):
        self.role_id = role_id

    def set_role_name(self, role_name):
        self.role_name = role_name

    def set_role_button(self, role_button):
        self.role_button = role_button
