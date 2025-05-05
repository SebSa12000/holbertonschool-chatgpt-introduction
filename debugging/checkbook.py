#!/usr/bin/python3
# Define a class to represent a simple checkbook
class Checkbook:
    def __init__(self):
        # Initialize the account balance to zero
        self.balance = 0.0

    # Method to deposit money into the checkbook
    def deposit(self, amount):
        self.balance += amount  # Add the deposit amount to the balance
        print("Deposited ${:.2f}".format(amount))  # Display confirmation
        print("Current Balance: ${:.2f}".format(self.balance))  # Show updated balance

    # Method to withdraw money from the checkbook
    def withdraw(self, amount):
        if amount > self.balance:
            # Check if there are sufficient funds before withdrawing
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount  # Subtract the amount from the balance
            print("Withdrew ${:.2f}".format(amount))  # Display confirmation
            print("Current Balance: ${:.2f}".format(self.balance))  # Show updated balance

    # Method to print the current balance
    def get_balance(self):
        print("Current Balance: ${:.2f}".format(self.balance))

# Main function to interact with the user
def main():
    cb = Checkbook()  # Create a Checkbook object
    while True:
        # Prompt the user for an action
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")

        # Exit the loop and end the program
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            # Loop until valid numeric input is received
            while True:
                try:
                    amount = float(input("Enter the amount to deposit: $"))
                    cb.deposit(amount)
                    break
                except ValueError:
                    print("Invalid amount. Please enter a number.")
        elif action.lower() == 'withdraw':
            # Loop until valid numeric input is received
            while True:
                try:
                    amount = float(input("Enter the amount to withdraw: $"))
                    cb.withdraw(amount)
                    break
                except ValueError:
                    print("Invalid amount. Please enter a number.")
        elif action.lower() == 'balance':
            # Display the current balance
            cb.get_balance()
        else:
            # Handle invalid input
            print("Invalid command. Please try again.")

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()