# atm_system.py

class ATM:
    def __init__(self, name, balance, pin):
        self.name = name
        self.__balance = balance
        self.__pin = pin

    def check_pin(self, entered_pin):
        return entered_pin == self.__pin

    def deposit(self, amount):
        self.__balance += amount
        print(f"Amount Deposited Successfully: ${amount}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdraw Successful: ${amount}")
        else:
            print("Insufficient Balance")

    def check_balance(self):
        print(f"Available Balance: ${self.__balance}")

# Create user account
user = ATM("xyz", 5000, 1234)

# PIN verification
pin = int(input("Enter PIN: "))

if user.check_pin(pin):
    print(f"\nWelcome {user.name}!")
    
    # Optional: Use the money variable if needed
    withdraw_amount = int(input("Enter amount to withdraw: $"))
    user.withdraw(withdraw_amount)
    
    # Additional operation
    user.check_balance()
else:
    print("Incorrect PIN")
