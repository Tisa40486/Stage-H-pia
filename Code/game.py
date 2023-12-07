from random import randint
def game (guess, lb, lh):
    # to_guess=int(input())
    to_guess=guess
    limit_basse=lb
    limit_haute=lh
    find= False 
    # num= randint(0,100)
    num= int(limit_haute/2)
    while not find:
        # print(f"guess: {num}, answer: {to_guess}")
        # print(f"lb: {limit_basse}, lh: {limit_haute}")

        if num>to_guess:
            limit_haute = num
            num= round(limit_haute-(limit_haute-limit_basse)/2)
        elif num < to_guess: 
           limit_basse= num
           num= round(limit_basse+(limit_haute-limit_basse)/2)
        else: 
           find= True 
    # print(f"gagné {num}")

def test_game():
    lb = 0
    lh = int(10e3)

    for i in range(lh):
        print(f"Testing number {i+1}")
        game(i+1, lb, lh)

    print("Tests passed")


test_game()