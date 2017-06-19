import pytest


@pytest.fixture(scope='function', autouse=True)
def setup_function(request):
    setup_data = request.node.get_marker('setup_data').args[0]

    print(setup_data)
