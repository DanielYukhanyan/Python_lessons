import random
man=0
computer=0
ch=["rock","paper","scissors"]
print("""rock-->scissors
paper-->rock
scissors-->paper""")
player=input("do you want to be rock,paper,scissors or exit")
while player!="exit":
  player=player.lower()
  comp=random.choice(ch)
  print("you choice "+player+" and computer choice "+comp)
  if player=="exit":
    break
  elif player==comp:
    print("draw")
  elif player=="rock":
    if comp=="scissors":
      print("!YOU WIN!")
      man=man+1
    else:
      print("computer win")
      computer=computer+1
  elif player=="paper":
    if comp=="rock":
      print("!YOU WIN!")
      man=man+1
    else:
      print("computer win")
      computer=computer+1
  elif player=="scissors":
    if comp=="paper":
      print("!YOU WIN!")
      man=man+1
    else:
      print("computer win")
      computer=computer+1
  else:
    print("bad input")
  print("")
  player=input("do you want to be rock,paper,scissors or exit")
print("computer wins are "+str(computer))
print("man wins are "+str(man))