import p60
import math


def cos(x, y):
    def mag(v):
        return math.sqrt(sum([e**2 for e in v]))
    dot = sum([x[i]*y[i] for i in range(len(x))])
    return dot / (mag(x)*mag(y))



model = p60.read_vectors()

united_states = model['United_States']
us = model['U.S.']
print(model.similarity('United_States', 'U.S.'))
print(cos(united_states, us))
