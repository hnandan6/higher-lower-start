from art import logo
from art import vs
from game_data import data
import random

game_play = True
count = 0
while game_play:
  print(logo)
  x = random.choice(data)
  print("Compare A:",x["name"],",",x["description"],",",x["country"])
  print(vs)
  y = random.choice(data)
  print("Compare B:",y["name"],",",y["description"],",",y["country"])

  answer = input("who has more follower? Type A or B:").lower()
  
  if (answer == 'a') and (x["follower_count"] > y["follower_count"]):
    count += 1
  else:
    print("You lost and the points you received is:", count)
    game_play = False
