from Bio.Seq import Seq
dna_seq = Seq("acgtACGT")
print(dna_seq.upper())
print(dna_seq.lower())

# These are useful for doing case insensitive matching:
if "GTAC" in dna_seq:
    print("False")

else:
    print("True")
