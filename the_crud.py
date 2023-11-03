def choice_selection():
    global choice
    choice = input("\nEnter the option desired: ").capitalize()
    while True:
        if choice in choices_list:
            break
        else:
            choice = input("""
----- Only can enter 'C', 'R', 'U', 'D' or 'E' -----
- Try again: """).capitalize()


def create():
    global name
    while True:
        name = input("- Enter the name to create: ").capitalize()
        if name.isalpha():
            break
        else:
            print("----- The name only can contain words -----\n")
    if name in users_list:
        print(f"\n----- '{name}' was created again -----")
    else:
        print(f"\n----- '{name}' was created successfully -----")
    users_list.append(name)


def read():
    search = input("- Enter the name to search: ").capitalize()
    if search in users_list:
        position = users_list.index(search)
        print(f"""
- Hi, {users_list[position]}!

----- List of names -----
""")
        for number, nigger in enumerate(users_list, 1):
            print(f"- Name {number}: {nigger}")
    else:
        print("\n----- Sorry, the name isn't in our database -----")


def update():
    update = input("- Enter the name to update: ").capitalize()
    if update in users_list:
        while True:
            new = input("  + Enter the new name: ").capitalize()
            if new.isalpha():
                break
            else:
                print("----- The name only can contain words -----\n")
        position = users_list.index(update)
        users_list[position] = new
        print(f"\n----- '{update}' was updated to '{new}' successfully -----")
    else:
        print("\n----- Sorry, the name isn't in our database -----")


def delete():
    delete = input("- Enter the name to delete: ").capitalize()
    if delete in users_list:
        users_list.remove(delete)
        print(f"\n----- '{delete}' was deleted successfully -----")
    else:
        print("\n----- Sorry, the name isn't in our database -----")


if __name__ == '__main__':
    users_list = []
    choices_list = ["C", "R", "U", "D", "E"]
    print("""
Welcome! What would you to like today?
- "C" to create a user
- "R" to read a user
- "U" to update a user
- "D" to delete a user
- "E" to exit""")
    while True:
        choice_selection()
        if choice == "C":
            create()
        elif choice == "R":
            read()
        elif choice == "U":
            update()
        elif choice == "D":
            delete()
        elif choice == "E":
            print(" "*137, "See you space, cowboy...")
            break