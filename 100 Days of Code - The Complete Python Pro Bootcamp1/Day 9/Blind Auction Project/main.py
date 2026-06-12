# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import art
print(art.logo)
empty_dict={}
def find_highest_bidder(bids):
    max_bid = 0
    max_bidder = ""
    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount > max_bid:
            max_bid= bid_amount
            max_bidder = bidder
    print(f"The winner is {max_bidder} with a bid of ${max_bid}")


setcontinue = True
while  setcontinue:
    name = input("Enter your name: ")
    bit_price = int(input("Enter your bit price: "))
    if name in empty_dict:
        empty_dict[name] += bit_price
    elif name not in empty_dict:
        empty_dict[name] = bit_price
    should_continue = input("Do you want to continue (yes/no): ")
    if should_continue == "no":
        setcontinue = False
        find_highest_bidder(empty_dict)
    elif should_continue == "yes":
        print("\n" * 50)




