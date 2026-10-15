import streamlit as st
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction  # Added this tool to help build your graph
import matplotlib.pyplot as plt
from io import StringIO


from n50_checker import calculate_length_stats
from gc_n_checker import gc_content, n_count

st.title("Genome Assembly Quality Checker")
 
uploaded_file = st.file_uploader("Upload a .fasta file", type=["fasta", "fa"])

if uploaded_file is not None:
  
    string_data = uploaded_file.getvalue().decode("utf-8")
    contigs = list(SeqIO.parse(StringIO(string_data), "fasta"))

    total_len, total_pieces, n50, l50 = calculate_length_stats(contigs)
    overall_gc = gc_content(contigs)
    total_ns = n_count(contigs)

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="Total Assembly Length", value=f"{total_len:,} bp")
        st.metric(label="Contig Count", value=total_pieces)
        
    with col2:
        st.metric(label="N50 Score", value=f"{n50:,}")
        st.metric(label="L50 Score", value=l50)
        
    with col3:
        st.metric(label="Overall GC Content", value=f"{overall_gc:.2f}%")
        st.metric(label="Total 'N' Count", value=total_ns)

    gc_percentages = [gc_fraction(rec.seq) * 100 for rec in contigs]

    
    # Draw the line graph
    fig, ax = plt.subplots(figsize=(6, 3))
    
    # Create a sequence of numbers (1, 2, 3...) for the X-axis based on how many contigs there are
    contig_numbers = range(1, len(gc_percentages) + 1)
    
    # Plot the line graph with markers at each data point
    ax.plot(contig_numbers, gc_percentages, color='dodgerblue', marker='o', linestyle='-')
    
    ax.set_title("GC Content Across Contigs")
    ax.set_xlabel("Contig Number")
    ax.set_ylabel("GC Content (%)")
    
    # Ensure the X-axis only uses whole numbers (you can't have half a contig)
    ax.set_xticks(contig_numbers)
    
    st.pyplot(fig)