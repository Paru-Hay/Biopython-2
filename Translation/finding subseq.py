from Bio.Seq import Seq, MutableSeq
seq = Seq("ACGTACGT")
print(seq.index("TAC"))
print(seq.index(b"TAC"))
print(seq.index(bytearray(b"ACGT")))
print(seq.index(Seq("CGT")))
print(seq.index(MutableSeq("GTA")))

# print(seq.index("ACTG"))   #Value error will be raised

print(seq.find("ACTG")) #find method returns -1 if not found

print(seq.find("TAC")) #find method returns the index if found
print(seq.rfind("AC")) #rfind method returns the last index if found

for index, sub in seq.search("AC"):  #search method returns all occurrences
    print(f"Found at index: {index}, Subsequence: {sub}")