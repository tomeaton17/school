import random
import string
import questionplotclass


class Randomized(object):
    def __init__(self):
        self.args = {}
        self.question = None

    def __getitem__(self, name):
        return RandomizedFormatter(name, self.args)

    def format(self, s):
        return string.Formatter().vformat(s, args=(), kwargs=self)

    def get_class(self):
        if(self.args['equation'] ==  "findtheta"):
            self.question = questionplotclass.ProjectileQuestion(self.args['b'], self.args['a'], random.randint(40, 60))
            self.question.find_theta()
            return self.question
        if (self.args['equation'] == "findmaxheight"):
            self.question = questionplotclass.ProjectileQuestion(self.args['c'], self.args['a'], self.args['b'])
            self.question.find_max_height()
            return self.question
        if (self.args['equation'] == 'findxdistance'):
            self.question = questionplotclass.ProjectileQuestion(self.args['c'], self.args['a'], self.args['b'])
            self.question.find_xdistance()
            return self.question




class RandomizedFormatter(object):
    def __init__(self, name, args):
        self.name = name
        self.args = args

    def __format__(self, fmt):
        op, rest = fmt.split(':', 1)

        if op == 'type':
            self.args[self.name] = rest
            return ""
        elif op == 'random':
            low, high = rest.split(':')
            value = random.randint(int(low), int(high))
            self.args[self.name] = value
            return str(value)

def load(questionType, object):
    lines = [line.rstrip('\n') for line in open(questionType + ".txt")]
    return object.format(random.choice(lines))

if __name__ == '__main__':
    rr = Randomized()
    load("projectilemotionquestions", rr)
    print(rr.get_class())