class Account:
    def __init__(self, balance, nbr):
        self.balance = balance
        self.nbr = nbr

    def withdraw_money(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Not enough funds...")

    def deposit_money(self, amount):
        self.balance += amount

    def __str__(self):
        return "${}".format(round(self.balance, 2))


class CheckingAccount(Account):
    def __init__(self, balance, nbr):
        super().__init__(balance, nbr)

    def __str__(self):
        return "Checking Account #{} \n  Balance: {}".format(self.nbr, Account.__str__(self))


class SavingAccount(Account):
    def __init__(self, balance, nbr):
        super().__init__(balance, nbr)

    def __str__(self):
        return "Saving Account #{} \n  Balance: {}".format(self.nbr, Account.__str__(self))


class BusinessAccount(Account):
    def __init__(self, balance, nbr):
        super().__init__(balance, nbr)

    def __str__(self):
        return "Business Account #{} \n  Balance: {}".format(self.nbr, Account.__str__(self))


class Costumer:
    def __init__(self, name, pin):
        self.name = name
        self.pin = pin
        self.accounts = {'C': [], 'S': [], 'B': []}

    def open_checking(self, balance, nbr):
        self.accounts['C'].append(CheckingAccount(balance, nbr))

    def open_saving(self, balance, nbr):
        self.accounts['S'].append(SavingAccount(balance, nbr))

    def open_business(self, balance, nbr):
        self.accounts['B'].append(BusinessAccount(balance, nbr))

    def total_balance(self):
        total = 0
        for acc in self.accounts['C']:
            print(acc)
            total += acc.balance
        for acc in self.accounts['S']:
            print(acc)
            total += acc.balance
        for acc in self.accounts['B']:
            print(acc)
            total += acc.balance
        print("Total balance is ${}".format(round(total, 2)))

    def make_deposit(self, acc_type, amount):
        for acc in self.accounts[acc_type]:
            acc.deposit_money(amount)

    def make_withdraw(self, acc_type, amount):
        for acc in self.accounts[acc_type]:
            acc.withdraw_money(amount)

    def make_transfer(self, from_acc, to_acc, amount):
        for acc in self.accounts[from_acc]:
            acc.withdraw_money(amount)
        for acc in self.accounts[to_acc]:
            acc.deposit_money(amount)

    def __str__(self):
        return self.name


def check_pin(pin, cust):
    if pin == cust.pin:
        return True
    return False


def show_menu():
    print("\n1. Withdraw Money\n2. Deposit Money\n3. Transfer Money\n4. Show Balance\n5. End Session")


def choose_account():
    account_choice = int(
        input("1. Checking Account\n2. Saving Account\n3. Business Account\nChoose the account to be processed:"))
    if account_choice == 1:
        return 'C'
    elif account_choice == 2:
        return 'S'
    elif account_choice == 3:
        return 'B'


def money_amount():
    amount = float(input("Enter the amount you want to be processed: "))
    return amount

costumer_list = []

endri = Costumer('Endri', 1234)
endri.open_checking(555.55, '001')
endri.open_saving(250.80, '002')
endri.open_business(350, '003')
costumer_list.append(endri)

print("Welcome")
enter_pin = int(input("Please Enter PIN: "))
for costumer in costumer_list:
    if check_pin(enter_pin, costumer):
        while True:
            show_menu()
            choose_menu = int(input("Please choose your action (1-6): "))
            if choose_menu == 1:
                costumer.make_withdraw('C', money_amount())
            elif choose_menu == 2:
                account = choose_account()
                costumer.make_deposit(account, money_amount())
            elif choose_menu == 3:
                print("From")
                from_account = choose_account()
                print("To")
                to_account = choose_account()
                costumer.make_transfer(from_account, to_account, money_amount())
            elif choose_menu == 4:
                costumer.total_balance()
            elif choose_menu == 5:
                print("Have a nice day!")
                break
    else:
        print("Wrong PIN!")
