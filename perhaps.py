data = { 'a': 
            { 'b': {
                    'c' : 42
                }
            }
        }


def getc(d):
    if d.get('a'):
        d = d['a']
    if d.get('b'):
        d = d['b']
    if d.get('c'):
        return d['c']

def perhaps(d, func):
    if d is not None:
        return func(d)

print(perhaps(perhaps(perhaps(data, lambda x: x.get('a')), lambda x:
    x.get('b')), lambda x: x.get('c')))

class Perhaps:
    def __init__(self, value): self.value = value
    def __repr__(self): return str(self.value)
    def __lshift__(self, other): print(self)
    def __rshift__(self, other):
        if self.value is not None: 
            return Perhaps(other(self.value))
        else:
            return self

Perhaps(data) >> (lambda x: x.get('a')) \
              >> (lambda x: x.get('b')) \
              >> (lambda x: x.get('c')) \
              << None

              continue 1:39:41
