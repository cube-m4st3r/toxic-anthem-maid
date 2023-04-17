from database import database as db

class Menu_Embed:
    def __init__(self, menu_embed_id, message_id, embed_title=None, embed_description=None, embed_roles=None):
        self.id = menu_embed_id
        self.message_id = message_id
        self.title = embed_title
        self.description = embed_description
        # load roles
        if embed_roles is None:
            self.roles = db.load_embed_menu_roles(menu_embed_id)
        else:
            self.roles = embed_roles

    def get_id(self):
        return self.id

    def get_message_id(self):
        return self.message_id

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_roles(self):
        return self.roles

    def set_id(self, menu_embed_id):
        self.id = menu_embed_id

    def set_message_id(self, message_id):
        self.message_id = message_id

    def set_title(self, title):
        self.title = title

    def set_description(self, description):
        self.description = description

    def set_roles(self, roles):
        self.description = roles