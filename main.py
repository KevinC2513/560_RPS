
import random  

def g_u_ch():
    u_c = input("Choose (r, p, or s): ").lower()
    return u_c

def g_c_ch():
    return random.choice(["r", "p", "s"])

def det_win(u_c, c_c):
    if u_c == c_c:
        return "U tied!"
    elif (u_c == "r" and c_c == "s") or \
         (u_c == "p" and c_c == "r") or \
         (u_c == "s" and c_c == "p"):
        return "U win!"
    else:
        return "U lose!"

def play_game():
    print("Let's play r, p, s!")

    while True:
        u_c = g_u_ch()  
        c_c = g_c_ch()  

        print(f"U chose {u_c}.")
        print(f"C chose {c_c}.")

        result = det_win(u_c, c_c)  
        print(result)

        play_again = input("Play again? (y/n): ").lower()  
        if play_again != 'y':
            print("Thanks. Bye!")
            break

if __name__ == "__main__":
    play_game()
