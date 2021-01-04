"""
game: dice
source: http://hplgit.github.io/primer.html/doc/pub/random/._random-readable004.html#sec:random:twodicesumguess
"""
import random
import sys


class Dice:
    def __init__(self, n=1):
        self.n = n

    def throw(self):
        return [random.randint(1, 6) for i in range(self.n)]


class Player:
    def __init__(self, name, capital, guess_function, ndice):
        self.name = name
        self.capital = capital
        self.guess_function = guess_function
        self.dice = Dice(ndice)

    def play_one_round(self):
        self.guess = self.guess_function(self.dice.n)
        self.throw = sum(self.dice.throw())
        if self.guess == self.throw:
            self.capital += self.guess
        else:
            self.capital -= 1
        self.message()
        self.broke()

    def message(self):
        print("%s guessed %d, got %d" % (self.name, self.guess, self.throw))

    def broke(self):
        if self.capital == 0:
            print(f"{self.name} lost")
            sys.exit(0)


def computer_guess(ndice):
    return random.randint(ndice, 6 * ndice)


def player_guess(ndice):
    return int(input("Guess the sum of the number od dies in the next roll: "))


def play(nrounds, ndice=2):
    player = Player("YOU", nrounds, player_guess, ndice)
    computer = Player("Computer", nrounds, computer_guess, ndice)

    for i in range(nrounds):
        player.play_one_round()
        computer.play_one_round()
        print(f"Players credit: {player.capital}, Computers credit: {computer.capital}")

    if computer.capital > player.capital:
        winner = "Computer"
    else:
        winner = "You"
    print(f"{winner} wins!")


play(5, 1)
