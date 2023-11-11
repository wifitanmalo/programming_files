import shutil

def choice_selection():
    global choice
    while True:
        choice = input("\nEnter the option desired: ").capitalize()
        if choice in choices_list:
            break
        else:
            print("----- Only can enter C, R, U, D or E -----")
    return choice


def create():
    global users_list, number
    while True:
        name = input("- Enter the name to create: ").capitalize()
        if name.isalpha():
            break
        else:
            print("  ----- The name only can contain WORDS -----")
    if name in users_list:
        print(f"----- '{name}' was created again -----")
    else:
        print(f"----- '{name}' was created -----")
    number += 1
    users_list |= {number:name}


def read():
    search = input("- Enter the name to search: ").capitalize()   
    if search not in users_list.values():
        return(f"----- '{search}' isn't in our database -----")
    else:
        for name_number in range(1, number+1):
            if users_list[name_number] == search:
                return(f"  + Hi, {search}! {users_list}")


# ----- List of names -----""")
#         for name_number, nigger in enumerate(users_list, 1):
#             print(f"- Name {name_number}: {nigger}")


def update():
    update = input("- Enter the name to update: ").capitalize()
    if update in users_list.values():
        while True:
            new = input("  + Enter the new name: ").capitalize()
            if new.isalpha():
                break
            else:
                print("  ----- The name only can contain WORDS -----")
        for name_number in range(1, number+1):
            if users_list[name_number] == update:
                users_list[name_number] = new
                break
        return(f"----- '{update}' was updated to '{new}' -----")
    else:
        return(f"----- '{update}' isn't in our database -----")


def delete():
    global number
    delete = input("- Enter the name to delete: ").capitalize()
    if delete in users_list.values():
        for name_number in range(1, number+1):
            if users_list[name_number] == delete:
                number -= 1
                users_list.pop(name_number)
        return(f"----- '{delete}' was deleted -----")
    else:
        return(f"----- '{delete}' isn't in our database -----")


def exit():
    farewell = "See you space, cowboy..."
    terminal_width, _ = shutil.get_terminal_size()
    x = terminal_width - len(farewell)
    print(" " * x, end="")
    return farewell


if __name__ == '__main__':
    number = 0
    users_list = {}
    choices_list = ["C", "R", "U", "D", "E"]
    print("""
Welcome! What would you to like today?
- "C" to create a user
- "R" to read a user
- "U" to update a user
- "D" to delete a user
- "E" to exit""")
    while True:
        try:
            choice_selection()
            if choice == "C":
                create()
            elif choice == "R" and len(users_list) > 0:
                print(read())
            elif choice == "U" and len(users_list) > 0:
                print(update())
            elif choice == "D" and len(users_list) > 0:
                print(delete())
            elif choice == "E":
                print(exit())
                break
            else:
                print("- No user has registered yet")
        except(EOFError, KeyboardInterrupt):
            print("\n----- Error, rebooting system -----")