import random
import string
import questionplotclass

#Randomized class, that is used to format strings, and return question objects.
#This is the parent of the RandomizeddFormatter class.
class Randomized(object):
    def __init__(self):
        self.args = {}
        self.question = None

    #Returns the value of the randomized variable in the string.
    def __getitem__(self, name):
        return RandomizedFormatter(name, self.args)

    #Formats the string, using the overridden method found in the RandomizedFormatter class.
    def format(self, s):
        return string.Formatter().vformat(s, args=(), kwargs=self)

    #Returns the question class depending on the equation type.
    def get_class(self):
        if self.args['equation'] == "findtheta":
            self.question = questionplotclass.ProjectileQuestion(self.args['b'], self.args['a'], random.randint(40, 60))
            self.question.find_theta()
            return self.question
        if self.args['equation'] == "findmaxheight":
            self.question = questionplotclass.ProjectileQuestion(self.args['c'], self.args['a'], self.args['b'])
            self.question.find_max_height()
            return self.question
        if self.args['equation'] == 'findxdistance':
            self.question = questionplotclass.ProjectileQuestion(self.args['c'], self.args['a'], self.args['b'])
            self.question.find_xdistance()
            return self.question

#RandomizedFormatter class. Child of Randomized class. Overrides String formatter to allow
#question formatting.
class RandomizedFormatter(object):
    def __init__(self, name, args):
        self.name = name
        self.args = args

    #This function overrides the Python string formatter.
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

#This code only runs if the file is run specifically, not when it is imported.
if __name__ == '__main__':
    rr = Randomized()
    load("projectilemotionquestions", rr)
    print(rr.get_class())