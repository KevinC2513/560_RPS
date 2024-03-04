import random  

def get_user_choice():
    #turns the inputs r, p, s into lower case if inputting as upper
    user_choice = input("Choose (r, p, or s): ").lower()
    return user_choice

def get_comp_choice():
    #changed some code here to maintain consistency. 
    #added comp_choice to mirror user_choice
    comp_choice = random.choice(["r", "p", "s"])
    return comp_choice

def who_wins(user_choice, comp_choice):
    #defines parameters for what should go into func
    if user_choice == comp_choice:
        return "U tied!"
    #if user choice represented by u_c  == comp -> tie.
    
    elif (user_choice == "r" and comp_choice == "s") or \
         (user_choice == "p" and comp_choice == "r") or \
         (user_choice == "s" and comp_choice == "p"):
             
        return "U win!"
    else:
        return "U lose!"

def play_game():
#change the sentence here for full sentence.
    print("Let's play Rock, Paper, Scissors!")

    while True:
        #set the arguments of who_wins to these two funcs
        user_choice = get_user_choice()  
        comp_choice = get_comp_choice()  

        print(f"U chose {user_choice}.")
        print(f"C chose {comp_choice}.")

        result = who_wins(user_choice, comp_choice) 
        print(result)

#Added a bit of code to account for users inputting anything other than y or n
#also added some text for clarity. 

        play_again = "y"
        while play_again == "y" or play_again == "reset":
            play_again = input("Play again? (y/n): ").lower()
            
            if play_again == "y":
                print("Another Round Begins!")
                break
            if play_again == 'n':
                print("Thanks. Bye!")
                break
            else:
                print("Not a valid answer.")
                play_again = "reset"
                

if __name__ == "__main__":
    play_game()
