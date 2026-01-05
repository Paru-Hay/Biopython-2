# 1. Seq objects are immutable in biopython which ensures not changing the sequence data.
from Bio.Seq import Seq
my_seq = ("GCCATTGTAATGGGCCGCTGAAAGGGTGCCCGA")
# my_seq[5] = "G"
# print(my_seq)

# 2. The code can be converted into a mutable sequence and then we can do anything we want.
# from Bio.Seq import MutableSeq
# mutable_seq = MutableSeq(my_seq)
# print(mutable_seq)

# 3. To create MutableSeq object directly from a string.
# from Bio.Seq import MutableSeq
# mutable_seq = MutableSeq(my_seq)

# print(mutable_seq)

# mutable_seq[5] = "G"
# print(mutable_seq)

# print(mutable_seq.remove("T"))

# mutable_seq.reverse()
# print(mutable_seq)

# To get back to a read-only Seq object
new_seq = Seq(my_seq)
new_seq = Seq(my_seq)
print(new_seq)
