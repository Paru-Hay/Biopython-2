from Bio.Seq import Seq
my_seq = Seq("AGTACACTGGT")
print(my_seq.complement())
print(my_seq.reverse_complement())

# An easy way to just reverse a Seq object (or a Python string) is slice it with -1 step:
print(my_seq[::-1])

