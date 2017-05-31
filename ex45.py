#Exercise 45: You Make a Game

from sys import exit
from random import randint

class Scene(object):

    drawer_located = False
    key_found = False
    baseball_bat_found = False
    gun_found = False
    code = ""

    def enter(self):
        print("Not yet configured.")
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

class Lose(Scene):

    def enter(self):
        print("GAME OVER.")
        exit(1)

class Bedroom(Scene):

    print("""
        07:30am. You're in your bedroom and notice that your cat's not there.
        You heard rumours that an old guy across the street hates cats like
        noone else.
        """)

    def enter(self):

        print("What do you do?")

        action = input("> ")

        if action == "look around":
            print("There is a door to the hallway in front of you and drawer to your left")
            Scene.drawer_located = True
            return 'bedroom'

        elif action == "open drawer" and Scene.drawer_located:
            print("You found a key to your basement.")
            Scene.key_found = True
            return 'bedroom'

        elif action == "leave":
            return 'hallway'

        else:
            print("What's that? Maybe you should look around the room...")
            return 'bedroom'

class Hallway(Scene):

    def enter(self):
        print("""
            The door to your bedrooms shuts behind you
            and you now stand in your hallway.
            The front door is straight ahead of you,
            a door to your basement to your right.
            """)

        action = input("> ")

        if action == "front door":
            return 'street'

        elif action == "basement" and Scene.key_found:
            return 'basement'

        elif action == "basement" and not Scene.key_found:
            print("The basement is locked.")
            return 'hallway'

        elif action == "bedroom":
            return 'bedroom'

        else:
            print("That can't be right.")
            return 'hallway'

class Basement(Scene):

    def enter(self):
        print("""
            The basement is quite dark. You can see quite a lot of spiderwebs and
            dust near the dimly lit light bulb. You didn't take much care of this
            basement the last couple of years... There's only an old baseball bat
            in the corner and an old rug beneath the bulb.
            """)
        print("What do you do?")

        action = input("> ")

        if action == "take baseball bat":
            print("PLACEHOLDER baseball bat taken")
            Scene.baseball_bat_found = True
            return 'basement'

        elif action == "look under the rug":
            print("PLACEHOLDER secret door")
            Scene.gun_found = True
            return 'basement'

        elif action == "leave" or action == "leave basement":
            return 'hallway'

        else:
            print("PLACEHOLDER error")
            return 'basement'

class Street(Scene):

    def enter(self):
        print("PLACEHOLDER ruin on the right, house of the left")

        action = input("> ")

        if action == "go to house on the left" or action == "go to the left house":
            return 'house_on_the_left'

        else:
            print("PLACEHOLDER maybe try the left one")
            return 'street'

class House_On_The_Left(Scene):

    rock_paper_scissor = ["Rock", "Paper", "Scissor"]

    def enter(self):
        print("PLACEHOLDER old creep, rps")

        enemy_turn = House_On_The_Left.rock_paper_scissor[randint(0, len(self.rock_paper_scissor) - 1)]
        #debugging
        print(enemy_turn)
        action = input("Rock, Paper or Scissor? ")

        if action == "Rock":
            if enemy_turn == "Rock":
                print("DRAW")
                return 'House_On_The_Left'
            elif enemy_turn == "Scissor":
                print("You win!")
                return 'the_attack'
            else:
                print("You lose!")
                return 'lose'
        elif action == "Paper":
            if enemy_turn == "Rock":
                print("You win!")
                return 'the_attack'
            elif enemy_turn == "Paper":
                print("DRAW")
                return 'house_on_the_left'
            else:
                print("You lose!")
                return 'lose'
        elif action == "Scissor":
            if enemy_turn == "Rock":
                print("You lose!")
                return 'lose'
            elif enemy_turn == "Paper":
                print("You win")
                return 'the_attack'
            else:
                print("DRAW")
                return 'house_on_the_left'
        else:
            return 'lose'

class The_Attack(Scene):

    def enter(self):
        print("PLACEHOLDER old creep attacks you")

        if Scene.gun_found or Scene.baseball_bat_found:
            print("PLACEHOLDER you strike him down")
            print("he drops a little piece of paper and you pick it up. it reads")

            if Scene.gun_found:
                print("The sound of your gun firing alarmed your kitten and it runs towards you.")
                return 'finished'

            else:
                Scene.code = "{r1}{r2}{r3}".format(r1 = randint(1,9), r2 = randint(1,9), r3 = randint(1,9))
                #debugging
                print(Scene.code)
                code_list = list(Scene.code)
                print("Looks like a shopping list...")
                print("""
                    {r1} Eggs
                    {r2} Loafs of bread
                    {r3} Apples
                    """.format(r1 = code_list[0], r2 = code_list[1], r3 = code_list[2]))
                print("You hear a faint meow in a shed nearby and you run towards the sound.")
                return 'shed'

        else:
            print("PLACEHOLDER kills you")
            return 'lose'

class Shed(Scene):

    def enter(self):
        print("PLACEHOLDER shed keypad")

        action = input("KEYPAD: ")
        guesses = 0

        while action != Scene.code and guesses <= 3:
            print("CODE NOT VALID!")
            guesses += 1

        if action == Scene.code:
            print("DING!")
            print("The door opens and your cat jumps into your arms")
            return 'finished'
        else:
            print("TOO MANY ATTEMPTS")
            return 'lose'

class Finished(Scene):

    def enter(self):
        print ("Congratulations! You won!")
        return 'finished'

class Map(object):

    scenes = {
        'bedroom': Bedroom(),
        'hallway': Hallway(),
        'basement': Basement(),
        'street': Street(),
        'house_on_the_left': House_On_The_Left(),
        'the_attack': The_Attack(),
        'shed': Shed(),
        'lose': Lose(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('bedroom')
a_game = Engine(a_map)
a_game.play()
