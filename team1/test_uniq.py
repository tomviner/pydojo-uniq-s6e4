from subprocess import check_output

import pytest

from uniq import uniq

@pytest.mark.parametrize("n", range(1, 6))
def test_basic_uniq(n):
    with open('test{}'.format(n)) as f:
        output = uniq(f)
    expected = open('expected{}'.format(n)).read().splitlines()
    assert expected == output


def test_arg():
    # returns bytes
    output = check_output(["./uniq.py", "./test1"])
    assert open('expected1', 'bU').read() == output

def test_stdin():
    # returns bytes
    output = check_output("cat ./test1 | ./uniq.py", shell=1)
    assert open('expected1', 'bU').read() == output
