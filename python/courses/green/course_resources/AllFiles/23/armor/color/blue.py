class Blue:

    def __init__(self):
        self.red = 0
        self.green = 0
        self.blue = 255
        self.texture = "smooth"
        self.shininess = 4
        self.specularity = 20.5
        self.material = None

    def lighten(self, amount):
        pass

    def darken(self, amount):
        pass

    def texturize(self, amount, texture_type):
        pass

    def enspecular(self, amount):
        pass

    def despecular(self, amount):
        pass

    def render(self, render_target):
        pass

    def invert(self):
        pass

    def introvert(self):
        pass

    def public_speaking(self):
        pass
