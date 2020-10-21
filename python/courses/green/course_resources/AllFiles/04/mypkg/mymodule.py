def my_function(x):
    return x * 2

class MyClass():

    counter = 0

    def __init__(self):
        self.id = self.counter
        self.counter += 1

    def get_id(self):
        return self.id

