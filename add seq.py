from Bio.Seq import Seq
seq1 = Seq("ACGT")
seq2 = Seq("AACCGG")
print(seq1+seq2)

# Biopython does not check the sequence contents and will not raise an exception if for example you concatenate a protein sequence and a DNA sequence (which is likely a mistake)
protein_seq = Seq("MADSEQENCE")
dna_seq = Seq("ACGT")
print(protein_seq + dna_seq) # will not raise an error

# You may often have many sequences to add together, which can be done with a for loop like this
list_of_seqs = [Seq("ACGT"), Seq("AACCGG"), Seq("TTAA")]
concatenated = Seq("")
for s in list_of_seqs:
    concatenated += s
print(concatenated)

# Like Python strings, Biopython Seq also has a .join method:
contigs = [Seq("ACGT"), Seq("AACCGG"), Seq("TTAA")]
spacer = Seq("N" * 2)
spacer.join(contigs)
print(spacer.join(contigs))
