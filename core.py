from prettytable import PrettyTable
import time
import os
import json
import random

class democrazybrain:
    def __init__(self):
        print(
            '''Welcome to Democrazy!\n
In this game you are the delegate of the Velkar Republic in the United Nations!
Every turn (2 months) you will be given decisions to make, affecting some factors.
If your Reputation or Country Internal Reputation falls below 0, you will be ignored and executed.
If your Reputation goes above 35, you become too aggressive and are executed.
Last till turn 12 (2 years) to win this game.
'''
        )
        self.crep = 9
        self.rep = 9
        self.al = 5
        self.turn = 1

        self.showstats()
        time.sleep(10)
        os.system("cls")
        self.day()

    def day(self):
        os.system("cls")
        print(f"TURN {self.turn}")

        # Random positive/negative events
        ran = random.randint(1, 4)
        if ran == 2:
            self.positive()
        elif ran == 4:
            self.negative()



        time.sleep(5)



        # Random event chance
        if random.randint(1, 2) == 1:
            self.event()


        time.sleep(5)


        self.ammendment()
        self.check()

    def check(self):
        if self.rep > 35 or self.rep <= 0:
            os.system("cls")
            print("You have lost! You will be executed.")
            self.showstats()
        elif self.crep > 35 or self.crep <= 0:
            os.system("cls")
            print("You have lost! You will be executed.")
            self.showstats()
        elif self.al <= 0:
            os.system("cls")
            print("You have lost! You will be executed.")
            self.showstats()
        else:
            self.turn += 1
            if self.turn > 12:
                print("🎉 YOU WIN! The government honors you with USD 100,000 for your brilliant work!")
                self.showstats()
            else:
                self.day()

    def ammendment(self):
        with open("choices.json", "r") as file:
            data = json.load(file)

        index = random.randint(0, len(data)-1)
        event = data[index]["event"]
        des = data[index]["description"]

        print(f"THE TOPIC IS INTRODUCED: {event}\n{des}")

        cresadd = 0
        resadd = 0
        alladd = 0

        # Discussion phase
        choice1 = int(input("DISCUSSION TIME\n1: Give Speech\n2: Lobby Supporters\n3: Do Nothing: "))
        if choice1 == 1:
            print("You gave a powerful speech!")
            resadd += data[index]["discussion"]["give_speech"]["reputation"]
            alladd += data[index]["discussion"]["give_speech"]["alliances"]
            cresadd += data[index]["internal_reputation"]["give_speech"]
        elif choice1 == 2:
            print("You lobbied supporters!")
            resadd += data[index]["discussion"]["lobby"]["reputation"]
            alladd += data[index]["discussion"]["lobby"]["alliances"]
            cresadd += data[index]["internal_reputation"]["lobby"]

        # Voting phase
        choice2 = int(input("TIME TO VOTE\n1: Yes\n2: No\n3: Abstain: "))
        if choice2 == 1:
            print("You voted YES!")
            resadd += data[index]["vote"]["vote_yes"]["reputation"]
            alladd += data[index]["vote"]["vote_yes"]["alliances"]
            cresadd += data[index]["internal_reputation"]["vote_yes"]
        elif choice2 == 2:
            print("You voted NO!")
            resadd += data[index]["vote"]["vote_no"]["reputation"]
            alladd += data[index]["vote"]["vote_no"]["alliances"]
            cresadd += data[index]["internal_reputation"]["vote_no"]
        elif choice2 == 3:
            print("You abstained!")
            resadd += data[index]["vote"]["abstain"]["reputation"]
            alladd += data[index]["vote"]["abstain"]["alliances"]
            cresadd += data[index]["internal_reputation"]["abstain"]

        # Apply stats changes
        self.rep += resadd
        self.al += alladd
        self.crep += cresadd
        self.showstats()

    def showstats(self):
        table = PrettyTable()
        table.field_names = ["Category", "Value"]
        table.add_row(["Reputation", self.rep])
        table.add_row(["Country Internal Reputation", self.crep])
        table.add_row(["Alliance", self.al])
        print(table)

    def positive(self):
        with open("postive.json", "r") as file:
            data = json.load(file)

        event = random.choice(data)
        print(f"POSITIVE EVENT: {event['event']}\n{event['description']}")
        print(f"Changes: Reputation +{event['effect']['reputation']}, Alliance +{event['effect']['alliances']}")
        self.rep += event["effect"]["reputation"]
        self.al += event["effect"]["alliances"]
        self.showstats()
        time.sleep(3)
        os.system("cls")

    def negative(self):
        with open("negative.json", "r") as file:
            data = json.load(file)

        event = random.choice(data)
        print(f"NEGATIVE EVENT: {event['event']}\n{event['description']}")
        print(f"Changes: Reputation {event['effect']['reputation']}, Alliance {event['effect']['alliances']}")
        self.rep += event["effect"]["reputation"]
        self.al += event["effect"]["alliances"]
        self.showstats()
        time.sleep(3)
        os.system("cls")

    def event(self):
        with open("events.json", "r") as file:
            data = json.load(file)

        event = random.choice(data)
        print(f"EVENT: {event['event']}\n{event['description']}")

        choices = list(event["choices"].keys())
        for i, c in enumerate(choices):
            print(f"{i}: {c}")

        choice = int(input("Choose an action (0-2): "))
        selected = event["choices"][choices[choice]]
        self.rep += selected["reputation"]
        self.al += selected["alliances"]
        self.showstats()
        time.sleep(3)
        os.system("cls")