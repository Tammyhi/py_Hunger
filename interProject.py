import time
import random
import colorama
from colorama import Fore, Back, Style 
class Game:
    def __init__(self, name):
        self.fridge = [" a slice of pepperoni pizza. Drips of oil and strings of cheese flow from your mouth.",
                   " a scoop of ice cream. You taste chocolate, mint, vanilla, strawberry, and an abudance of other flavors.",
                    " a blueberry muffin. The sugar that covered the muffin now sticks onto your face.",
                    " a large chocolate chip cookie. It is just the perfect balance of soft and crunchy.",
                    " a slice of cheesecake. Bits of its sweet crust is stuck in your teeth. Soft icing is stuck on your lips."]
        self.hunger = 5
        print("Welcome to 'HUNGER'.")
        time.sleep(1)
        print("What is your name? ")
        self.name = input()
        
    def slowprint(self, str):
        print(str)
        time.sleep(1.5)
        
    def story(self):
        self.slowprint("You, " + self.name + ", are standing in front of a refrigerator.")
        self.slowprint("There is nothing else around you.")
        self.slowprint("Your stomach growls.")
        self.slowprint("You are hungry.")
        self.slowprint("Open the fridge?")
        if self.prompt("YN") == 0:
            self.endGame("n")
        else:
            self.slowprint("The frige is filled with pepperoni pizza, a large tub of ice cream, a huge party-sized cake, a cabinet full of chocolate chip cookies and another cabinet stuffed with sugar crusted blueberry muffins.")
            self.slowprint("The more you look at the food, the more hungry you get.")
            while(self.hunger != 10  and self.hunger != 0):
                self.slowprint("Eat something?")
                self.prompt("Eat")

    def prompt(self, type):
        state = True
        while(state):
            if type == "YN":
                inp = input("Type y for yes and n for no: ")
                if(inp == "y"):
                    return 1
                    state = False
                elif(inp == "n"):
                    return 0
                    state = False
                else:
                    continue
            if type == 'Eat':
                self.eat(input("Type e to eat and anything else to not eat: "))
                state = False
                

    def eat(self, inp):
        if(inp == "e"):
            self.slowprint("You decided to eat" + self.fridge[random.randrange(0,4)])
            self.hunger += 1
            if(self.hunger == 10):
                self.endGame("b")
        else:
            print("You resisted the urge to eat.")
            self.hunger -= 1
            if(self.hunger == 0):
                self.endGame("g")

    def endGame(self, inp):
        if inp == "g":
            self.slowprint("Suddenly, you don't feel hungry anymore.")
            self.slowprint("It was all an illusion.")
            self.slowprint("You are in control of yourself.")
            self.slowprint("You turn around and walk away from the fridge.")
            print(Fore.GREEN)
            self.slowprint("Good ending!")
            print(Style.RESET_ALL + "")
        elif inp == "n":
            self.slowprint("You don't open the fridge.")
            self.slowprint("There is nothing to do.")
            self.slowprint("After waiting around for a moment, the refrigerator begin to fade.")
            self.slowprint("There is no longer a fridge.")
            print(Fore.BLUE)
            self.slowprint("Neutral ending.")
            print(Style.RESET_ALL + "")
        else:
            self.slowprint("You don't want to eat from the fridge anymore, but you continue to do so anyways.")
            self.slowprint("You lick every last drop of ice cream and every last crumb of dessert.")
            self.slowprint("There is nothing left in the fridge.")
            self.slowprint("A gaping feeling in your chest makes you uncomfortable.")
            self.slowprint("You've eaten so much. Surely you're not hungry anymore?")
            self.slowprint("Yet, you just can't stop thinking about eating.")
            self.slowprint("Your stomach grumbles. It howls for MORE.")
            self.slowprint("You eat your right pinky finger.")
            self.slowprint(self.name + " tastes like chicken meat.")
            self.slowprint("So delicious!")
            for i in range(0,11):
                print(Fore.RED + "MORE!")
                if(i < 6):
                    time.sleep(0.3)
                else:
                    time.sleep(0.1)
            print(Style.RESET_ALL)
            time.sleep(2)
            self.slowprint(self.name + " has been eaten.")
            print(Fore.RED)
            self.slowprint("Bad ending.")
            print(Style.RESET_ALL + "")
            
YO = Game("placeholder")
YO.story()