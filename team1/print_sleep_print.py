import time

def print_lots():
    """
    print more than 8Kb
    with some dups
    """
    print('--- start of block ---')
    for i in range(5):
        print('foo\n' * 1408, end='')
        print('bar')
    print('--- end of block ---')

print_lots()
time.sleep(2)
print_lots()
