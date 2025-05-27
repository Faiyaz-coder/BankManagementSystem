from datetime import datetime
import random
import sys
import os

os.system("cls") # to clean unusual things from display (Terminal)

# Display Bank name center top of the screen
BankName = "-----  National Bank of India  -----"

#Screen width (for example, 120 characters wide)
screen_width = 120

# Centering the bank name within the screen width
print(BankName.center(screen_width))

class UserInput:
    def __init__(self, name=None, password=None, age=None, email=None, deposite=None):
        self.name = name
        self.password = password
        self.age = age
        self.email = email
        self.deposite = deposite
        self.account_number = self.generate_account_number()

    # Generating account nunmber
    def generate_account_number(self):
        # Account number ko 10 digit ka random number generate karne ke liye
        account_number = random.randint(8000000000, 9999999999)  # 10 digit number
        return account_number

    def get_user_input(self):
        # Name Input
        while True:
            print("If you want to exit the page at any time, press (1) and (Enter).\n")

            self.name = input("Enter your name: ") # Name input

            if self.name == "1": # to stop programe
                print("\nExiting the page.")
                sys.exit()
            
            if all(part.isalpha() for part in self.name.split()):  # Space se split kar ke har part check karte hain
                break
            else:
                print("Invalid name! Name should contain only letters. Try again.")
            
        # password input
        while True:
            self.password = input("Create a Password (minimum 8 characters) : ")

            if self.password == "1": # to stop programe
                print("\nExiting the page.")
                sys.exit()

            if len(self.password) >= 8: # to make sure len of password requirement
                break
            else:
                print("Length of password should be at least 8 characters, Please try agian.")
     
        # Age input
        while True:
            self.age = input("Enter Holder's Age in Numbers : ")

            if self.age == "1": # to stop program
                print("\nExiting the page.")
                sys.exit()

            if not self.age.isdigit():
                print("Invalid Number. Please enter a number in digits!")
                continue

            self.age = int(self.age) # convert into integer

            if self.age > 100:  # age limit restriction
                print("Age must be 100 or less. Please enter an age within the range.")
                continue
            elif self.age >= 18: # minimum age limit
                break
            else:
                print("Age must be 18 or older. Please try again.!")

        # Email input
        while True:
            self.email = input("Enter your email: ")

            if self.email == "1": # to stop program
                print("\nExiting the page.")
                sys.exit()

            if "@" in self.email and "." in self.email:
                break
            else:
                print("Invalid email address! Please try again.")
                continue

        while True:
            self.deposite = input("Enter amount you want to deposite: ")

            if self.deposite == "1": # to stop program
                print("\nExiting the page.")
                sys.exit()

            if not self.deposite.isdigit():
                print("Invalid Number. Please enter a number in digits!")
                continue

            self.deposite = int(self.deposite) # convert into integer
            break

        # Account successfully create hone par yeh message print karenge
        self.balance = self.deposite  # Assign initial deposit to balance
        print(f"\nWelcome {self.name}! Your account has been created successfully.")
    
    # Display details   
    def display_acc_details(self):
        os.system("cls") # to clean unusual things from display (Terminal)
        print(BankName.center(screen_width))
        print("----- Account Details -----\n")
        print(f"Name :       \t{self.name}")
        print(f"Account No : \t{self.account_number}")
        print(f"Password :   \t{self.password}")
        print(f"Age :        \t{self.age}")
        print(f"Email :      \t{self.email}")
        print(f"Balance :    \t{self.balance}")
            
# BankAccount Class inheriting from UserInput
class BankAccount(UserInput):
    def __init__(self, balance=0):
        super().__init__()   # Call the constructor of the UserInput class
        self.balance = balance # Initial balance is 0
        self.passbook = [] # List to store transactions
        self.current_datetime = datetime.now() # date and time for transaction history

    def debit(self, amount): # when amount debit in account
        if amount > self.balance:
            print("Insufficient balance!")
            self.passbook.append(f"Rs.{amount}\t Failed \t on {self.current_datetime.strftime("%d-%m-%Y \t\t at %H:%M:%S %p.")}\t (Insufficient Balance)")
        else:
            self.balance -= amount
            os.system("cls")
            print(f"\nRs.{amount} has been Debited on {self.current_datetime.strftime("%d-%m-%Y at %H:%M:%S %p.")} Your available balance is Rs.{self.balance}")
            self.passbook.append(f"Rs.{amount}\t Debited \t on {self.current_datetime.strftime("%d-%m-%Y \t\t at %H:%M:%S %p.")}\t Available Balance: {self.balance}") # collecting transation history to passbook

    def credit(self, amount): # when amount credit in account
        self.balance += amount
        os.system("cls")
        print(f"\nRs.{amount} has been Credited on {self.current_datetime.strftime("%d-%m-%Y at %H:%M:%S %p.")} Your available balance is Rs.{self.balance}.")
        self.passbook.append(f"Rs.{amount}\t Credited \t on {self.current_datetime.strftime("%d-%m-%Y \t\t at %H:%M:%S %p.")}\t Available Balance: {self.balance}") # collecting transation history to passbook

    def show_passbook(self):
        print("\n\t\t\t\t\t----- Passbook -----\n")
        print("-- Amount --\t-- Dr/Cr --\t  -- Date --\t\t   -- Time --\t\t        -- Status --\n")
        if self.passbook:
            for transaction in self.passbook:
                print(transaction)
        else:
            print("No transactions yet")

    @staticmethod
    def main_menu():
        account = None  # Initialize account variable
    
        while True:
            os.system("cls")
            print(BankName.center(screen_width))
            print("\n----- Main Menu -----")
            print("1. Create a New Account")
            print("2. View Account Details")
            print("3. Credit Money")
            print("4. Debit Money")
            print("5. View Passbook")
            print("6. Exit")

            choice = input("\nEnter your choice: ")

            if choice == "1":
                os.system("cls")
                print(BankName.center(screen_width))
                print("\n--- Create a New Account ---")
                if account is None:
                    account = BankAccount()
                    account.get_user_input()
                    input("\nPress Enter to continue...")
                else:
                    print("Account already exists! You cannot create a new account.")
                    input("\nPress Enter to continue...")

            elif choice == "2":
                print(BankName.center(screen_width))
                if account is not None:
                    account.display_acc_details()
                    input("\nPress Enter to continue...")
                else:
                    print("No account found! Please create an account first.")
                    input("\nPress Enter to continue...")

            elif choice == "3":
                if account is not None:
                    os.system("cls")
                    print(BankName.center(screen_width))
                    try:
                        amount = float(input("Enter amount to credit: "))
                        if amount > 0:
                            account.credit(amount)
                        else:
                            print("Amount must be greater than 0.")
                    except ValueError:
                        print("Invalid input! Enter a valid amount.")
                else:
                    print("No account found! Please create an account first.")
                input("\nPress Enter to continue...")

            elif choice == "4":
                if account is not None:
                    os.system("cls")
                    print(BankName.center(screen_width))
                    try:
                        amount = float(input("Enter amount to debit: "))
                        if amount > 0:
                            account.debit(amount)
                        else:
                            print("Amount must be greater than 0.")
                    except ValueError:
                        print("Invalid input! Enter a valid amount.")
                else:
                    print("No account found! Please create an account first.")
                input("\nPress Enter to continue...")

            elif choice == "5":
                if account is not None:
                    os.system("cls")
                    print(BankName.center(screen_width))
                    account.show_passbook()
                else:
                    print("No account found! Please create an account first.")
                input("\nPress Enter to continue...")

            elif choice == "6":
                os.system("cls")
                print(BankName.center(screen_width))
                print("\nThank you for using Private Bank! Have a great day!\n")
                break
            else:
                print("Invalid choice! Please try again.")
                input("\nPress Enter to continue...")

# Start the program
if __name__ == "__main__":
    BankAccount.main_menu()