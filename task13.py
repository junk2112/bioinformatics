
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

k, d = 4, 2

kmers = """
GAGA|TTGA
TCGT|GATG
CGTG|ATGT
TGGT|TGAG
GTGA|TGTT
GTGG|GTGA
TGAG|GTTG
GGTC|GAGA
GTCG|AGAT
"""
kmers = [item for item in kmers.split("\n") if item.strip()]
kmers1 = [item.split("|")[0] for item in kmers]
kmers2 = [item.split("|")[1] for item in kmers]

# r = "TGCCCCTTTGATCGCGGTTCTCGAATCCATGTAAATACAAAGATCTTATGTCCGCCGCGTATAGCGGTCGTAAAAATCTACGAGTTTCGATAACTCCAGGATCAATGCGGAACTATGCCCTTATAATAAGGCCACAATTAGTGCGCGTATTAGTGCGATTCCCATTTGCTCCTTTTCTCAACGACCAACGTAGGCGGGGGATGAGTATGCACACGCCCACCCGCTACACTCGACCCTCTCGGCTCTTTTTGTACCGGGGGCCTATATCTCCTGCACCGCCACCATCGCGTTCTCTCTTATTTTGCTATTATTATTCTTTCCAGAACATATGACATATCAGTGCAAGCTGAATCGCGAAGCGGCACTTAATACGATTTCTTGCGATGTGTCTTCTCGCGGCAATTGCTAGTGCCTGGTAAGTCACCGTGATCGTGTCTATG"
result1 = reconstruction(k, kmers1 + kmers2)
# result2 = reconstruction(k, kmers2)
print(result1)
print(result2)
# print(result == r)
# print(result)