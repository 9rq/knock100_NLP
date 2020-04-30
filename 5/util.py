class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        return '{0.surface} {0.base} {0.pos} {0.pos1}'.format(self)

    __repr__ = __str__

class Chunk:
    def __init__(self, dst, srcs):
        self.morphs = []
        self.dst = dst
        self.srcs = srcs
