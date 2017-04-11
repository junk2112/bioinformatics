
amino_masses = [57,71,87,97,99,101,103,113,114,115,128,129,131,137,147,156,163,186]

def peptides(length, lcp):
    for i in range(0, len(amino_masses)):
        if length - amino_masses[i] in lcp.keys():
            lcp[length] = lcp[length - amino_masses[i]] + (lcp[length] if length in lcp.keys() else 0)
    return lcp

def count(mass):
    lcp = {0: 1}
    for i in range(57, mass+1):
        lcp = peptides(i, lcp)
    return lcp[mass] if mass in lcp.keys() else 0

print(count(1459))