class Account(object):
    def __init__(self, data_interface):
        self.di = data_interface

    def get_account(self, id):
        try:
            result = self.di.get(id)
        except ConnectionError:
            result = "Connection error occurred. Try again."
        return result


class ConnectionError(Exception):
    pass
