import os

# Function to display the current balance
def view_balance(transactions):
    return sum(transactions)

# Function to add a debit (withdrawal)
def record_debit(transactions, amount):
    transactions.append(-amount)

# Function to add a credit (deposit)
def record_credit(transactions, amount):
    transactions.append(amount)

# Function to exit the application
def exit_program(transactions):
    with open("ledger.txt", "w") as ledger_file:
        for transaction in transactions:
            ledger_file.write(f"{transaction}\n")
    print("Thanks, have a great day!")

# Main function
def main():
    if not os.path.exists("ledger.txt"):
        with open("ledger.txt", "w") as ledger_file:
            ledger_file.write("0\n")

    with open("ledger.txt", "r") as ledger_file:
        transactions = [float(line) for line in ledger_file]

    while True:
        print("\n~~~ Welcome to your terminal checkbook! ~~~")
        print("What would you like to do?\n")
        print("1) view current balance")
        print("2) record a debit (withdraw)")
        print("3) record a credit (deposit)")
        print("4) exit")

        choice = input("Your choice? ")

        if choice == '1':
            balance = view_balance(transactions)
            print(f"Your current balance is ${balance:.2f}.")
        elif choice == '2':
            amount = float(input("How much is the debit? $"))
            record_debit(transactions, amount)
        elif choice == '3':
            amount = float(input("How much is the credit? $"))
            record_credit(transactions, amount)
        elif choice == '4':
            exit_program(transactions)
            break
        else:
            print("Invalid choice:", choice)

if __name__ == "__main__":
    main()