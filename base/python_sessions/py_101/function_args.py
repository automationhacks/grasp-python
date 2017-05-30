

def welcome_user(*user_name, welcome_msg='Welcome to world of Python'):
    full_name = ''
    
    for name in user_name:
        full_name = '%s %s ' % (full_name, name)
    print('Hi %s, %s' % (full_name, welcome_msg))

welcome_user('Gaurav', 'Singh')
welcome_user('Gaurav', 'Singh', welcome_msg='Variable + Keyword args')


