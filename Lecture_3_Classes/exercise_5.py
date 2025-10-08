# ================================
# Challenge Exercise: Advanced Classes
# ================================

# Challenge: Build a Simple Banking System

class BankAccount:
    """
    Create a BankAccount class with the following features:
    - Account holder name
    - Account number (should be unique)
    - Balance (private, starts at 0)
    - Transaction history
    """

    # Class variable to track next account number
    next_account_number = 1000

    def __init__(self, holder_name):
        """Initialize a new bank account"""
        self.holder_name = holder_name
        self.account_number = BankAccount.next_account_number  # Assign unique account number
        self._balance = 0  # Private attribute (convention: prefix with _)
        self.transaction_history = []
        BankAccount.next_account_number += 1
        # Increment the class variable for next account
        ...

    def deposit(self, amount):
        """
        Deposit money into the account.
        - Check if amount is positive
        - Update balance
        - Record transaction
        """
        if amount <= 0:
            print("Deposit amount must be positive!")
            return False
        self._balance += amount
        self.transaction_history.append(amount)

        ...  # Update balance
        ...  # Add to transaction history
        print(f"Deposited ${amount:.2f}. New balance: ${self._balance:.2f}")
        return True

    def withdraw(self, amount):
        """
        Withdraw money from the account.
        - Check if amount is positive
        - Check if sufficient balance
        - Update balance
        - Record transaction
        """
        is_success = False
        if amount <= 0:
            print("Withdraw amount must be positive!")
            is_success = False
        if self._balance - amount >= 0:
            self._balance -= amount
            self.transaction_history.append(-1 * amount)
            print(f"Withdrew ${amount:.2f}. New balance: ${self._balance:.2f}")
            is_success = True
        return is_success


    def get_balance(self):
        """Return the current balance"""
        return self._balance

    def transfer(self, amount, recipient_account):
        """
        Transfer money to another account.
        - Withdraw from this account
        - Deposit to recipient account
        """
        if self.withdraw(amount):
            self.transaction_history.append(-1 * amount)
            recipient_account.deposit(amount)
            recipient_account.transaction_history.append(amount)

    def print_statement(self):
        """Print account statement with all transactions"""
        print(f"\n=== Account Statement ===")
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.holder_name}")
        print(f"Current Balance: ${self._balance:.2f}")
        print("\nTransaction History:")
        for transaction in self.transaction_history:
            print(f"  {transaction}")

    def __str__(self):
        """String representation of the account"""
        return f"Account {self.account_number} ({self.holder_name}): ${self._balance:.2f}"


# ================================
# Challenge Extension: Savings Account
# ================================

class SavingsAccount(BankAccount):
    """
    Extend BankAccount to create a SavingsAccount with:
    - Interest rate
    - Minimum balance requirement
    - Method to apply interest
    """

    def __init__(self, holder_name, interest_rate=0.02, min_balance=100):
        """Initialize savings account with interest rate and minimum balance"""
        super().__init__(holder_name)
        self.interest_rate = interest_rate
        self.min_balance = min_balance

    def withdraw(self, amount):
        """
        Override withdraw to enforce minimum balance.
        """
        # Check if withdrawal would violate minimum balance
        if self._balance - amount < self.min_balance:
            print(f"Cannot withdraw. Minimum balance of ${self.min_balance:.2f} required.")
            return False

        # Call parent class withdraw method
        return super().withdraw(amount)

    def apply_interest(self):
        """Apply interest to the current balance"""
        interest = ...  # Calculate interest
        ...  # Add interest to balance
        ...  # Record transaction
        print(f"Interest of ${interest:.2f} applied. New balance: ${self._balance:.2f}")


# ================================
# Test Your Banking System
# ================================

if __name__ == "__main__":
    # Create two regular accounts
    alice_account = BankAccount("Alice Smith")
    bob_account = BankAccount("Bob Jones")

    # Test deposits
    alice_account.deposit(1000)
    bob_account.deposit(500)

    # Test withdrawal
    alice_account.withdraw(200)

    # Test transfer
    alice_account.transfer(100, bob_account)

    # Print statements
    alice_account.print_statement()
    bob_account.print_statement()

    # Create a savings account
    savings = SavingsAccount("Charlie Brown", interest_rate=0.03, min_balance=500)
    savings.deposit(1000)
    savings.apply_interest()

    # Try to withdraw below minimum
    savings.withdraw(600)  # Should fail
    savings.withdraw(400)  # Should succeed

    savings.print_statement()
