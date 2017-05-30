def test_ehlo(smtp5):
    resp, msg = smtp5.ehlo()
    assert resp == 250
    assert 0
