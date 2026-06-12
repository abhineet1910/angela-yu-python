import art
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# user_cards_A = random.choice(cards)
# user_cards_B = random.choice(cards)
# user_cards_C = random.choice(cards)
# usercards= [user_cards_A, user_cards_B]
#
# computer_cards_A = random.choice(cards)
# computer_cards_B = random.choice(cards)
# total_sumcomp = computer_cards_A + computer_cards_B
# computercards = [computer_cards_A, computer_cards_B]
def deal_card():
    "this function provides a random card from the user,computer"
    card= random.choice(cards)
    return card
def calculate_score(cards):
    "this function takes a list of cards and calculates the score"
#     totalsum = sum(user_card)
#     return totalsum
# def check_ace (listname):
    if sum(cards)==21 and len(cards)==1:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(u_score, c_score):
    """Compares the user score u_score against the computer score c_score."""
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def play_game():
    print(art.logo)
    user_card=[]
    computer_card=[]
    user_score=-1
    computer_score=-1
    is_game_over=False
    for i in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())



    while not is_game_over:
        user_score=calculate_score(user_card)
        computer_score=calculate_score(computer_card)


        print(f"here are the cards of user: {user_card} and user score: {user_score}")
        print(f"computer card: {computer_card[0]}")
        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over=True
        else:
            withdraw=input("Would you like to draw anathor card? (y/n): ")
            if withdraw=="y":
                user_card.append(deal_card())
            else:
                is_game_over=True
    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)
    print(f"here are the final cards of user: {user_card} and final  user score: {user_score}")
    print(f"here are the fianl cards of computer: {computer_card},and final score is {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()


# wannaplay = input("Do you want to play the game of BLACKJACK? type yes:'y' and no :'n' ")
# # if wannaplay == 'y':
# #     print("Welcome to the game of BLACKJACK!")
# #     print(art.logo)

    # total_sum = sum(usercards)
    # print(f"here are the cards of user [{usercards}]")
    # print(f"here is the total sum of the cards : {total_sum}")
    # print(f"heres the computrer first card : {computer_cards_A}")
    # if total_sum == 21:
    #     print("you win there is a blackjack ace + 10 ")
    # elif total_sumcomp == 21:
    #     print("you lose computer has a blackjack ace + 10 ")
    # elif total_sum>21:
    #     check_ace(usercards)
    #     check_ace(computercards)
    # else:
    #     another_card=input("do you want another card? type yes:'y' and no :'n' ")
    #     if another_card == 'y':
    #         usercards.append(user_cards_C)
    #         total_sum = sum(usercards)
    #         print(f"here are the cards of user [{usercards}]")
    #         print(f"here is the total sum of the cards : {total_sum}")









