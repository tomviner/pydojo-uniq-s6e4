from unicodedata import normalize


def uniq(f):
    results = []
    previous = None
    for line in f.read().splitlines():
        if normalize('NFKC', line) != previous:
            results.append(line)
            previous = normalize('NFKC', line)
    return results
