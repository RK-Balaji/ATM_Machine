class User:
    def __init__(self, user_id, pin):
        self.user_id = user_id
        self.pin = pin
        self.balance = 1000  # Initial balance
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited ${amount}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")
        else:
            print("Insufficient balance.")

    def transfer(self, recipient, amount):
        if self.balance >= amount:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(f"Transferred ${amount} to {recipient.user_id}")
        else:
            print("Insufficient balance.")

    def view_transaction_history(self):
        for transaction in self.transaction_history:
            print(transaction)

class ATM:
    def __init__(self):
        self.users = {}

    def authenticate_user(self, user_id, pin):
        if user_id in self.users and self.users[user_id].pin == pin:
            return self.users[user_id]
        else:
            return None

def main():
    atm = ATM()

    # Create sample users
    user1 = User("user123", "1234")
    user2 = User("user456", "5678")

    atm.users[user1.user_id] = user1
    atm.users[user2.user_id] = user2

    while True:
        print("-----------------------------------------------------")
        print("\nATM INTERFACE TASK")
        print("1. Transactions History")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Transfer")
        print("5. Quit")
        print("-----------------------------------------------------")

        choice = input("Enter your choice: ")

        if choice == "1":
            user_id = input("Enter your user ID: ")
            pin = input("Enter your PIN: ")

            user = atm.authenticate_user(user_id, pin)

            if user:
                user.view_transaction_history()
            else:
                print("Authentication failed.")

        elif choice == "2":
            user_id = input("Enter your user ID: ")
            pin = input("Enter your PIN: ")
            amount = float(input("Enter the withdrawal amount: "))

            user = atm.authenticate_user(user_id, pin)

            if user:
                user.withdraw(amount)
                print(f"Withdrew ${amount}")
            else:
                print("Authentication failed.")

        elif choice == "3":
            user_id = input("Enter your user ID: ")
            pin = input("Enter your PIN: ")
            amount = float(input("Enter the deposit amount: "))

            user = atm.authenticate_user(user_id, pin)

            if user:
                user.deposit(amount)
                print(f"Deposited ${amount}")
            else:
                print("Authentication failed.")

        elif choice == "4":
            user_id = input("Enter your user ID: ")
            pin = input("Enter your PIN: ")
            recipient_id = input("Enter the recipient's user ID: ")
            amount = float(input("Enter the transfer amount: "))

            user = atm.authenticate_user(user_id, pin)
            recipient = atm.users.get(recipient_id)

            if user and recipient:
                user.transfer(recipient, amount)
                print(f"Transferred ${amount} to {recipient_id}")
            else:
                print("Authentication or recipient not found.")

        elif choice == "5":
            print("Exiting ATM.")
            break

if __name__ == "__main__":
    main()
