"""
Integrantes:
- Nicolas Chaparro (2380530)
- Santiago Alexander Criollo (2380661)
- Juan José López (2380647)
- Joan Esteban Villamil (2380466)
"""


import random


# # ----- Exercise 1: wear 'em front. wear 'em back -----


# def first_ones():
#     global first_numbers
#     first_numbers = 0
#     for i in range(0, 3):
#         first_numbers += int(number[i])


# def last_ones():
#     global second_numbers
#     second_numbers = 0
#     for i in range(3, 5):
#         second_numbers += int(number[i])


# if __name__ == '__main__':
#     number = str(random.randint(10000, 99999))
#     print(f"\nThe random number is {number}")
#     first_ones()
#     last_ones()
#     if first_numbers == second_numbers:
#         print(f"""
# - Wow! The sum of {number[0:3]} ({first_numbers})
# is the same as {number[3:5]} ({second_numbers})
# """)
#     else:
#         print(f"""
# - Oh... the sum of {number[0:3]} ({first_numbers})
# isn't the same as {number[3:5]} ({second_numbers})
# """)


# # ----- Exercise 2: Nequi -----


def cards_information():
    global total_money, a, loc, amount
    while True:
        try:
            amount = int(input("\nEnter amount of cards: "))
            break
        except ValueError:
            print("----- Only can enter int numbers -----")
    for i in range(1, amount+1):  
        card_number = random.randint(1000000, 9999999)
        pass_number = random.randint(1000, 9999)
        total_money = random.randint(0, 2000000)
        card_data = {f"card_{i}":card_number,
                    f"pin_{i}":pass_number,
                    f"money_{i}":total_money}
        loc |= card_data
    print(f"- Cards information: {loc}")


def input_card():
    global card, a
    while True:
        try:
            card = int(input("\nEntry your card number: "))
            while card not in loc.values():
                card = int(input("- Not found, try again: "))
            break
        except ValueError:
            print("----- Only can enter int numbers -----")
    
        
def input_pin():
    global a
    for a in range(1, amount+1):
        while card == loc[f"card_{a}"]:
            try:
                pin = int(input("\nEntry your card PIN: "))
                while pin != loc[f"pin_{a}"]:
                    pin = int(input("- Incorrect PIN, try again: "))
                break
            except ValueError:
                print("----- Only can enter int numbers -----")
    print(f"\n----- You have: $", loc[f"money_{a}"], "-----")


def withdraw_money():
    if loc[f"money_{a}"] > 10000:
        while True:
            try:
                money = int(input("\nEntry money to withdraw: "))
                while money%10000 != 0 or money > loc[f"money_{a}"]:
                    money = int(input("- Invalid amount, try again: "))
                print(f"""
You have successfully withdrawn: $ {money}
- Now you have left: $""", loc[f"money_{a}"]-money)
                break
            except ValueError:
                print("----- Only can enter int numbers -----")
    else:
        print("- Not enough balance to make a withdraw")


if __name__ == '__main__':
    loc = {}
    cards_information()
    input_card()
    input_pin()
    withdraw_money()