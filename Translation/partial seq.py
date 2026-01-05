from Bio.Seq import Seq
seq = Seq({117512683: "TTGAAAACCTGAATGTGAGAGTCAGTCAAGGATAGT"}, length = 159345973)
print(seq)

print(len(seq[1000:1020]))
print(seq[117512690:117512700])
print(len((seq[117512670:117512690])))
print(len(seq[117512700:]))

# Partially defined sequences can also be created by appending sequences, if at least one of the sequences is partially or fully undefined:
seq = Seq("ACGT")
undefined_seq = Seq(None, length = 10)
seq+undefined_seq
print(seq+undefined_seq)