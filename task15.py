
import sys

def hamming_distance(a, b):
    if len(a) != len(b):
        raise Exception("len(a) != len(b)")
    return len(list(filter(lambda item: item[0] != item[1], zip(a, b))))

def distance(pattern, dnas):
    k = len(pattern)
    dist = 0
    for dna in dnas:
        ham_dist = sys.maxint
        for item in [dna[i:i+k] for i in range(0, len(dna)-k+1, 1)]:
            new_dist = hamming_distance(pattern, item)
            if ham_dist > new_dist:
                ham_dist = new_dist
        dist += ham_dist
    return dist

pattern = "TGGCG"
dnas = """
CGTTTCAAATCAATAGCCCCGTTCTGCTCGCACCTAAAACCGAGGTTAGAAATGGGAGAACCAGGCGGGCCTGCCGTTTACTTCTGGTTTTAGGGGCGCGCTAATGC TGACTCTGACGTGTTACGATACGCGAGGGTACTCCCGGGCACTGATACCATCGATGGGCTACGAGTACTCGCGAGATTAATGCAACTTCAAGGCTTGCGCTCACTAA CGCCTGTCGGAAATCGCTGCAAGAATCGGTCGCCCCGGGTGGTCGCCAATGTTTGGTATACCCCGTGTAATCCCGGAACATTATCATGTTATTGATGGCCCCTATCA CCTACTGTAAAAGTGTCGTCTCTAAAGTGAGCGCCCTGTCAATCTTGACCATTCATAGTTCTAAGGACCAGACGTCACCACTCTACTAGTCATCTTGTATTCCTCCG TAAAGGACCCATTCTGACAGGACTCATATTGTGTGGAAACATTACCTTGACGGTCGGAGTTTGGTCATGCGTTTGTGGCCTGCAAATTGGGGCTAATTTACACATAG CGCGCATACGTCGCTCTTTAGGCATGTCTTCATATACGCCGCCGCTATCAAGCCAACTGCGTCAAGTTTTGTTAACAACTCCACGCAAATTTGTTAATCGGTACTGA GAAACGGCACAACAAGCTGCGTTTTCATATTGTCTACATTATGGGGACCCTGTGTTGCGCGCTACAAACCAACCACTCTGTTGATGCATGACATCAGCCCGATTGGG CAATCCTAAGGCCACTTCGTCGTCCACGAGATCTGGAACAGAGCGATGTGGGCACACACTTAATTGTCCGTAGGCTAATTCTGTAGTGGAACGACTCCAGCGTCGCC ACTTGGAACACAAGTTACCTTGCACAGAATTTGGCGCGCGTATGATCCGTGTACCTGCGACGTGCCAAGTCCGACGATTGTCCGACCAAGAAATTCAGAATCGAGTG AAGCAAAGTTCGGACTATATTAAAACCCTAAGATTGCCTACAAAGACGGGGGTAGTTCCCACGCCTCTAGCGTCAGTAGGGACGGTTTCCTAACTTGAGGTCTACGT TAACTATAAGTACCTATTTGGACAACCCCTTACTACACCTCATAAAAGAAATCTCGGGGTAGGTTAAATGCCCCTACCGGCCCATATACATCGTGTTGCCAGACTCA CTAGACGCTATTTCCTGACGTATCTATATGCATAGCCAGAGAGAATCCATGAGAAAACTGACACCTGGCATTGAAGTGTCAAGCCGTCGGTGTCGACAAACGATCTC GTATCATTCGATATCCCTGATTGCCTAACCCAGAAGGCTCACCGCACCGGGAGATGAGAATGCCAGCATCTCATTGGTTTGGGTCTAGGGCTATCTAGGCTTCACTT CTACGACCACTGAAGGAAGCAACCCACCTGTAGGGCCCGTCGTTTCGCCGAATAGTGATTCTTGCAGCCGGGAGCAACGCAAAACTCGAGCGAGAGTCCCCAGCCTT TCTCGTTGGCGAGAAGGTAACATCAGCGCTGTGCGGGAGCTTGTCTACACCCCACTTGAGACACTACAGGTCTCCTCACTGGTACCTTTGTTGGGTTAAAGATATCG CACAGCGAATCATCGTTGATGCGTCCGTTGTCTTGGGTGTTCTTGTGCAGCGGAGCCGTAAGGGGCTTGCGAGCGAAGAGAAATGTAGACATCCGCTGTCTATACTA CATTCATCCGAGTCTGCAGATAAAAAGTTGGGTGCTTGCGGACGGCAGTTCCGTCATGGAAAGAACGAGGCGGCGCTGCTGGTGAGGTCATCGTGGACGTACGTATG ACTGGATAGGATCCACCCCATATATCTGCTCACGAAAGTAAGCAGGACTTTCGCTGACTGGTGGTGCCGACCCATAAGGCCGAGAGCCGAGTTACGTATCAGTCACC TACGCAAAGTTATTAGGCCCGAAGGCTTTTAGTGATGGTAACAACAATCGTAATGTGCATAAATTCGCACGGGCCCCTCAAATGCGTTCTTTGATCTTGTCGCATAT GGGGAAGGTGGATTCACTAGGTGACTCACTTGCGGTTGATACAAGGGTATAACACCTGGTAGCCCAGGTAGGAACATCTTCTGCTTATGCATCGTGACCAAGCTCCG AGCCAAAATCCAGTTCCCGTATGAAGGATCCGTGCGACATTAATAGTAGCAGTTCCGTTACGTAACTTTGTATAACTGTATTCTAAGAGAGTGCGGCCGTCCGACCC CACGTGTTGTGTTGGTGACATGATCAACAGAGATCAGTGGGAAAAAGCTTTCGCAATGGAACCTTGAAATACGTAGCGCTTTGAAAGCGGCTTGCCGCAGTTGCAAT TATGACCGTTGAAGAAATCCGCTGACAGCACGCTTAGCGCCGCTTCAATCGGGGCACTTGCATACCAGAAGAAATTTATGGTACGAGTCGGGGGCGATGCTCACAAT CGCTAAGCTGCATGAGCTCCAATATAATGAGAACCACCATAGCTTAACGTGGACTTTGAAAGAGGGGGGGTCGAACCAAACGGTGGGTACCGGCCTGGCCTACGGCG AATCCCTGGGAGGTGCGCTTCCGGTCCCGGGCGCCCGTGATCATGCTGGCAAATCGTGCTCAATAATTTCCGGGTCCGCATGACGATGGCAGAGTCGCGCCTAGAAT TTCACATTGTTTCTATGCCGCTCGTATTTCACGCCAGCAATCGAACATACAATGCACAAAGGCCATATAAGGCTATGCACGATGCCCATTCGTGGCAACCATAATGC TGGGAGGTCTGAGCGGCGTTCCAGTGCTTTTCTGCGGAGCGTCAATCACTAGTCCCGGGGTGTGTAAACCCGAGGCAACGTTCCTGCGGTGGAGTACCGACCTTGTA TGAACCGCCGACTTTGATGGTGAGCTCTATGCGACTGATTCTCTTCAAGGAGTACGCAACCACGCCGTCTATTGAAATAAAACCAACTAACCCCACTGGTACGATTT CTGGGGAATTAGACCCTAGTTGCTGTGGACTGGTTCCACCCGGCGAACTATCGCTTGTTTTCTCCGCGAAGAGCAAATCTAGTGCAATTTGCGTCCTTCTTACTGTT GTTGGGCCTCCGCCTTTGAAGATATTAAGAGCATGAGGGTTCCTGATTCAATTGCACCGTGCGCTAGTATCCAACAAACTTGGCACTTGCTTTATAAATCATTGGGG ATCGTTTATGTGCGCGGAGGCCTAACATATAATCGAGACCGACACCATTCGGCCTGCGTGTTACCAAGTAAGGTGTCGCCAATGTGTCTCTAGTACGAGTTGGGCAA TTGCTTTCCTCATAATGGGACAGGTTGGCAGGGGTAGGCATTATATCATAACAAAGTTCTCACGCAACGAAGGTATGGCGATCGCTTCAGTCCAGCAATGGGTAGTC AGCCTAATTCTTATTGTCTGACATGTTCCAGATGAGTTCTCGACGTGGCTTCAAACCATGTTACGCCCGAGTCGTGTATCACCACGTTACTAACATCCAAGATGTGT GCAAGAGTAAGTGACAGGTGTAGGGACAAGGTCCTAGTGAAACAGGGCCACGCAACCCATCGTACTAAATACCTCGAAATGGCTACCCGGTTCTTAATCTTTTATAC GTTACGGCCGTGGAGTTAACTGAGTTAAATAAGAGTCGTTTTCAACACGGAGATGGGGGTCGTAACGTGGCTGACTCTCACTCTCATGATAGGTATCTCGTTGCATG CAGGTAGAACAGTAGTTTCACGGATCAATTATATTTCACATTGACGCCGTTAAAGTACTTTGCGGGTGGGCCGCAAATCTATCGTTGAATCGACGCGTTGACTCGGG TTTATAGTGTTAAAGAATCGCGGTGCTGTGCTCGTGGTACGGCCAAGGAGGTTCGTTAGTCAGAATAAGCGAAAAGCGCTGGAGAGGTACACCCGGCGAGAGACTAC CGCCTGGCCCACTCTCCCCCTTTGAGGGGCGCATCTGGAGCCTCTCCCGTGCTAAATTTGCGCTGTGAGCCACATTAATGACTTTTTATAGATGAGATATCACTCGG
""".strip().split()

print(distance(pattern, dnas))