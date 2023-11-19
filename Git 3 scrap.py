"""Ex3 - Git Commit Mastery"""
accounts = dict()


def account_creation(base, account_id):
    """Account Creation: A function to create a new account
    with a unique account ID and initial balance"""
    base[account_id] = 0.00
    return base
