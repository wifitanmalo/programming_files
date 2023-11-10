def signature_grades():
    global total
    while True:
        total = 0
        try:
            for i in range(0, amount):
                grades = float(input(f"- Enter grade #{i+1}: "))
                percentage = (float(input(f"  + Enter grade #{i+1} percentage: "))/100) * grades
                total += percentage
            break
        except(ValueError, EOFError, KeyboardInterrupt):
            print("----- Only NUMBERS are allowed -----")
    return total


def approach():
    global total
    decimal_1 = int(total*10) % 10
    decimal_2 = int(total*100) % 10
    if decimal_1 in decimals_list[0:9] and decimal_2 in up_decimals:
        total = float(f"{int(total)}.{decimal_1+1}")
    elif decimal_1 == 9 and decimal_2 in up_decimals:
        total = float(f"{int(total+1)}.{decimal_1-decimal_1}")
    elif decimal_1 in decimals_list and decimal_2 in down_decimals:
        total = float(f"{int(total)}.{decimal_1}")
    if(total >= 3.0):
        return f"----- Your GPA is {total}, now you can rest -----"
    else:
        return f"----- Your GPA is {total}, you'll have to repeat -----"


if __name__ == '__main__':
    decimals_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    up_decimals = [5, 6, 7, 8, 9]
    down_decimals = [0, 1, 2, 3, 4]
    while True:
        try:
            amount = int(input("\nEnter amount of grades: "))
            while amount < 0:
                amount = int(input("- Only POSITIVE numbers: "))
            break
        except(ValueError, EOFError, KeyboardInterrupt):
            print("------ Only INT numbers are allowed -----")
    signature_grades()
    print(approach())