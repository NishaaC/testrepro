import random
class Game:
    def __init__(self):
        #users_pick , computes_pick , result -> win lose draw
         self.computer_pick = self.get_computer_pick()

         self.user_pick = self.get_user_pick()

         self.result = self.get_result()

    def get_computer_pick(self):
        #random no pick garna 
        random_number = random.randint(1,3)
        options = {1: 'rock', 2: 'paper', 3: 'scissors'}
        return options[random_number]

    def get_user_pick(self):
        while True:
            options = {1: 'rock', 2: 'paper', 3: 'scissors'}
            user_pick = int(input("Enter 1 for rock, 2 for paper, or 3 for scissors: "))

            if user_pick in options:
                break
            else:
                print('Wrong input! Please enter 1, 2, or 3.')

        return options[user_pick]

    def get_result(self):
        #if draw
        if self.computer_pick == self.user_pick:
            return 'draw'

        # for user to win 
        elif self.user_pick =='paper' and self.computer_pick =='rock':
            return 'win'
        elif self.user_pick=='rock' and self.computer_pick=='scissors':
            return 'win'
        elif self.user_pick=='scissors'and self.computer_pick=='paper':
            return 'win'

        #if users loses 
        # if users loses 
        else:
            return 'lose'

    

    def print_result(self):
        print(f"computer's pick: {self.computer_pick}")
        print(f"users pick: {self.user_pick}")
        print(f"You {self.result}")

while True:
    #an object of game class
    game = Game()
    game.print_result()

    play_again = input("Do you want to play again (y/n): ").lower()
   # if user chooses y then 
    if play_again != 'y':
        break 