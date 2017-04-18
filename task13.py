import sys
import random

def profile_mofits(profile, data, k):
    return [most_probable(item, k, profile) for item in data]

def get_score(motifs):
    columns = [''.join(item) for item in zip(*motifs)]
    max_count = sum([max([c.count(nucleotide) for nucleotide in 'ACGT']) for c in columns])
    return len(motifs[0]) * len(motifs) - max_count

def most_probable(data, k, profile):
    nuc_loc = {nucleotide:index for index,nucleotide in enumerate('ACGT')}
    max_probability = -1

    for i in range(len(data) - k + 1):
        current_probability = 1
        for j, nucleotide in enumerate(data[i:i+k]):
            current_probability *= profile[j][nuc_loc[nucleotide]]

        if current_probability > max_probability:
            max_probability = current_probability
            most_probable = data[i:i+k]

    return most_probable

def get_profile(motifs):
    columns = [''.join(item) for item in zip(*motifs)]
    return [[float(col.count(nuc) + 1) / float(len(col) + 4) for nuc in 'ACGT'] for col in columns]

def greedy_motif_search(data, k, t):
    rand_ints = [random.randint(0,len(data[0])-k) for a in range(t)]
    motifs = [data[i][r:r+k] for i,r in enumerate(rand_ints)]

    best_motifs = motifs
    while True:
        profile = get_profile(motifs)
        mofits = profile_mofits(profile, data, k)
        if get_score(mofits) < get_score(best_motifs):
            best_motifs = mofits
        else:
            return best_motifs

    return best_motifs


data = """
ACTTAATGCACGTATCATCAGCTAACTAAAGATGTTGTCCCTCAACAAACCCCTATCGCCTAGAGGCGTTCAAAAAGAGGGTCCATGATAGCTGACGGCGCGGCGAACTGGGAGTCGGAGTCGCACACAGTTTACGTAACGTTACGCCTGAACTTAATGCACGTAT
CATCAGTACACATCTCTGCATCTAACTAAAGATGTTGTCCCTCAACAAACCCCTATCGCCTAGAGGCGTTCAAAAAGAGGGTCCATGATAGCTGACGGCGCGGCGAACTGGGAGTCGGAGTCGCACACAGTTTACGTAACGTTACGCCTGAACTTAATGCACGTAT
TTCCCTGTCAGACGCAAAATCCGTGAACTGCCTTCTTGAGGAACTAGCGCCTTGATGCCCGCTCGGTCCTCCGTGCAACGGGGACTTAAGGTGCATCCGGAGGGTAACTGGCGTTGGTCGCACGACACATATACTGCAACCGACGATGGTACTTCTACGTGCATAG
GCCTTAACTTCTCTCTGCTGGGGCTGCCGAACTATGTTAACTTTGGTTCCTCCTCCCGGTGATACTAAGGCTGTTTATAAGTGTCGCAGTCGGTCGAGGCTAGCGTATTACCGCCTATCACTTGTACCGCGACGTCCAGGTAGGAGCCTCTTTGCGCGGCGGGTAA
TCGGTGTACAAGAAATTAAAGTACTAGACGTTGCGGGAGCCCGGGTTGCTGGCCGAGGTAAGCTAAACAGCGTCTGTCTCTCTGCATACCAAGGTAGACCTGCTTCGGCGCGAGCTGACCCTGTTATGCACGCAGCTGAACGGGGACACCCGATCCCTATAACACG
GCTACTTTCTCTCTGCATGGATTAATAGTGACTTCAGACACAGCTACAGCCCAACCCTCGAAATGGCCTAGCTAAGATACGTTGCGAGTTCACCACCAGCCGCGGCTTTGTCCACATGTCTACTGACAGAATACATAATGATGTCCTAGTCTCGGTTCATGGGCCT
TTTTAACATTCTTTGGACTTGACGCCCGTGACTACATCGCGAGGCTCAACTGAGATCGTAACTTAGTGCGGTAGCTGTTAAACCGAATGAACACAGATGCGTTCAGGCTGAAACGGCGACCGTGGTTTGATGATTCTATACTGTACTCTGCATATTCCTTGAGGCC
TGGAAAGTCTAAATTGGTCTGGCCTCTACTTCTCAGGGCATTGTCTCGACTGGCTGTAGGGAATACACAATTTTGAATCACGACTGTAACACCCGGCCTGACTTGGGTTAGTTGACTAAGTTGACTCCATCATAGATAAGTTACTACCCTTATCATCAGGTCGACC
CTTCCGTGGAACAAGGGGTCTCGTTCTTGCATCTAAATAGCCTGAGTCTCTCCCGCGCGACTGCGGCATCATAGCTCTCTGGCGGCCGCGTTGGACTATACCCATCTCTGCATGCCCCGACCCGTACCACACCTCTTCCTCCCATGGCAGGAAGTAAGGAGCCTCG
TACACAATTACTTCTCTCATAATATCCTCAGGTTTGGCGCCAAGTCGGGCGTATGCGTGGCTATTATAGTCATCCCAGAAAGCGACCGGGTAGGGGTGCGTAGATAGGTACCTTACCCATACCAGTACGTACTTGGGTTATAGCACCTTGTCCGAGGCGTTTATCA
TCCATTTAAATTCGAAACCATTGGAGCCGTGTGTCAATAACTTTCAGTTGGTATGATCATGCTGGGACAACTAGTATGTCCGCAATGTTACTTAAATGTAATGTCATTTGAACAAGTAGGACTCTCTGCATGGGGGGGCGCAACGTATCCTTTAGTAGGGCTACAA
TACTTCTCTAACCATATGCCACACAGGATCATAAGCCTACAAGCCAAACACGTTCGCGCTGTGTCATTATTTTAGCCGCTTGTAACTAATTCCTTCAGTGGCCAAGCGTGGCGATGTGGCCCGTGGCCTAATAGTGTTGGCGGTTCGCACGAGAGGCGAGCGGCTG
GAGGGTTGAAGGGCACGGGGCAATATATCCGGTGAAGGTGTCCTGGCTTCAGATTCGACAGGATAAGGGCGCTCTGAGAACATACTATCTCCCTACTTTAGTCTGCATCCCGGTCTGTTGCCGCTCCTGAGGATATTGCATACCTTGTCTTATCTCTCTCTAGGAC
TCTCTCTGAGAAGCAAGCCGTGAGTGCGCGTCACTAGACGCATCTGCTACTTGATTCTGCATCTGGCTCAGACTTGAAACACTTCCGAGTACTACGATTATTACGTTAGTACGCATCATCGGAAGTCATATGAACGCCCATGCATCAACTATAATCATTTCTGAGC
CTTTTCACTTATATCGGTGAGGTCGCCCCCATGCCTAAAGACTGTCGCACCGGAGGTTTCTGCGGGGCTACCGGCGTTATATCTCCGCCCTGAAATGCGGTTACTGACCTCTGCATCAGCTCGCGTGAGCTCCTAAAGTTGAATAACCAATTTGCCGCTAATTTAT
TAATAGATCCGTACTTCTCTCTTTCTCTGGTTAAGTACATACCGCTCTGACAGAAGGGCTTTGACATGAGACTGGTGCCAGCTTTAGGTCGACGTAGTTGAGGTCGAACGATGCATTTCCGACGTGTCAGAGTGACTCAAAAACATTAAACACACCTTCCCAATTT
CCGATGCATGACAGGACCTAGATAATCCCTGGTCGATTATTATCTACCTTGTATCGGCGAGGCTTCACCACACTGACCTACTTCAGGCTGCATAATCTCTCGCCCCCAGGGAGCAATGGCCTAGCTTGATAAAGCTCCACCGCCGCAAGTTGTTTCATAGACCAAA
AACGCACTGTGGCGACTTTGCAGTATCTTCGTCTTTCTACTTCTCTCTGGGGATGCGAAAGTGTGGGCGGAGGAGGATTCTGCCGCGCATACCTTTAGTGCTTATAATAAAAACGTTATTGATGCCCTAGAGGCGACACACAAGAACACTAATTCACTATTAACTA
CTCAATATCGACTTGTAAGCGGCACTACCGATACATGTTACTTCCGGCTGCATCGACCGCCCGCGCGATACGCGGCCTGCTGTGGGTTTACCGCTCTACCCATCTTCGATGACCTTACTAGTGTGATATGTTCATAACAGCGGCGCCGCAAACACTGGACCCTATT
TACGCTCCGCTTACGGGGTAGGGATGTTATCCTATTTCATAGTCAATGTAAGGCGCACCCAGCTTCTCTCTGCACAGGAAACCGCGATAGATGCAGCAGGGCGGCAGCTTTTACTATTAGATGACTGTCGGTTACCCATTTACTTGGGTCACAGTACTTGCTTAGC
"""
k, t = 15, 20
data = [item for item in data.split("\n") if item]
best_scores = k * t
best_motifs = None
for i in range(10000):
    motifs = greedy_motif_search(data, k, t)
    score = get_score(motifs)
    if score < best_scores:
        best_scores = score
        best_motifs = motifs
        print(best_scores)
        print("\n".join(best_motifs))
print("END")