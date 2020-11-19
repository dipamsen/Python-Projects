class atm():
    def __init__(self, card_number, pin):
        self.card_number = card_number
        self.pin = pin
        self.amount = 1000

    def cash_withdrawal(self, amount):
        self.amount -= amount
        print("Rs " + str(amount) + " was withdrawn from the account.")

    def balance_enquiry(self):
        print("Current Account Balance = " + str(self.amount))


def main():
    bank_account = atm("ABCD-EFGH-IJKL-MNOP", 1234)
    bank_account.balance_enquiry()
    bank_account.cash_withdrawal(100)
    bank_account.balance_enquiry()


main()
