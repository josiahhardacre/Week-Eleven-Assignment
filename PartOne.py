# Josiah Hardacre
# Week Eleven
# 11/18/15

from BowlingGame import Game

testscores = open("testscores.txt","r")
         
for line in testscores:
    line = line.strip() 
    scoreList = line.split(",") #Puts into list with commas
    scoreList = [int(i) for i in scoreList] #Strings turns into integers
    finalScore = scoreList.pop() #finalScore is last number in the line
    g = Game() #From BowlingGame.py
    for roll in scoreList: #Puts frames into BowlingGame
        g.roll(roll)
    score = g.score() #Retrieves score from BowlingGame
    print("Calculated score is {}, and the given score is {}".format(score,  finalScore))
    if score == finalScore: #Compares to see if they are correct
        print("The score was correct!")
    else:
        print("Score was incorrect. The score should be", score)
        
# Close file
testscores.close()