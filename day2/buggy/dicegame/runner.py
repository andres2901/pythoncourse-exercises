from .die import Die

class GameRunner:

    def __init__(self):
        self.dice = Die.create_dice(5)
        self.reset()

    def reset(self):
        self.round = 1
        self.wins = 0
        self.loses = 0

    def answer(self):
        total = 0
        for die in self.dice:
            total += die.dice_value()
        return total
   
    def roll(self):
        self.dice = Die.create_dice(5)

    @classmethod
    def run(cls):
        runner = cls()
        while True:
            print("\nRound {}\n".format(runner.round))

            for die in runner.dice:
                print(die.show())
            
            while True:
                guess = input("What is your guess?: ")
                try:
                    guess = int(guess)
                    break
                except ValueError:
                    print(f"Value '{guess}' is not accepted. Please put an integer")
            
            if guess == runner.answer():
                print("Congrats, you can add like a 5 year old...")
                runner.wins += 1
            else:
                print("Sorry that's wrong")
                print("The answer is: {}".format(runner.answer()))
                print("Like seriously, how could you mess that up")
                runner.loses += 1
            print("Wins: {} Loses {}".format(runner.wins, runner.loses))
            runner.round += 1

            if runner.round > 6:
                print()
                print("The game has ended. This was the 6th round")
                print(f"You're statst are: Wins = {runner.wins} Loses = {runner.loses}")
                exit(0)

            while True:
                prompt = input("Would you like to play again?[Y/n]: ")

                if prompt == 'y' or prompt == 'Y':
                    runner.roll()
                    break
                elif prompt == 'n' or prompt == 'N':
                    print("Thanks for playing")
                    print(f"You're statst are: Wins = {runner.wins} Loses = {runner.loses}")
                    exit(0)
                else:
                    print("unaccepted value for the question. Accepted value are: 'Y','y','N','n'")
