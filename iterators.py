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

    def __iter__(self):
        self.trans_no = 0
        return self

    def next(self): # will only work in Python 2, __next__ in Python 3.
        if self.trans_no == len(self.transactions):
            raise StopIteration
        self.trans_no += 1
        return self.transactions[self.trans_no -1]



transactions = Transactions()
transactions.add_transaction(Transaction(10, 'paul'))
transactions.add_transaction(Transaction(-5, 'alex'))
transactions.add_transaction(Transaction(100, 'cath'))
transactions.add_transaction(Transaction(-100, 'stu'))

for transaction in transactions:
    print('transaction name %s and amount %s.' %(transaction.name, transaction.amount))

