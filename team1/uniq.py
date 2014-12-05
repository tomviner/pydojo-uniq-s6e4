#! /usr/bin/env python
from unicodedata import normalize

import fileinput
import os

def uniq(f=None):
    results = []
    previous = None
    for line in f or fileinput.input():
        line = line.rstrip()
        if normalize('NFKC', line) != previous:
            results.append(line)
            previous = normalize('NFKC', line)
    return results

if __name__ == '__main__':
    print(os.linesep.join(uniq()))
