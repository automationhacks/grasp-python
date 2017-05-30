import pytest
import smtplib


@pytest.fixture(scope='module')
def smtp4(request):
    server = getattr(request.module, 'smtpserver', 'smtp.gmail.com')
    print('\n inside ' + __name__)
    smtp = smtplib.SMTP(server)
    yield smtp
    print('\n finalizing %s (%s)' % (smtp, server))
    smtp.close()

