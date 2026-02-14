from bank_account import BankAccount


class SavingsAccount(BankAccount):

    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, interest_rate):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.interest_rate = float(interest_rate)

    def apply_interest(self):
        if self.interest_rate <= 0:
            print("Interest denied: interest rate must be positive.")
            return

        interest = self.current_balance * self.interest_rate
        self.current_balance += interest
        print(f"Interest applied: +${interest:.2f} (new balance: ${self.current_balance:.2f})")
