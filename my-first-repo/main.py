from bank import BankAccount

def main():
    account = BankAccount("Alice", 100)
    print(account)
    account.deposit(50)
    account.withdraw(30)
    print(account)

if __name__ == "__main__":
    main()
