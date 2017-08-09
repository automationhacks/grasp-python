import pytest


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.failed:
        setattr(item, 'rep' + rep.when, rep)
        print(item)


@pytest.fixture()
def log_screenshot_with_trace(request):
    yield
    node = request.node
    print(node)
