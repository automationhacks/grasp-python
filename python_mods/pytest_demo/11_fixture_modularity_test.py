import pytest
import smtplib


class App(object):
    def __init__(self, smtp6):
        self.smtp = smtp6


@pytest.fixture(scope='function', params=['smtp.gmail.com', 'mail.python.org'])
def smtp(request):
    smtp = smtplib.SMTP(request.param)
    yield smtp
    print('executing teardown in ', __name__)
    smtp.close()


@pytest.fixture(scope='function')
def app(smtp):
    return App(smtp)


def test_smtp_exists(app):
    assert app.smtp
    assert 0
