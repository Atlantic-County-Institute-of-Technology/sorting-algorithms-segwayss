
import os
def main():
    apple_number = 0
    while True:

        print("[-] Which sort would you like?\n"
            "[-] 1. Exit\n"
                "[-] 2. Insertion Sort\n"
                "[-] 3. Bubble Sort")

        selection = int(input("[-] Please select an option:"))

        os.system('cls' if os.name == 'nt' else 'clear')

        if selection == 1:
            exit()
        elif selection == 2:
            print("insertion sort")
        elif selection == 3:
            print("bubble sort")


if __name__ == "__main__":
    main()
print("here for commit")