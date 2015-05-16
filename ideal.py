class NrComplex(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __add__(self, sn):
        return NrComplex(self.a + sn.a, self.b + sn.b)
    def __repr__(self):
        return "%s + i * %s" % (self.a, self.b)


