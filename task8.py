def get_next(m, prev):
    next = m[prev][0]
    del m[prev]
    return m, next



def overlapping(k, a, b):
    return max([ i if a[k-i:] == b[:i] else 0 for i in range(k)])

def reconstruction(k, kmers):
    m = {kmers[j]: [kmers[i] for i in range(len(kmers)) if overlapping(
        k, kmers[i], kmers[j]) == k - 1] for j in range(len(kmers))}
    for key, value in m.items():
        print(key, value)
    first = min([(key, value) for key, value in m.items()], key=lambda item: len(item[1]))[0]
    print(first)
    result = [first]
    del m[first]
    new_m = {}
    for key, value in m.items():
        for v in value:
            if v not in new_m.keys():
                new_m[v] = []
            new_m[v].append(key)
    m = new_m
    print("")
    for key, value in m.items():
        print(key, value)
    prev = first
    while m.keys():
        m, next = get_next(m, prev)
        result.append(next)
        prev = next
    result = "".join([result[0]] + [item[-1:] for item in result[1:]])
    return result



# k = 4

# kmers = [
#     "CTTA",
#     "ACCA",
#     "TACC",
#     "GGCT",
#     "GCTT",
#     "TTAC",
# ]

k = 4

kmers = """
TTGA
GATG
ATGT
TGAG
TGTT
GTGA
GTTG
GAGA
AGAT
"""

result = reconstruction(k, [item.strip() for item in kmers.split("\n") if item.strip()])
# print(result == r)
print(result)