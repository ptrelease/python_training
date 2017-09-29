# Like the iterator - but is a generator instead.

transactions = {"alex": -5, "paul": 10, "stu": 100, "cath": -100}


class Transaction(object):

    def __init__(self, amount, name):
        self.amount = amount
        self.name = name


class Transactions(object):

    def __init__(self):
        self.transactions=[]

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def generator_function_to_get_transaction(self):
    # This is the generator.
        count = 0
        while count < len(self.transactions):
            yield self.transactions[count]
            count += 1

transactions = Transactions()
transactions.add_transaction(Transaction(10, 'paul'))
transactions.add_transaction(Transaction(-5, 'alex'))
transactions.add_transaction(Transaction(100, 'cath'))
transactions.add_transaction(Transaction(-100, 'stu'))

# So here, rather than loop through the tranactions, use the
# generator to return a transaction at a time.
for transaction in transactions.generator_function_to_get_transaction():
    print('transaction name %s and amount %s.' %(transaction.name, transaction.amount))

