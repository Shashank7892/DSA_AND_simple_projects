import random

while True:
    print("\n choose 1 for rock \n choose 2 for paper \n choose 3 for sciessor")
    user_input=int(input("enter the choice"))
    if user_input < 1 or user_input > 3:
        print("Invalid Input!!!! computer wins")
    else:
        computer_choice=random.randint(1,3)
        print(computer_choice)
        if computer_choice == user_input:
            print(f" your input is {user_input} and computer choice is {computer_choice}... So Its a Draw")
        elif computer_choice == 1 and user_input == 3:
            print(f" your input is {user_input} and computer choice is {computer_choice}... So Its a computer wins")
        elif computer_choice == 3 and user_input == 1:
            print(f" your input is {user_input} and computer choice is {computer_choice}... So Its a user wins")
        elif user_input > computer_choice:
            print(f" your input is {user_input} and computer choice is {computer_choice}... So Its a user wins")
        elif computer_choice > user_input:
            print(f" your input is {user_input} and computer choice is {computer_choice}... So Its a computer wins")
    
