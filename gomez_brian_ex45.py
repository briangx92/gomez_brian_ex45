# I'm going to try to simulate this to how in the movie Black Mirror: Bandersnatch is portrayed. It's similar in the aspect of making choices.
from sys import exit ; from random import randint ; from textwrap import dedent

choice = input("> ")

class Scene(object):

    def enter(self):
        print("empty")
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
    self.scene_map = scene_map

def play(self):
    current_scene = self.scene_map.opening_scene()
    last_scene = self.scene_map.next_scene('finished')

    while current_scene != last_scene:
        next_scene_name = current_scene.enter()
        current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()
# The class Death will be where you get some nice comments when you fail
class Death(object):
    death_type = [
        "You don't have a choice with death.",
        "Better luck next time",
        "You should throw your computer away because of how bad you are",
        "Why bother playing?"
        ]

    def enter(self):
        print(Death.death_type[randint(0, len(self.death_type)-1)])
        exit(1)

class Room(Scene):

    def enter(self):
        print(dedent("""
        You wake up gasping for air and its the same dream, every night.
        It's time to start the day ."""))
        print(dedent("""
        The morning routine: Brush teeth, take your meds, and shower... """))
        print(dedent("""
        1. I'm gonna skip taking my meds they're making me feel strange. 
        2. Skip morning routine entirely. 
        3. Go back to bed.
        """))

        if choice == '1':
            print(dedent("""
            The therapist told you to take your meds or you won't be able to function properly.
            1. Should I call her?
            2. Continue about your day?
            """))
            if choice == '1':
                return 'therapist'
            else:
                return 'work'
        elif choice == '2':
            print(dedent("""
            You're not late for anything but you look ragged. But it'll be another day at work in your little cubicle

            """))
            return 'work'
        else choice == '3':
            return 'death'

        
    


class Limbo(Scene):

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
    'death': Death(),
    'limbo': Limbo(),
    'therapist': Therapist(),



    }
