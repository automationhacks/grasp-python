import pytest


class DB(object):
    def __init__(self):
        self.intrasection = []

    def begin(self, name):
        self.intrasection.append(name)

    def rollback(self):
        self.intrasection.pop()


@pytest.fixture(scope='module')
def db():
    return DB()


class TestClass(object):

    @pytest.fixture(autouse=True)
    def transact(self, request, db):
        db.begin(request.function.__name__)
        yield
        db.rollback()

    def test_method1(self, db):
        assert db.intrasection == ['test_method1']

    def test_method2(self, db):
        assert db.intrasection == ['test_method2']
