def uniq(f):
    results = []
    for line in f.read().splitlines():
        if (not results) or (results and line != results[-1]):
            results.append(line)
    return results
