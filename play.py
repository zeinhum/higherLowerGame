from game_data import data
import random

print("** let's play higher-lower game, you choose who has more followers")



score = 0


def play_game():
    global score
    while True:
        player_a, player_b = random.sample(data, 2)

        print(f"Option A: {player_a['name']}, {player_a['description']} from {player_a['country']}")
        print(f"Option B: {player_b['name']}, {player_b['description']} from {player_b['country']}")
        print("Option S : to exit the game")

        option = input("** choose your option: ").lower().strip()
        if option == 'a':
            if player_a['follower_count'] > player_b['follower_count']:
                score += player_a['follower_count']
                print(f"nice ! your score is {score}")
            else:
                print(f"oops! wrong gase, you score is {score}")
                break

        if option == 'b':
            if player_b['follower_count'] > player_a['follower_count']:
                score += player_a['follower_count']
                print(f"nice ! your score is {score}")
            else:
                print(f"oops! wrong gase, you score is {score}")
                break
        if option == 's':
            break
        else:
            print("it's not the the correct option, please try again")

play_game()
