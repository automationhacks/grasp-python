import smtplib
import pytest


@pytest.fixture(scope='module')  # executed once for all test methods
def smtp():
    smtp = smtplib.SMTP('smtp.gmail.com')
    yield smtp  # provide fixture value
    print('executing teardown code')
    smtp.close()


@pytest.fixture(scope='module')
def smtp2():
    with smtplib.SMTP('smtp.gmail.com') as smtp:  # another way
        yield smtp
        print('executing teardown code using with')
