import random
Rock=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

Paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

Scissors=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
user_choice=[Rock, Paper, Scissors]
x=int(input("0 for Rock, 1 for Paper, 2 for Scissor "))
print(user_choice[x])
computer_choice= random.randint(0,2)
y=user_choice[computer_choice]
print(f"'Computer Chose :{y}")
if user_choice==0 and computer_choice==1:
    print("You lose sed :(")
elif x==1 and computer_choice==0:
    print("You Win yayyy xD")
elif x==1 and computer_choice==2:
    print("You lose noob")
elif x==2 and computer_choice==1:
    print("you win les goo")
elif x==2 and computer_choice==0:
    print("you lose man !!")
elif x==0 and computer_choice==2:
    print("You win dude!!")
elif x==computer_choice:
    print("draw T_T")
else:
    print("invalid input")
    
