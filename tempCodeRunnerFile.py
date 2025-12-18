from Bio.Seq import Seq
list_of_seqs = [Seq("ACGT"), Seq("AACCGG"), Seq("TTAA")]
concatenated = Seq("")
for s in list_of_seqs:
    concatenated += s
print(concatenated)
