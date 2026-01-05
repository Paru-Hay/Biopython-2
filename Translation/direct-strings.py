from Bio.Seq import Seq

my_string = "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGA"
seq = Seq(my_string)

print("Reverse complement =", seq.reverse_complement())
print("Transcribe =", seq.transcribe())
print("Back transcribe =", seq.back_transcribe())
print("Translate =", seq.translate())