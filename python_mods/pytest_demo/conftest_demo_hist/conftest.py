import smtplib
import pytest


@pytest.fixture(scope='module')
def smtp3(request):
    smtp = smtplib.SMTP('smtp.gmail.com')

    def fin():  # gets executed after all tests are run
        print('\n executing teardown using request.finalizer')
        smtp.close()

    request.addfinalizer(fin)
    return smtp  # provide fixture value
