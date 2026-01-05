from Bio.Data import CodonTable
standard_table = CodonTable.unambiguous_dna_by_name["Standard"]
print("Standard Table Stop Codons:", standard_table.stop_codons)

mito_table = CodonTable.unambiguous_dna_by_name["Vertebrate Mitochondrial"]
print("Vertebrate Mitochondrial Table Stop Codons:", mito_table.stop_codons)