class Roles:
    def __init__(self, role_id=None):
        if not role_id:
            self.role_id = role_id

    def get_role_id(self):
        return self.role_id

    def get_role_name(self):
        return self.role_name

    def get_role_color_code(self):
        return self.role_color_code

    def set_role_id(self, role_id):
        self.role_id = role_id

    def set_role_name(self, role_name):
        self.role_name = role_name

    def set_role_color_code(self, role_color_code):
        self.role_color_code = role_color_code

