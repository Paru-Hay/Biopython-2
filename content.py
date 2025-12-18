from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction
my_seq = Seq("AGTACACTGGT")
gc_fraction(my_seq)
print(gc_fraction(my_seq))