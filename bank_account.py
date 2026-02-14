class BankAccount:
    bank_title = "Bank Of Dressrosa"

    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        self.customer_name = customer_name
        self.current_balance = float(current_balance)
        self.minimum_balance = float(minimum_balance)

        self._account_number = account_number
        self.__routing_number = routing_number        

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
        print(f"Account Number: {self._account_number}")
        print(f"Routing Number: {self.get_routing_number()}")
        print("====================\n")

    def get_routing_number(self):
        return self.__routing_number
