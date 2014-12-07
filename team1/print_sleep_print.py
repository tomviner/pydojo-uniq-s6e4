import time

def print_lots():
    """
    print more than 8K
    with some dups
    """
    print('start123')
    for i in range(5):
        # output 4k
        print('foo\n' * 408, end='')
        print('bar\n', end='')
    print('end\n', end='')

print_lots()

time.sleep(2)

print_lots()
