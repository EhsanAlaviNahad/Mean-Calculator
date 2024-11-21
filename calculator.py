import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

while True:
    numbers = input("Enter Your Amount: ")

    numbers = numbers.replace(',', ' ').split()

    if not all(num.replace('.', '', 1).isdigit() for num in numbers):
        print(Fore.RED + "Invalid Input. Try again:")
        continue

    numbers_list = list(map(float, numbers))

    # Calculation
    mean = sum(numbers_list) / len(numbers_list)

    # Result
    print(Fore.GREEN + f"Avarage: {mean:.2f}")
    
    # Ask if the user wants to try again
    try_again = input(Fore.CYAN + "Do you want to try again? (y/n): ").strip().lower()
    if try_again != "y":
        break
