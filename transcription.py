from Bio.Seq import Seq
coding_dna = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")
template_dna = coding_dna.reverse_complement()
print(template_dna)

# Now let’s transcribe the coding strand into the corresponding mRNA, using the Seq object’s built-in transcribe method:
m_rna = coding_dna.transcribe()
print(m_rna)

# If you do want to do a true biological transcription starting with the template strand, then this becomes a two-step process:
print(template_dna.reverse_complement().transcribe())

# The Seq object also includes a back-transcription method for going from the mRNA to the coding strand of the DNA. Again, this is a simple U -> T substitution:
print(m_rna.back_transcribe())