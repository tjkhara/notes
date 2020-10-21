class Widget:

    def __init__(self, used=False):
        self.used = used
        self.state = "unsprocketed"
        self.mass = 5

    def sprocket(self):
        self.mass += 10
        if self.mass > 50:
            self.state = "sproinged"
        else:
            self.state = "sprocketed"

    def drop(self):
        if self.used:
            self.state = "splutted"
        else:
            self.state = "splatted"
