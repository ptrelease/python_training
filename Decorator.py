# This is the decorator function that is henceforth referrred to as @heading_message('')
# The creation oc th decorator is a bit like a russian doll - but
# essentially returns a decorator function.

# The function names in the decorator are not resereved words - use any names you like
# In fact, I think I could have put the 'heading'implementation directly into
# the 'decorator' function, but at least this demonstrates how functions can be nested.




def heading_message(message):
    def decorator(func):
        def heading(*args, **kwargs):
            print('client is making a %s' % message)
        return heading
    return decorator


class Bank(object):

    balance = 0
    overdraft = 0

    def __init__(self, balance):
        Bank.balance = balance

    @heading_message('get balance')
    def get_balance(self):
        return Bank.balance

    @heading_message('deposit')
    def deposit(self, amount):
        Bank.balance += amount

    @heading_message('withdrawal')
    def withdraw(self, amount):
        check_overdraft = Bank.balance
        if (check_overdraft - amount) > Bank.overdraft:
            Bank.balance -= amount
        else:
            raise Exception('too poor!')




    def set_overdraft(self, overdraft_amount):
        Bank.overdraft = 0 - overdraft_amount


barclays = Bank(10)


print(barclays)
print(barclays.get_balance())
barclays.deposit(10)
print(barclays.get_balance())
barclays.withdraw(15)
print(barclays.get_balance())
print(Bank.overdraft)
barclays.set_overdraft(400)
print(Bank.overdraft)
barclays.withdraw(300)
print(barclays.get_balance())
barclays.withdraw(300)
print(barclays.get_balance())


