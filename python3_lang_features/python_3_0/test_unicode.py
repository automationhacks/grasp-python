def test_unicode():
    # Before
    text = "café"
    # In Python 2, this is a byte string, and the 'é' character is represented as two bytes.
    print(text)

    # After
    text = "café"
    # In Python 3, this is a Unicode string, and the 'é' character is represented as a single Unicode code point.
    print(text)
    # To get the byte representation of the string, you can encode it using a specific encoding (e.g., UTF-8).
    data = text.encode()
    print(data)
