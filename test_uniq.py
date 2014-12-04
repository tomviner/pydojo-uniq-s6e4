import pytest

from uniq import uniq

@pytest.mark.parametrize("n", range(1, 6))
def test_basic_uniq(n):
    with open('test{}'.format(n)) as f:
        output = uniq(f)
    expected = open('expected{}'.format(n)).read().splitlines()
    assert expected == output
