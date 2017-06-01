import pytest
import tempfile
import os


@pytest.fixture()
def clean_dir():
    new_path = tempfile.mkdtemp()
    os.chdir(new_path)
