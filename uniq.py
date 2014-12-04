#! /usr/bin/env python
from unicodedata import normalize
import sys
import os


def uniq(f):
    results = []
    previous = None
    for line in f.read().splitlines():
        if normalize('NFKC', line) != previous:
            results.append(line)
            previous = normalize('NFKC', line)
    return results

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Syntax:')
        print('uniq.py <filename>')
        sys.exit(1)

    target_file = sys.argv[1]
    print(os.linesep.join(uniq(open(target_file))))
