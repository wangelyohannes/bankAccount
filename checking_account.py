from bank_account import BankAccount


class CheckingAccount(BankAccount):

    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, transfer_limit):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.transfer_limit = float(transfer_limit)

    def transfer(self, amount):
        amount = float(amount)

        if amount <= 0:
            print("Transfer denied: amount must be positive.")
            return

        if amount > self.transfer_limit:
            print(f"Transfer denied: amount exceeds transfer limit of ${self.transfer_limit:.2f}.")
            return

        remaining_balance = self.current_balance - amount

        if remaining_balance < self.minimum_balance:
            print(
                f"Transfer denied: remaining balance would be ${remaining_balance:.2f}, "
                f"which is below the minimum balance of ${self.minimum_balance:.2f}."
            )
            print(f"Balance unchanged: ${self.current_balance:.2f}")
            return

        self.current_balance = remaining_balance
        print(f"Transfer approved: -${amount:.2f} (new balance: ${self.current_balance:.2f})")
