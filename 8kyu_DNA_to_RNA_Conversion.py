def dna_to_rna(dna):
    b = ""
    for i in (dna):
        if i == "T":
            b += "U"
        else:
            b += i
    print(b)

if __name__ == "__main__":
    dna_to_rna("TTTT")
