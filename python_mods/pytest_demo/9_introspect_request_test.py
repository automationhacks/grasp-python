def test_ehlo(smtp4):
    resp, msg = smtp4.ehlo()
    assert resp == 250
    assert 0
