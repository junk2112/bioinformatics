import sys

def get_score(motifs):
    columns = [''.join(item) for item in zip(*motifs)]
    max_count = sum([max([c.count(nucleotide) for nucleotide in 'ACGT']) for c in columns])
    return len(motifs[0]) * len(motifs) - max_count

def most_probable(dna, k, profile):
    nuc_loc = {nucleotide:index for index,nucleotide in enumerate('ACGT')}
    max_probability = -1

    for i in range(len(dna) - k + 1):
        current_probability = 1
        for j, nucleotide in enumerate(dna[i:i+k]):
            current_probability *= profile[j][nuc_loc[nucleotide]]

        if current_probability > max_probability:
            max_probability = current_probability
            most_probable = dna[i:i+k]

    return most_probable

def get_profile(motifs):
    columns = [''.join(item) for item in zip(*motifs)]
    return [[float(col.count(nuc)) / float(len(col)) for nuc in 'ACGT'] for col in columns]

def greedy_motif_search(data, k, t):
    best_score = t * k

    for i in range(len(data[0]) - k + 1):
        motifs = [data[0][i:i+k]]
        for j in range(1, t):
            current_profile = get_profile(motifs)
            motifs.append(most_probable(data[j], k, current_profile))
        current_score = get_score(motifs)
        if current_score < best_score:
            best_score = current_score
            best_motifs = motifs

    return best_motifs

data = """
CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA
GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG
TAGTACCGAGACCGAAAGAAGTATACAGGCGT
TAGATCAAGTTTCAGGTGCACGTCGGTGAACC
AATCCACCAGCTCCACGTGCAATGTTGGCCTA
"""
k, t = 8, 5
data = [item for item in data.split("\n") if item]
print("\n".join(greedy_motif_search(data, k, t)))

