import random

computer_choice = random.randint(1, 100)
user_choice_history = []

while 4>2:
    user_choice = int(input("loftn adday dar bazeye 1 ta 100 hads bezanid: "))
    user_choice_history.append(user_choice)
    print(f"entekhab compter: {computer_choice} \nentekhab karbar: {user_choice}")
    if user_choice == computer_choice:
        print("ahsant, belakhare dorost gofty")
        break

print(user_choice_history)