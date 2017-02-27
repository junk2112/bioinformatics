import itertools
import time


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print('%r %2.2f sec' % (
            method.__name__, te - ts))
        return result
    return timed


def locate_max(a, key):
    biggest = max(a, key=key)
    return biggest, [index for index, element in enumerate(a)
                     if key(biggest) == key(element)]


def hamming_distance(a, b):
    if len(a) != len(b):
        raise Exception("len(a) != len(b)")
    return len(list(filter(lambda item: item[0] != item[1], zip(a, b))))


def get_kmers(text, k):
    result = {}
    for i in range(0, len(text) - k + 1):
        kmer = text[i:i + k]
        if kmer not in result:
            result[kmer] = 0
        rev_comp = reverse_complement(kmer)
        if rev_comp not in result:
            result[rev_comp] = 0
        result[kmer] += 1
        result[rev_comp] += 1
    return result


def get_possible_kmers(word, hamming_distance, charset='ATCG'):
    result = set()
    for indices in itertools.combinations(range(len(word)), hamming_distance):
        for replacements in itertools.product(charset, repeat=hamming_distance):
            kmers = list(word)
            for index, replacement in zip(indices, replacements):
                kmers[index] = replacement
            result.add("".join(kmers))
    return result

def reverse_complement(seq):
    complement = {"A": "T", "C": "G", "G": "C", "T": "A"}
    bases = list(seq)
    bases = reversed([complement.get(base,base) for base in bases])
    bases = "".join(bases)
    return bases

def approx_pattern_matching(pattern, kmers, d):
    p_len = len(pattern)
    distances = [(hamming_distance(pattern, kmer), kmers[kmer])
                 for kmer in kmers.keys()]
    return sum([item[1] for item in filter(lambda item: item[0] <= d, distances)])

@timeit
def freq_words(text, k, d):
    kmers = get_kmers(text, k)
    possible_patterns = [get_possible_kmers(word, d) for word in kmers.keys()]
    tmp = set()
    for item in possible_patterns:
        tmp = tmp.union(item)
    possible_patterns = list(tmp)
    print(len(possible_patterns))
    frequences = [approx_pattern_matching(
        pattern, kmers, d) for pattern in possible_patterns]
    indexes = locate_max(
        list(zip(possible_patterns, frequences)), lambda item: item[1])[1]
    result = [possible_patterns[i] for i in indexes]
    return result


text = "TGGAAGGTGGAAGGTCTTATGGGGGGGCAATCTGAAGTCATGGAAGGTCTTATGGGCTGAAGTCAGGGGCAATGGGGCAATTGGAAGGCTGAAGTCACTGAAGTCACTGAAGTCATCTTATGGGCTGAAGTCACCGGCTATCTTATGGGCCGGCTACCGGCTACCGGCTATGGAAGGCTGAAGTCACCGGCTATCTTATGGGCCGGCTATCTTATGGGTCTTATGGGGGGGCAATCTGAAGTCATCTTATGGGCCGGCTACTGAAGTCACTGAAGTCATCTTATGGGTCTTATGGGCTGAAGTCACCGGCTATCTTATGGGGGGGCAATGGGGCAATTCTTATGGGTCTTATGGGTCTTATGGGGGGGCAATTCTTATGGGTCTTATGGGCCGGCTACCGGCTATCTTATGGGCTGAAGTCACTGAAGTCATGGAAGGCCGGCTATGGAAGGCCGGCTATCTTATGGGTCTTATGGGTCTTATGGGTCTTATGGGCTGAAGTCATGGAAGGCCGGCTAGGGGCAATTCTTATGGGCCGGCTATGGAAGGTCTTATGGGCTGAAGTCACTGAAGTCATCTTATGGGCCGGCTATCTTATGGGTCTTATGGGGGGGCAATCTGAAGTCACCGGCTACCGGCTAGGGGCAATGGGGCAATGGGGCAATCTGAAGTCATGGAAGGCTGAAGTCACTGAAGTCATCTTATGGGCTGAAGTCACTGAAGTCACCGGCTATGGAAGGGGGGCAATGGGGCAATTCTTATGGGGGGGCAATCCGGCTATCTTATGGGTCTTATGGGTCTTATGGGTCTTATGGGCCGGCTATCTTATGGGTCTTATGGGTGGAAGGTGGAAGGGGGGCAATTGGAAGGTGGAAGG"
k, d = 7, 2

# text = "AAT"
# k, d = 3, 0


print(" ".join(sorted(freq_words(text, k, d))))
