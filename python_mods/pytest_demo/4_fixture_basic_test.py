"""
tmpdir specified in test func signature will ensure pytest does a look up
and calls a fixture factory to create the resource before performing test func
"""


def test_needs_files(tmpdir):
    print(tmpdir)
    assert 0
