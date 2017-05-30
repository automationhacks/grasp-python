def test_ehlo(smtp3):
    resp, msg = smtp3.ehlo()
    assert resp == 250
    assert 0
