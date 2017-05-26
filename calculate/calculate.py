class Calculate(object):
    def add(self, x, y):
        """Takes two integers and adds them together to produce the result"""

        if type(x) == int and type(y) == int:
            return x + y
        else:
            raise TypeError("Invalid type: {} and {}".format(type(x), type(y)))
