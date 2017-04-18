    # GIBBSSAMPLER(Dna, k, t, N)
    #     randomly select k-mers Motifs = (Motif1, …, Motift) in each string
    #         from Dna
    #     BestMotifs ← Motifs
    #     for j ← 1 to N
    #         i ← Random(t)
    #         Profile ← profile matrix constructed from all strings in Motifs
    #                    except for Motifi
    #         Motifi ← Profile-randomly generated k-mer in the i-th sequence
    #         if Score(Motifs) < Score(BestMotifs)
    #             BestMotifs ← Motifs
    #     return BestMotifs

def gibbs_sampler(dna, k, t, N):
    pass


k, t, N = 8, 5, 100
dna = """
CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA
GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG
TAGTACCGAGACCGAAAGAAGTATACAGGCGT
TAGATCAAGTTTCAGGTGCACGTCGGTGAACC
AATCCACCAGCTCCACGTGCAATGTTGGCCTA
""".strip().split()