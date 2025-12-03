game1 = input("player 1, enter rock, paper, or scissors")
game2 = input("player 2, enter rock, paper, or scissors")

if(game1 == game2):
   print("Tie")


elif(game1 == "rock"):
 if(game2 == "scissors"):
	print("player1 wins")
else:
	print("player2 wins")

elif(game1 == "paper"):
 if(game2 == "rock"):
	print("Player1 wins")
else:
	print("Player2 wins")

elif(game1 == "scissors"):
 if(game2 == "paper"):
	print("Player1 wins")
else:
	print("Player2 wins")

else:
	print("Invalid input")
