class Laser(object):

    def __init__(self, sound="Pew!"):
        self.sound = sound
        print("Assembling {}".format(self.__class__.__name__))

    def fire(self):
        return self.sound


class TurboLaser(Laser):

    def __init__(self):
        super(TurboLaser, self).__init__("KAPEW!")


class Xwing(object):
    """
    Xwings have four lasers, so they fire four shots at a time.
    """

    def __init__(self):
        print("Assembling Xwing")
        self.weapons = [Laser(), Laser(), Laser(), Laser()]

    def fire(self):
        print("\n".join(w.fire() for w in self.weapons))


class Frigate(object):

    def __init__(self):
        print("Assembling Frigate")
        self.weapons = [TurboLaser(), TurboLaser()]
        self.ships = [Xwing()]

    def launch(self):
        for ship in self.ships:
            ship.launch()
