str1 = 'Gaurav'
str2 = 'Rajesh'
str3 = 'Rajesh'

cnt = 0

def pass_counter(cnt):
    cnt += 1
    return cnt

try:
    assert (str2 == str3), 'Strings dont match - 1'
    cnt = pass_counter(cnt)
    assert (str2 == str3), 'Strings dont match - 1'
    cnt = pass_counter(cnt)
    assert (str1 == str3), 'Strings dont match - 2'
    pass_counter(cnt)
except AssertionError as e:
    print('Came here')
    print(str(e))
finally:
    print(cnt)