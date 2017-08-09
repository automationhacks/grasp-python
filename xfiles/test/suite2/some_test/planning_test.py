from xfiles.test.src.wrapper import *


class TestClass:
    x = find('dummy1.yml')

    def test_foo(self):
        print(self.x)
        assert 0

    def test_bar(self):
        pass