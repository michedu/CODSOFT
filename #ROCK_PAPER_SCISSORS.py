import random
q = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
game_sec = ["rock","paper","scissors"]
print(game_sec[q])
print("Computer chooses:")
t = random.randint(0,2)
print(game_sec[t])


if q>=3 and q<0:
  print("Please choose a proper number mentioned above")
elif q==0 and t==2:
  print("You win")
elif q==2 and t==0:
  print("You lose")
elif q<t:
  print("You lose")
elif q>t:
  print("You win")
elif q==t:
  print("Draw")

else:
  print("Invalid")