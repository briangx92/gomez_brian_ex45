# I'm going to try to simulate this to how in the movie Black Mirror: Bandersnatch is portrayed. It's similar in the aspect of making choices but you get to navigate around
from sys import exit

class Scene(object):

    def enter(self):
        print("empty")
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        pass
# The class Death will be where you get some nice comments when you fail
class Death(object):
    death_type = [


    ]

class Room(Scene):

    def enter(self):
        pass


class Therapist(Scene):

    def enter(self):
        pass

class Work(Scene):

    def enter(self):
        pass

class ColinsHouse(Scene):

    def enter(self):
        pass

class SecretRoom(Scene):

    def enter(self):
        pass


# The class World is where everything is going to take place. it'll be where everything gets pointed to.
class World(object):

    scenes = {

    }
