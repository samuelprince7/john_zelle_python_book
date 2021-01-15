# rball.py
# this program simulates a specific number of games of racquetball
# based on the probability factor of player A winning and
# the probability factor of player B winning
# the number of games is entered by the user as 'n'

# the primary concern of designing this program is to
#  do Top-Down-Design, or working on 'one function at at time'
# making sure 'that function' works, b4 distributing it into the program

from random import random

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)

def printIntro():
    print("This program simulates a game of racquetball between two")
    print('players called "a" and "B".  The ability of each player is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("the player will win a particular point when serving.  Player A always")
    print("has the first serve, when a new game begins")
    print(" *the 1st player to reach 15 points wins that game")

def getInputs():
    # returns the three simulation parameters
    a = float(input("What is the prob. player A wins a serve? "))
    b = float(input("What is the prob. player B wins a serve? "))
    n = int(input("How many games to simulate?"))
    return a, b, n

def simNGames(n, probA, probB):
    # Simulates n games of racquetball between players whose
    # abilities are represented by the probability of winning a serve.
    # Returns final scores for A and B 

    winsA = winsB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA = winsA + 1
        else: 
            winsB = winsB + 1
    return winsA, winsB 


def simOneGame(probA, probB):
    # imulates a single game or racquetball between players whose
    #  abilities are represented by the probability of winning a serve.
    # Returns final scores for A and B 
    serving = "A"
    scoreA = 0
    scoreB = 0
    while not gameOver(scoreA, scoreB):

        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else: 
                serving = "B"
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else: 
                serving = "A"

    return scoreA, scoreB

def gameOver(a, b):
    # a and b represent scores for a racquetball game 
    # Returns True if the game is over, False otherwise.
    return a==15 or b==15

def printSummary(winsA, winsB):
    # Prints a summary of wins for each player.
    n = winsA + winsB
    print("\nGames simulated:", n)
    print("Wins for A: {0} ({1:0.1%})".format(winsA, winsA/n))
    print("Wins for B: {0} ({1:0.1%})".format(winsB, winsB/n))

if __name__ == '__main__' : main() 
    
                



        
