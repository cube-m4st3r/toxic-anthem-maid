import roles
class Guild:
    def __init__(self, guildId, roles):
        self.guildId = guildId
        self.roles = roles()
