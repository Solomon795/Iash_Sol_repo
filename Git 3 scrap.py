"""Ex3 - Git Commit Mastery"""
accounts = dict()


def account_creation(base, account_id):
    """Account Creation: A function to create a new account
    with a unique account ID and initial balance"""
    base[account_id] = 0.00
    return base


def check_balance(base, account_id):
    """Balance Inquiry: A function to check the current balance
    of a given account ID."""
    return base[account_id]


def deposit(base, account_id, deposit_input):
    """Deposit: A function to deposit an amount to a specific account,
    updating the balance."""
    if not all(char.isdigit() or char == '.' for char in deposit_input):
        deposit_amount = "You've entered an incorrect value, try again."
        return deposit_amount
    deposit_amount = float(deposit_input)
    base[account_id] += deposit_amount
    return deposit_amount


def withdrawal(base, account_id, withdrawal_input):
    """Withdrawal: A function to withdraw an amount from a specific account,
    updating the balance if sufficient funds exist."""
    if not all(char.isdigit() or char == '.' for char in withdrawal_input):
        withdrawal_amount = "You've entered an incorrect value, try again."
        return withdrawal_amount
    withdrawal_amount = float(withdrawal_input)
    if base[account_id] - withdrawal_amount < 0:
        withdrawal_amount = "You're low on your funds!"
        return withdrawal_amount
    base[account_id] -= withdrawal_amount
    return withdrawal_amount


def account_summary(base, account_id):
    """Account Summary: A function to print a summary of an account,
    including the account ID and current balance"""
    return (f"Your account ID: {account_id} "
            f"Your current balance: {base[account_id]} $")


def main():
    global accounts
    while True:
        input_id = input("Greetings!\nEnter your account ID number in format XXXX.\n"
                         "If entered ID doesn't exist, it will be created.\n"
                         "To exit the program, type '-e': \n")
        if not input_id.isnumeric() and input_id != '-e':
            print("You're allowed to enter only 4 digits!")
        elif input_id == '-e':
            break
        elif not len(input_id) == 4:
            print("You're allowed to enter only 4 digits!")
        elif input_id in accounts:
            option = input("Your account is in our base! Choose what you'd like to do\n"
                           "-c for checking balance\n"
                           "-d for making deposit\n"
                           "-w for withdrawing cash\n"
                           "-s for account summary\n"
                           "-e for exiting\n")

            if option == "-c":
                print(f"Your current balance now is:\n {check_balance(accounts, input_id)} $")
            elif option == "-d":
                deposit_input = input("How much (XXXX.XX $) would you like to deposit?: ")
                if deposit(accounts, input_id, deposit_input) == ("You've entered an incorrect value, "
                                                                  "try again."):
                    print("You've entered an incorrect value, try again.")
                    break
                print(f"Balance of account {input_id} has been updated "
                      f"(+{deposit_input}$).\n"
                      f"Now you have: {accounts[input_id]} $.")
            elif option == "-w":
                withdrawal_input = input("How much cash (XXXX.XX $) would you like to withdraw?: ")
                if withdrawal(accounts, input_id, withdrawal_input) == "You're low on your funds!":
                    print("You're low on your funds!")
                else:
                    print(f"Balance of account {input_id} has been updated (-{withdrawal_input} $.\n"
                          f"Now you have: {accounts[input_id]} $.")
            elif option == "-s":
                print(account_summary(accounts, input_id))
            elif option == "-e":
                break
            else:
                print("You did not pick an existing function, try again.")

            final_option = input("Is there something else you'd like to do ('y'/'any other key')? ")
            if final_option.lower() == "y":
                main()
            else:
                break
            break
        else:
            account_creation(accounts, input_id)
            print(f"Account ID {input_id} created!"
                  f"You have 0$ on your balance right now."
                  f"You're now returned to main menu")


if __name__ == "__main__":
    assert account_creation({}, "1111") == {"1111": 0.00}
    assert check_balance({"0001": 50, "0002": 1000}, "0001") == 50.0
    assert deposit({"0001": 50, "0002": 1000}, "0002", "25.50") == 25.50
    assert withdrawal({"0001": 50, "0002": 1000}, "0002", "800.80") == 800.80
    assert account_summary({"0001": 50, "0002": 1000}, "0002") == "Your account ID: 0002 Your current balance: 1000 $"
    print("All tests are passed!")
    main()
