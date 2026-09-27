from Bio import SeqIO

from gc_n_checker import gc_content, n_count
from n50_checker import calculate_length_stats

fasta_trial = "trial.fasta"


contigs = list(SeqIO.parse(fasta_trial, "fasta"))

print(f"--- Genome Quality Results for: {fasta_trial} ---")
print(f"Total Contigs: {len(contigs)}")


print(f"Overall GC Content: {gc_content(contigs):.2f}%")
print(f"Total 'N' Count: {n_count(contigs)}")


total_len, total_pieces, n50, l50 = calculate_length_stats(contigs)
print(f"Total Assembly Length: {total_len} bases")
print(f"N50 Score: {n50}")
print(f"L50 Score: {l50}")

