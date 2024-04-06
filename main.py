print("    ____  ____     ____      ____         _____\n"               
   "   / __ )/ __ \   /  _/___  / __/___     / ___/____ __   _____\n" 
  "  / __  / /_/ /   / // __ \/ /_/ __ \    \__ \/ __ `/ | / / _ \\\n"
 " / /_/ / _, _/  _/ // / / / __/ /_/ /   ___/ / /_/ /| |/ /  __/\n"
"/_____/_/ |_|  /___/_/ /_/_/  \____/   /____/\__,_/ |___/\___/ \n")

print("WARNING! If you don't save the data at the end, it will be lost!")
def start():
    name = input("Please enter your name: ")
    surname = input("Please enter your surname: ")
    age = input("Please enter how name age do you have: ")
    address = input("Please enter your address: ")
    number = input("Please enter your number (without +): ")

    lists = [name, surname, age, address, "+" + number]

    def change_data():
        change = input("What do you want to change? (Name, Surname, Age, Address, Number): ")
        if change.lower() == "name":
            nm = input("Please enter new name: ")
            lists[0] = nm
        elif change.lower() == "surname":
            sr = input("Please enter new surname: ")
            lists[1] = sr
        elif change.lower() == "age":
            ag = input("Please enter new age: ")
            lists[2] = ag
        elif change.lower() == "address":
            ad = input("Please enter new address: ")
            lists[3] = ad
        elif change.lower() == "number":
            nm = input("Please enter new number (without +): ")
            lists[4] = nm

    user = input("\nDo you want to see your information? (y/n): ")

    if user.lower() == "y":
        print("\nYour name: ", lists[0])
        print("Your surname: ", lists[1])
        print("Your age: ", lists[2])
        print("Your address: ", lists[3])
        print("Your number: ", lists[4])
    elif user.lower() == "n":
        pass

    del user
    user = input("\nDo you want to change information? (y/n): ")

    if user.lower() == "y":
        change_data()
        i = True
        while i:
            change = input("Do you want to change anything else? (y/n):")

            if change.lower() == "y":
                change_data()
            else:
                i = False
    elif user.lower() == "n":
        pass

    save = input("Do you want to save your data? (y/n): ")

    if save.lower() == 'y':
        file_name = input("Enter the filename to save: ")
        with open(file_name, 'w') as file:
            file.write(f"Name: {lists[0]}\n")
            file.write(f"Surname: {lists[1]}\n")
            file.write(f"Age: {lists[2]}\n")
            file.write(f"Address: {lists[3]}\n")
            file.write(f"Number: {lists[4]}\n")
            file.close()
        print("Data saved to file!")
        input()
    else:
        print("Data was not saved!")
        input()

bot = input("Have you used this program? (y/n): ")
if bot.lower() == "y":
    user = input("Do you have a save file from this program? (y/n): ")
    if user.lower() == "y":
        enter = input("Please enter file name (Attention, it should be in the program folder!): ")
        try:
            with open(enter, 'r') as file:
                content = file.read()
                print("\nFile content:")
                print(content)
                lists = [content]
        except FileNotFoundError:
            print(f"File '{enter}' not found.")
        del bot
        bot = input("Do you want to enter your data again? (y/n):")
        if bot == "y":
            start()
        elif bot == "n":
            print("Your data remained saved in the same file!")
            input("Press Enter to close the program...")
elif bot.lower() == "n":
    start()
