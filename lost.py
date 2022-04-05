from sys import exit
import lost_library
import random


class Level(object):

    def prompt(self, text):
        print(text)

    def response(self, correct_answer):
        guess = input("Type your response here >")


        if guess == correct_answer:
            print("You got it")

        else:
            print("Sorry, game over. Try again.")
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
        self.creek.response()

class Creek(object):

    def __init__(self):
        self.level = Level()
        self.pond = Pond()

    def prompt(self):
        self.level.prompt("""
            As soon as you answer, the tree vanishes revealing a creek ahead.
            You make your way to the bank of the creek, when you notice a young
            man sitting at the edge starring thoughtfully into the running water.
            You sit beside the man and look to the water in an attempt to
            understand what the man is doing. The creek has a silvery strong
            reflection on the surface so that you can only see yourself looking
            back.

            The man introduces himself as Siddartha. He asks you what you see,
            and you respond by saying that you can only see yourself. He smiles
            and tells you that you are not looking hard enough. He gently opens
            your palm and places a fidgetting worm inside. Then he tells you to
            keep looking, but to try to look deeper. Once you have found your
            sight, feed the one that calls to you.

            You stare with all your concentration at the running water below.
            Before long, you manage to see beyond your reflection and notice
            that three Koi fish. They are swimming around quite irritably
            waiting for the worm they assume belongs to them.

            There is one white, one orange, and one orange and white colored Koi.
            Which one do you feed?

            white
            orange
            orange and white
            """)


    def response(self):
        list = ["white", "orange", "orange and white"]
        color = random.choice(list)
        print(color)
        self.level.response(color)

    def next(self):
        self.pond.prompt()
        self.pond.response()

class Pond(object):

    def __init__(self):
        self.level = Level()
    def prompt(self):
        self.level.prompt("""
        The Koi fish eats the worm then starts to swim
        slowly upstream. You follow the fish and try to enjoy the scenery, but
        the last traces of light are fading which forces you to focus on where
        you are walking.

        Before long it is so dark that you can no longer see the fish.
        Determined, you continue slowly making your way up stream while walking
        on the river bank until the sound of running water slows to a stop. You
        have arrived at a pond. On the other side you can see the faint glow of
        a fire in a cabin.

        You arrive at the cabin door. What do you do?

        -knock
        -try to find your way back

        """)

    def response(self):
        self.level.response("knock")

    def next(self):
        print("""
        Emerson answers the door, and you can see Thoreau sitting in
        an arm chair by the fire. Emerson invites you in. The three of you sit
        in the arm chairs by the fire drinking beer and discussing life and the
        great journey you just completed.
        """ )

run_tree = Tree()
run_tree.prompt()
run_tree.response()
run_tree.next()
run_creek = Creek()
run_creek.next()
run_pond = Pond()
run_pond.next()
