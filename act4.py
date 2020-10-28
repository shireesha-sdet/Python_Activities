user1 = input ("Enter user 1 name ")
user2 = input ("Enter user 2 name ")

playGame = "yes"

while playGame == "yes":

    option1 = input (user1 + " : Choose one of these 3 options : rock, paper, scissors...  ").lower()
    option2 = input (user2 +" : Choose one of these 3 options : rock, paper, scissors...  ").lower()

    if option1 == option2:
        print ("It is a tie")
    elif option1 == "paper":
        if option2 == "scissors":
            print (user2 + " wins")
        elif option2 == "rock":
            print (user1 + " wins")
        else:
            print("Invalid " + user2 + " input! You have not entered rock, paper or scissors, try again.")
    elif option1 == "scissors":
        if option2 == "paper":
            print (user1 + " wins")
        elif option2 == "rock":
            print (user2 + " wins")
        else:
            print("Invalid " + user2 + " input! You have not entered rock, paper or scissors, try again.")
    elif option1 == "rock":
        if option2 == "paper":
            print (user1 + " wins")
        elif option2 == "scissors":
            print (user2 + " wins")
        else:
            print("Invalid " + user2 + " input! You have not entered rock, paper or scissors, try again.")
    else:
        print("Invalid " + user1 + " input! You have not entered rock, paper or scissors, try again.")

    playGame = input("Do you want to play again? Yes / No : ").lower()

else:
    print ("End of Game")