# from Bio.Seq import Seq
my_seq = ("AGTACACTGGT")
my_seq[4:8]
print(my_seq[4:8])

my_seq[0::3]
my_seq[1::3]
my_seq[2::3]

print(my_seq[0::3])
print(my_seq[1::3])
print(my_seq[2::3])

my_seq[::-1]
print(my_seq[::-1])

# Turning Seq objects to strings
str(my_seq)
print(str(my_seq))

fasta_format_string = ">Name\n %s\n" % my_seq
print(fasta_format_string)