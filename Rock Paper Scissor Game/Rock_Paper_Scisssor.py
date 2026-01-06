import random
print ("Welcome to the Rock, Paper, Scissor game!")
moves = ["Rock", "Paper", "Scissor"]
user_move = input("Enter your move: (Rock/Paper/Scissor) ")
comp_move = random.choice(moves)
print (f"Your move: {user_move}, Computer's move: {comp_move}")

if user_move == comp_move:
    print ("Both have chosen the same move, it's a tie!")

if user_move == "Rock" and comp_move == "Scissor":
    print ("You have smashed the computer's Scissor and won!")
if user_move == "Rock" and comp_move == "Paper":
    print ("The computer blocks your Rock with it's Paper and you lose!")
if user_move == "Paper" and comp_move == "Rock":
    print ("You block the computer's Rock with your Paper and win!")
if user_move == "Paper" and comp_move == "Scissor":
    print ("Your Paper is shredded to bits and pieces by the computer's Scissor and you lose!")
if user_move == "Scissor" and comp_move == "Rock":
    print ("Your Scissor gets smashed by the computer's Rock and you lose!")
else:
    print ("Your Scissor rips through the computer's Paper and you win!")