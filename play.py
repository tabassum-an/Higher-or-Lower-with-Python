import random
from game_data import data
import art

def profile(account):
    name = account["name"]
    description = account["description"]
    country = account['country']

    return f" {name}, a {description} from {country}."

def correct_answer(guess, profile_a, profile_b):
    if profile_a > profile_b:
        return guess == "A"
    else:
        return guess == "B"


print(art.logo)
score = 0
compare_B = random.choice(data)

while True:
    compare_A = compare_B
    compare_B = random.choice(data)
    if compare_A == compare_B:
        compare_B = random.choice(data)

    print(f"Compare A:{profile(compare_A)}")
    print(art.vs)
    print(f"Against B:{profile(compare_B)}")
    gamer_guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    print("\n" * 20)
    print(art.logo)

    follower_count_a = compare_A['follower_count']
    follower_count_b = compare_B['follower_count']

    correct_guess = correct_answer(gamer_guess, follower_count_a, follower_count_b)
    if correct_guess:
        score += 1
        print(f"You're right! Current score: {score}")

    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        break
