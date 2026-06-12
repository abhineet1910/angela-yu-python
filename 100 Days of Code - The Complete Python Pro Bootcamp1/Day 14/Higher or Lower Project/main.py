import random


import art
print(art.logo)

from game_data import data

score = 0
def compare_guess(guess,a_followers,b_followers):
    if guess== "a":
        a_followers>b_followers
        return True
    elif guess=="b":
        b_followers>a_followers
        return True
    else:
        return False


def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"
account_b = random.choice(data)
game_should_continue = True
while game_should_continue:
    account_a = account_b
    account_b = random.choice((data))
    if account_a == account_b:
        account_b = random.choice(data)
    print(f"compare a: {format_data(account_a)} ")
    print(art.vs)
    print(f"compare b: {format_data(account_b)}")
    guess = input("who has more followers? : type 'a' : for A type 'b' for B").lower()
    print("\n"*20)
    a_follower_cunt= account_a["follower_count"]
    b_follower_cunt= account_b["follower_count"]




    is_correct= compare_guess(guess,a_follower_cunt,b_follower_cunt)
    if is_correct:
        score+=1
        print(f"Correct answer , your score is: {score}")
    else:
        print(f"Incorrect answer your final score is :{score}")
        game_should_continue = False







