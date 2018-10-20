'''
https://docs.python.org/3.6/library/stdtypes.html?highlight=translate#str.translate
https://docs.python.org/3.6/library/stdtypes.html?highlight=translate#str.maketrans
'''
import re


def to_rna(dna_strand):
    if re.search('^[GCTA]+$', dna_strand):
        return dna_strand.translate(str.maketrans('GCTA', 'CGAU'))
    else:
        raise ValueError("DNA strand invalid, empty or incorrect nucleotide")
