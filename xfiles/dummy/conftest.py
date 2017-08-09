import pytest
import traceback


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.failed and call.excinfo is not None:
        etype = call.excinfo.type
        value = call.excinfo.value
        tb = call.excinfo.traceback

        string = '{} {} {}'.format(etype, value, str(tb[::-1]))

        # string = traceback.print_tb(tb)
        # string2 = traceback.extract_tb(tb)
        # string3 = traceback.format_tb(tb)

    print(outcome)
