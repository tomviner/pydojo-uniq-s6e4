# Team 1's `uniq`

For the state of the code base after the dojo, [see here](https://github.com/ldnpydojo/pydojo-uniq-s6e4/tree/master/team1)

For the extra playing around by Tom, [see here](https://github.com/tomviner/pydojo-uniq-s6e4/tree/master/team1)

Features:

- removes consecutive duplicate lines
- normalises unicode, e.g. diacritic marks
- normalises line endings (default python3 behaviour for file `open`)
- accepts either stdin or filename args
- python 3 only

Usage:

- `python3 uniq.py test1`
- `cat test1 | python3 uniq.py`
- `python3 uniq.py < test1`

## To test

- `pip install pytest`
- `py.test test_uniq.py`

### To compare with gnu `uniq`:

    diff <(uniq test1) <(python3 uniq.py test1)

Note you'll get different output for some of the test files, where the spec of gnu `uniq` doesn't match ours.

### To test streaming output

- python3 print_sleep_print.py | python3 uniq.py

You should see some output, then a 2 second wait, then the rest of the output. If you see all the output in one go, try increasing the amount printed in `print_sleep_print.py:print_lots`

## An unresolved question: how to test the streaming output?

See comments in `test_uniq.py:test_streamed`. We connect to both the stdin and stdout of a process running `python uniq.py`. But despite closing the pipe writting into the process, the output never seems to close, and just blocks as you continue to read. For this reason, we pass a known character at the end of the input, and look for that to signal the end of the output.

Does anyone know how to avoid looking for a special character?

