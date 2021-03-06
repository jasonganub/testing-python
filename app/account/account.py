import requests


class Account(object):
    def __init__(self, data_interface):
        self.di = data_interface

    def get_account(self, id):
        try:
            result = self.di.get(id)
        except ConnectionError:
            result = "Connection error occurred. Try again."
        return result

    def get_current_balance(self, id_num):
        response = requests.get("http://some-account-url/{}".format(id_num))
        return {'status': response.status_code,
                'data': response.text}


class ConnectionError(Exception):
    pass
