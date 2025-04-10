def count_rna_translation(protein):
    codon_table = {
        'F':2, 'L':6, 'S':6, 'Y':2, 'C':2, 'W':1,
        'P':4, 'H':2, 'Q':2, 'R':6, 'I':3, 'M':1,
        'T':4, 'N':2, 'K':2, 'V':4, 'A':4, 'D':2,
        'E':2, 'G':4
    }
    MOD = 1000000
    total = 1

    for aa in protein:
        total = (total * codon_table[aa]) % MOD

    total = (total * 3) % MOD
    return total

with open("protein.txt", "r") as file:
    protein_string = file.read().strip()

result = count_rna_translation(protein_string)

with open("output.txt", "w") as file:
    file.write(str(result) + "\n")
