from uniq import uniq

def test_basic_uniq():
    with open('test1') as f:
        output = uniq(f)
    expected = open('expected1').read().splitlines()
    assert expected == output
    
