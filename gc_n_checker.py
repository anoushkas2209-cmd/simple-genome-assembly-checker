def gc_content(contigs):
    """Calculates overall GC% = (G + C) / (A + C + G + T) * 100. N bases are ignored."""
    all_bases = "".join(str(contig.seq).upper() for contig in contigs)
    gc = all_bases.count("G") + all_bases.count("C")
    valid = sum(all_bases.count(b) for b in "ACGT")
    if valid == 0:
        return 0.0
    return gc / valid * 100


def n_count(contigs):
    """Counts the total number of N (gap / unknown) bases in the assembly."""
    all_bases = "".join(str(contig.seq).upper() for contig in contigs)
    return all_bases.count("N")


def plot_gc_distribution(contigs):
    """Calculates GC% for each individual contig and plots a histogram."""
    gc_percentages = []
    
    for contig in contigs:
        seq = str(contig.seq).upper()
        gc = seq.count("G") + seq.count("C")
        valid = sum(seq.count(b) for b in "ACGT")
        if valid > 0:
            gc_percentages.append((gc / valid) * 100)
            
    plt.figure(figsize=(6, 3))
    plt.hist(gc_percentages, bins=5, color='skyblue', edgecolor='black')
    plt.title("GC Content Distribution Across Contigs")
    plt.xlabel("GC Content (%)")
    plt.ylabel("Number of Contigs")
    plt.grid(axis='y', alpha=0.75)
    plt.tight_layout()
    plt.show()
