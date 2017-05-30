def test_ehlo(smtp):
    resp, msg = smtp.ehlo()
    assert resp == 250
    assert b'smtp.gmail.com' in msg
    assert 0


def test_noop(smtp):
    resp, msg = smtp.noop()
    assert resp == 250
    assert 0


def test_noop2(smtp2):
    resp, msg = smtp2.noop()
    assert resp == 250
    assert 0
