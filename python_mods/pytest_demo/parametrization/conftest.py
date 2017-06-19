def pytest_addoption(parser):
    parser.addoption('--stringinput', action='append', default=[], help='list of string inputs')


def pytest_generate_tests(metafunc):
    if 'string_input' in metafunc.fixturenames:
        metafunc.parametrize('string_input', metafunc.config.option.stringinput)
