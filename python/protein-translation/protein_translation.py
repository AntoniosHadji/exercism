# ("ATG",): "START",
DNA_codons = {
    ("GCT", "GCC", "GCA", "GCG"): "Alanine",
    ("CGT", "CGC", "CGA", "CGG", "AGA", "AGG"): "Arginine",
    ("AAT", "AAC"): "Asparagine",
    ("GAT", "GAC"): "Aspartic acid",
    ("TGT", "TGC"): "Cysteine",
    ("CAA", "CAG"): "Glutamine",
    ("GAA", "GAG"): "Glutamic acid",
    ("GGT", "GGC", "GGA", "GGG"): "Glycine",
    ("CAT", "CAC"): "Histidine",
    ("ATT", "ATC", "ATA"): "Isoleucine",
    ("TTA", "TTG", "CTT", "CTC", "CTA", "CTG"): "Leucine",
    ("AAA", "AAG"): "Lysine",
    ("ATG",): "Methionine",
    ("TTT", "TTC"): "Phenylalanine",
    ("CCT", "CCC", "CCA", "CCG"): "Proline",
    ("TCT", "TCC", "TCA", "TCG", "AGT", "AGC"): "Serine",
    ("ACT", "ACC", "ACA", "ACG"): "Threonine",
    ("TGG",): "Tryptophan",
    ("TAT", "TAC"): "Tyrosine",
    ("GTT", "GTC", "GTA", "GTG"): "Valine",
    ("TAA", "TGA", "TAG"): "STOP",
}

RNA_codons = {
    ("GCU", "GCC", "GCA", "GCG"): "Alanine",
    ("CGU", "CGC", "CGA", "CGG"): "Arginine",
    ("AAU", "AAC"): "Asparagine",
    ("GAU", "GAC"): "Aspartic acid",
    ("UGU", "UGC"): "Cysteine",
    ("CAA", "CAG"): "Glutamine",
    ("GAA", "GAG"): "Glutamic acid",
    ("GGU", "GGC", "GGA", "GGG"): "Glycine",
    ("CAU", "CAC"): "Histidine",
    ("AUU", "AUC", "AUA"): "Isoleucine",
    ("UUA", "UUG", "CUU", "CUC", "CUA", "CUG"): "Leucine",
    ("AAA", "AAG"): "Lysine",
    ("AUG",): "Methionine",
    ("UUU", "UUC"): "Phenylalanine",
    ("CCU", "CCC", "CCA", "CCG"): "Proline",
    ("UCU", "UCC", "UCA", "UCG"): "Serine",
    ("ACU", "ACC", "ACA", "ACG"): "Threonine",
    ("UGG",): "Tryptophan",
    ("UAU", "UAC"): "Tyrosine",
    ("GUU", "GUC", "GUA", "GUG"): "Valine",
    ("UAA", "UGA", "UAG"): "STOP",
}


def _RNA_dict():
    result = {}
    for k in RNA_codons:
        for code in k:
            result[code] = RNA_codons[k]
    return result


RNA = _RNA_dict()


def proteins(strand):
    result = []
    for x in range(0, len(strand), 3):
        codon = strand[x : x + 3]
        if RNA[codon] == "STOP":
            return result
        else:
            result.append(RNA[codon])

    return result
