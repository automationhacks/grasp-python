import pytest
import smtplib


@pytest.fixture(scope='module', params=['smtp.gmail.com', 'mail.python.org'])
def smtp5(request):
    with smtplib.SMTP(request.param) as smtp:  # request.param - fixture accesses values
        yield smtp
        print('\nfinalizing ', smtp)
