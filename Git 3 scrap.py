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
        return "You've entered an incorrect value, try again."
    base[account_id] += float(deposit_input)
    return deposit_input