import re


def to_rna(dna_strand):
    translation = {'G': 'C',
                   'C': 'G',
                   'T': 'A',
                   'A': 'U'
                   }

    if re.search('^[GCTA]+$', dna_strand):
        return dna_strand.translate(str.maketrans(translation))
    else:
        raise ValueError("DNA strand invalid, empty or incorrect nucleotide")
