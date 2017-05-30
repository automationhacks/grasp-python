

def args_demo(f_arg, *argv):
    print('First Arg: ', f_arg)

    print('Var args ', len(argv))
    print('Length ', argv[0])

args_demo('Gaurav', ['python', 'eggs'])