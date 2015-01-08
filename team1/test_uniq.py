import os
import pty
from subprocess import check_output, Popen, PIPE

import pytest

from uniq import uniq_list

NUM_TEST_FILES = 6

@pytest.fixture(params=range(1, NUM_TEST_FILES))
def filenames(request):
    n = request.param
    test_fn = 'test{}'.format(n)
    expected_fn = 'expected{}'.format(n)
    return test_fn, expected_fn

def test_basic_uniq(filenames):
    test_fn, expected_fn = filenames
    with open(test_fn) as f:
        output = uniq_list(f)
    expected = open(expected_fn).read().splitlines()
    assert expected == output


def test_arg(filenames):
    test_fn, expected_fn = filenames
    # returns bytes
    output = check_output(["./uniq.py", test_fn])
    assert open(expected_fn, 'bU').read() == output

def test_stdin():
    # returns bytes
    output = check_output("cat ./test1 | ./uniq.py", shell=1)
    assert open('expected1', 'bU').read() == output

def test_streamed():
    """Test passing in data to the process's stdin

    And receiving data from it's stdout
    Code based on http://stackoverflow.com/a/13605804/15890
    """
    master, slave = pty.openpty()
    process = Popen("python uniq.py", shell=True, stdin=PIPE, stdout=slave)
    stdin_handle = process.stdin
    stdout_handle = os.fdopen(master)
    # Now, we can communicate to the subprocess without closing

    # Write more than 8K here, as that seemed to be the buffer size
    # of pipes on my laptop
    stdin_handle.write(b'bar\n' * 1024)
    stdin_handle.write(b'foo\n' * 1024)
    stdin_handle.write(b'bar\n' * 2048)
    stdin_handle.write(b'foo\n' * 1024)
    stdin_handle.write(b'end\n')
    stdin_handle.close()
    os.close(slave)

    expected = ['bar\n', 'foo\n', 'bar\n', 'foo\n', 'end\n']
    result = []
    try:
        for line in stdout_handle:
            result.append(line)
    except OSError:
        # we get an OSError at the end of the output
        pass

    assert expected == result
