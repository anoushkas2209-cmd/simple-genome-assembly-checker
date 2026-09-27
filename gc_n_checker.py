from Bio import SeqIO

def gc_content(contigs):
    all_bases = "".join(str(contig.seq).upper() for contig in contigs)
    gc = all_bases.count("G") + all_bases.count("C")
    valid = sum(all_bases.count(b) for b in "ACGT")
    if valid == 0:
        return 0.0
    return gc / valid * 100


def n_count(contigs):
    all_bases = "".join(str(contig.seq).upper() for contig in contigs)
    return all_bases.count("N")

    
   
