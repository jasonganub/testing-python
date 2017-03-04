class Account(object):
    def __init__(self, data_interface):
        self.di = data_interface

    def get_account(self, id):
        return self.di.get(id)
