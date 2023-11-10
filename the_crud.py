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
    global name, users_list, number
    while True:
        name = input("- Enter the name to create: ").capitalize()
        if name.isalpha():
            break
        else:
            print("  ----- The name only can contain WORDS -----")
    if name in users_list:
        print(f"----- '{name}' was created again -----")
    else:
        print(f"----- '{name}' was created successfully -----")
    number += 1
    users_list |= {f"Name {number}":name}


def read():
    search = input("- Enter the name to search: ").capitalize()   
    for position in range(1, number+1):
        if search not in users_list.values():
            return "----- Sorry, the name isn't in our database -----"
        elif search == users_list[f"Name {position}"]:
            return "  + Hi, {}!".format(users_list[f"Name {position}"])


# ----- List of names -----""")
#         for name_number, nigger in enumerate(users_list, 1):
#             print(f"- Name {name_number}: {nigger}")


def update():
    update = input("- Enter the name to update: ").capitalize()
    if update in users_list:
        while True:
            new = input("  + Enter the new name: ").capitalize()
            if new.isalpha():
                break
            else:
                print("  ----- The name only can contain WORDS -----")
        position = users_list.index(update)
        users_list[position] = new
        print(f"----- '{update}' was updated to '{new}' successfully -----")
    else:
        print("----- Sorry, the name isn't in our database -----")


def delete():
    delete = input("- Enter the name to delete: ").capitalize()
    if delete in users_list:
        users_list.remove(delete)
        print(f"----- '{delete}' was deleted successfully -----")
    else:
        print("----- Sorry, the name isn't in our database -----")


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
                update()
            elif choice == "D" and len(users_list) > 0:
                delete()
            elif choice == "E":
                print(exit())
                break
            else:
                print("- No user has registered yet")
        except(EOFError, KeyboardInterrupt):
            print("\n----- Error, rebooting system -----")