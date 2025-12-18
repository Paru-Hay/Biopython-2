from Bio.Seq import Seq
my_seq = Seq("AGTACACTGGT")
len(my_seq)
print(len(my_seq))

my_seq.count("G")
print(my_seq.count("G"))

100*(my_seq.count("G") + my_seq.count("C")) / len(my_seq)
print(100*(my_seq.count("G") + my_seq.count("C")) / len(my_seq))