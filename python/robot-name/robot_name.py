import secrets


class Robot(object):
    def __init__(self):
        self.create_name()

    def create_name(self):
        self.name = chr(secrets.randbelow(26) + 65)
        self.name += chr(secrets.randbelow(26) + 65)
        for i in range(3):
            self.name += str(secrets.randbelow(10))

    def reset(self):
        self.create_name()

