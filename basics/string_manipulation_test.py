from assertpy import assert_that


def test_string_replace():
    msg = 'Hello world'
    assert_that(msg.replace('o', '0')).is_equal_to('Hell0 w0rld')


def test_string_iteration():
    msg_list = []
    msg = "Hello world"
    for char in msg:
        msg_list.append(char)

    assert_that(msg_list).is_equal_to(['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd'])