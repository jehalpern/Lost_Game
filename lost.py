from sys import exit


class Level(object):

    def prompt(self, text):
        print(text)

    def response(self, correct_answer):
        guess = input("Type your response here >")


        if guess == correct_answer:
            print("You got it")

        else:
            print("Wrong")
            exit(0)

    def next(self):
        pass

class Engine(object):

    def __init__ (self, scene):
        pass

    def play(self):
        pass

class Tree(object):

    def __init__(self):
        self.level = Level()
        self.creek = Creek()

    def prompt(self):
        self.level.prompt("""
        You are walking through a forest. The air is heavy
        with mist, and everything around you is cast in a
        deep blue as the last hour before nightfall settles in.
        You become ambigously aware of a tree just out of your
        field of view, yet it demands your attention as if
        its own sense of vanity compels you to draw near.
        It is a large presumptious live oak tree gnarling its
        arms through the hazey space it occupies.

        As you approach the trunk, Nietzsche steps around the tree
        to greet you. With a smile that is as joyful as it is menacing,
        he introduces himself. He asks you to describe the tree in front you.

        How do you respond?
        The tree is dying
        The tree is fighting against the dark
        There is no tree

        """)


    def response(self):
        self.level.response("There is no tree")


    def next(self):
        self.creek.prompt()

class Creek(object):

    def __init__(self):
        self.level = Level()

    def prompt(self):
        self.level.prompt("This is the creek")

    def Correct_answer(self):
        pass

    def next(self):
        pass

class Pond(object):

    def prompt(self):
        pass

    def Correct_answer(self):
        pass

    def next(self):
        pass

run_tree = Tree()
run_tree.prompt()
run_tree.response()
run_tree.next()
