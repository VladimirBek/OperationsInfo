class Operation:

    def __init__(self,
                 ind: int,
                 state='',
                 date='',
                 amount=None,
                 description='',
                 sender_acc='---',
                 recipient_acc=''
                 ):
        self.ind = ind
        self.state = state
        self.date = date
        if amount is None:
            self.amount = {}
        self.amount = amount
        self.description = description
        self.sender_acc = sender_acc
        self.recipient_acc = recipient_acc

    def __repr__(self):
        return f'Operation(id={self.ind}, ' \
               f'state={self.state}, ' \
               f'date={self.date}, ' \
               f'operationAmount={self.amount} ' \
               f'description={self.description} ' \
               f'sender_acc={self.sender_acc} ' \
               f'recipient_acc={self.recipient_acc})'
