class BankAccount:
    # 1) Class attribute: Title of the bank
    bank_title = "Bank Of Dressrosa"

    # 2) Instance attributes
    def __init__(self, customer_name, current_balance, minimum_balance):
        self.customer_name = customer_name
        self.current_balance = float(current_balance)
        self.minimum_balance = float(minimum_balance)

    # 3) Methods
    def deposit(self, amount):
        amount = float(amount)
        if amount <= 0:
            print("Deposit denied: amount must be positive.")
            return
        self.current_balance += amount
        print(f"Deposit approved: +${amount:.2f} (new balance: ${self.current_balance:.2f})")

    def withdraw(self, amount):
        amount = float(amount)
        if amount <= 0:
            print("Withdrawal denied: amount must be positive.")
            return

        remaining_balance = self.current_balance - amount

        # 4) Add validation: if remaining balance < minimum balance, cannot withdraw
        if remaining_balance < self.minimum_balance:
            print(
                f"Withdrawal denied: remaining balance would be ${remaining_balance:.2f}, "
                f"which is below the minimum balance of ${self.minimum_balance:.2f}."
            )
            print(f"Balance unchanged: ${self.current_balance:.2f}")
            return

        self.current_balance = remaining_balance
        print(f"Withdrawal approved: -${amount:.2f} (new balance: ${self.current_balance:.2f})")

    def print_customer_information(self):
        print("=== Account Info ===")
        print("Bank:", BankAccount.bank_title)
        print("Customer:", self.customer_name)
        print(f"Current Balance: ${self.current_balance:.2f}")
        print(f"Minimum Balance: ${self.minimum_balance:.2f}")
        print("====================\n")


# 5) Create at least two different instances to make sure it works
account1 = BankAccount("Wandering Yonko", 500, 100)
account2 = BankAccount("Big Tuna", 300, 50)

# --- Tests for account1 and account2 ---
account1.print_customer_information()
account1.withdraw(450)
account1.deposit(20)
account1.withdraw(420)
account1.print_customer_information()

account2.print_customer_information()
account2.withdraw(100)
account2.print_customer_information()
