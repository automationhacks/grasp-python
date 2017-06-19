import pytest


class Cert:
    def __init__(self, dsn, user_name, pwd):
        self.dsn = dsn
        self.user_name = user_name
        self.pwd = pwd

    def generate_cert(self):
        return self.dsn + self.user_name + self.pwd


@pytest.fixture(scope='module')
def get_cert(request):
    dsn, user_name, pwd = request.param
    yield Cert(dsn, user_name, pwd).generate_cert()
    print('teardown logic')
