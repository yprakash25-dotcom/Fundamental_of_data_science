"""Program to demonstrate a BankAccount class with simple deposit and withdrawal operations."""


def format_currency(amount: float) -> str:
    return f"{amount:.2f}"


class BankAccount:
    """A simple bank account class with deposit, withdraw, and display methods."""

    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """Add money to the account balance."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {format_currency(amount)}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount: float) -> None:
        """Withdraw money from the account if funds are sufficient."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient balance for withdrawal.")
        else:
            self.balance -= amount
            print(f"Withdrawn: {format_currency(amount)}")

    def display(self) -> None:
        """Display the account details."""
        print("\nAccount summary:")
        print(f"Owner  : {self.owner}")
        print(f"Balance: {format_currency(self.balance)}")


if __name__ == "__main__":
    print("Bank Account OOP Program")
    owner = input("Enter account owner name: ").strip()
    try:
        initial_balance = float(input("Enter initial balance: ").strip())
    except ValueError:
        print("Invalid balance value. Using 0.0 as initial balance.")
        initial_balance = 0.0

    account = BankAccount(owner, initial_balance)
    account.display()

    try:
        deposit_amount = float(input("Enter amount to deposit: ").strip())
        account.deposit(deposit_amount)
    except ValueError:
        print("Invalid deposit amount.")

    try:
        withdraw_amount = float(input("Enter amount to withdraw: ").strip())
        account.withdraw(withdraw_amount)
    except ValueError:
        print("Invalid withdrawal amount.")

    account.display()
