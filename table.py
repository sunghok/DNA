

def read_seq(inputfile):
    """Reads and returns the input sequence with special characters removed."""
    with open(inputfile, "r") as f:
        seq = f.read()
    seq = seq.replace("\n", "")
    seq = seq.replace("\r", "")
    return seq

# inputfile = "dna.txt"                  
# with open(inputfile, "r") as f:
#     seq = f.read()


# inputfile = "dna.txt"                  
# f = open(inputfile, "r")
# seq = f.read()

# seq.replace("\n", "")                
# seq = seq.replace("\n", "")
# seq = seq.replace("\r", "")


def translate(seq):
    """this fucntion translates DNA triplet sequence into Amino Acid"""
    table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }

    

    protein = ""
    if len(seq)% 3 == 0:
        for i in range(0,len(seq),3):         
            codon = seq[i : i+3]               ##RNA codon table. 0,3 => 3,6, 6,9
            protein += table[codon]

    return protein




prt = read_seq("protein.txt")
dna = read_seq("dna.txt")


print(translate(dna[20:935])==prt)




