#! /usr/bin/env python
from unicodedata import normalize
import fileinput


def uniq_list(f=None):
    return list(uniq(f))

def uniq(f=None):
    previous = None
    for line in f or fileinput.input():
        line = line.rstrip()
        if normalize('NFKC', line) != previous:
            yield line
            previous = normalize('NFKC', line)

if __name__ == '__main__':
    for line in uniq():
        print(line)
