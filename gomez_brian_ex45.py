# I'm going to try to simulate this to how in the movie Black Mirror: Bandersnatch is portrayed. It's similar in the aspect of making choices and its my own little spin up of it.
from sys import exit ; from random import randint ; from textwrap import dedent
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

        choice = input("> ")

        if choice == '1':
            print(dedent("""
            The therapist told you to take your meds or you won't be able to function properly.
            1. Should I call her?
            2. Continue about your day?
            """))
            choice1 = input("> ")

            if choice1 == '1':
                print(dedent("""
                Hey, I need to see you immediately. I'm heading over right now so you better clear your appointments
                """))
                return 'therapist'
            else:
                return 'work'
                
        elif choice == '2':
            print(dedent("""
            You're not late for anything but you look ragged. But it'll be another day at work in your little cubicle

            """))
            return 'work'
        else:
            return 'limbo'

        
    


class Limbo(Scene):

    def enter(self):
        print(dedent("""
        Mom!! I can't find my toy. I'm not going anywhere without it...
        """))

        print(dedent("""
        We're going to miss the 1500 train and have to get on the 1530 , leave it behind...
        1. We'll take the next train until I find it. I don't care if we're late
        2. I'll stay home
        """))
        choice = input("> ")

        if choice == '1':
            print(dedent("""
             TV NEWS REPORTER: 
                The 1530 train crashed and everyone died. the only train that made it was the 1500. Can you imagine,
                If you got on a little earlier you would've survived.
                A moment of silence for those lost in this tragic accident.

             """))
            return 'death'
        else:
            print(dedent("""
            TV NEWS REPORTER:
                The 1530 train survived a horrific accident. The passengers made it out alive
            """))
            return 'work'

        


class Therapist(Scene):

    def enter(self):
        print(dedent("""
        Is there anything you'd like to talk about today?
        1. No
        2. I feel like I'm not making these choices.
        3. Yes.
        """))
        choice = input("> ")

        if choice == '1':
            print(dedent("""
            Back home we go...
            """))
            return 'room'
        elif choice == '2':
            print(dedent("""
            Why do you feel like you can't make choices? Is it delusional or do you feel like physically you can't?
            1. I don't know.
            2. It feels like when I make a decision, something else takes over and does it for me.
            """))
            choice1 = input("> ")
            
            if choice1 == '1':
                print(dedent("""
                I'm going to give you some meds to help with your mental health.
                """))
            else:
                return 'work'
        else:
            print(dedent("""
            Your eyes start glazing over and you go to an unconscious state
            """))
            return 'limbo'
            
# The class Map is where everything is going to take place. it'll be where everything gets pointed to.
class Map(object):

    scenes = {
    'death': Death(),
    'limbo': Limbo(),
    'therapist': Therapist(),
    'room': Room(),

    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val
    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('room')
a_game = Engine(a_map)
a_game.play()

