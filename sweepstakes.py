from contestant import Contestant
import random
class Sweepstakes:
    def __init__(self,name):
        self.sweepstakes_name = name
        self.contestant = {}

    def register_contestant(self,contestant):
        self.contestant[contestant.registration_number] = contestant

    def pick_winner(self):
        winner = random.choice(self.contestant)
        return winner


    def print_contestant_info(self,contestant):
        print('l')

