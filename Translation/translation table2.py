from Bio.Data import CodonTable
# standard_table = CodonTable.unambiguous_dna_by_id[1]
# print("Standard Table Stop Codons:", standard_table)

mito_table = CodonTable.unambiguous_dna_by_id[2]
# print("Vertebrate Mitochondrial Table Stop Codons:", mito_table)

print(mito_table.stop_codons)
print(mito_table.start_codons)
print(mito_table.forward_table["ACG"])