from Bio.Seq import Seq
m_rna = Seq("AUGUACACUGGU")
print(m_rna.translate())

# Translating directly from the DNA coding strand
coding_dna = Seq("ATGTACACTGGT")
print(coding_dna.translate())

