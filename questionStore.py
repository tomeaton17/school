import random
import string


class Randomized(object):
    def __init__(self):
        self.args = {}

    def __getitem__(self, name):
        return RandomizedFormatter(name, self.args)

    def format(self, s):
        return string.Formatter().vformat(s, args=(), kwargs=self)


class RandomizedFormatter(object):
    def __init__(self, name, args):
        self.name = name
        self.args = args

    def __format__(self, fmt):
        op, rest = fmt.split(':', 1)
        if op == 'random':
            low, high = rest.split(':')
            value = random.randint(int(low), int(high))
            self.args[self.name] = value
            return str(value)


rr = Randomized()
question = rr.format("How much is {a:random:1:5} plus {b:random:109:110}?")
print(question)
print(rr.args['a'])
