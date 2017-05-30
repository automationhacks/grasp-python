smtpserver = 'mail.python.org'


def test_ehlo(smtp4):
    assert 0, smtp4.helo()
