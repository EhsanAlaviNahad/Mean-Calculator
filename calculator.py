import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

print(Fore.CYAN + "Welcome.")

while True:
    numbers = input("Enter Your Amount: ")

    numbers = numbers.replace(',', ' ').split()

    if not all(num.replace('.', '', 1).isdigit() for num in numbers):
        print(Fore.RED + "Invalid Input. Try again:")
        continue

    numbers_list = list(map(float, numbers))

    #Calculation
    mean = sum(numbers_list) / len(numbers_list)
    
    #Result
    print(Fore.GREEN + f"Avarage: {mean:.2f}")
    break
