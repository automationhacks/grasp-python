import os
import pytest


@pytest.mark.usefixtures('clean_dir')
class TestDirectoryInit(object):
    def test_cwd_starts_empty(self):
        assert os.listdir(os.getcwd()) == []
        with open('my_file', 'w') as f:
            f.write('hello world!')

    def test_cwd_again_starts_empty(self):
        assert os.listdir(os.getcwd()) == []