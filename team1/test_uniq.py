from subprocess import check_output

import pytest

from uniq import uniq

NUM_TEST_FILES = 6

@pytest.mark.parametrize("n", range(1, NUM_TEST_FILES))
def test_basic_uniq(n):
    with open('test{}'.format(n)) as f:
        output = uniq(f)
    expected = open('expected{}'.format(n)).read().splitlines()
    assert expected == output


@pytest.mark.parametrize("n", range(1, NUM_TEST_FILES))
def test_arg(n):
    # returns bytes
    output = check_output(["./uniq.py", "./test{}".format(n)])
    assert open('expected{}'.format(n), 'bU').read() == output

def test_stdin():
    # returns bytes
    output = check_output("cat ./test1 | ./uniq.py", shell=1)
    assert open('expected1', 'bU').read() == output
