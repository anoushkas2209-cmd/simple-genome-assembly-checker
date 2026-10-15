import streamlit as st
from Bio import SeqIO
import matplotlib.pyplot as plt

st.title("Genome Assembly Quality Checker")

uploaded_file = st.file_uploader("trial.fasta", type=["fasta", "fa"])

if uploaded_file is not None:
   
    from io import StringIO
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


    fig, ax = plt.subplots(figsize=(6, 3))
    ax.hist(gc_percentages, bins=5, color='skyblue', edgecolor='black')
    ax.set_title("GC Content Distribution Across Contigs")
    ax.set_xlabel("GC Content (%)")
    ax.set_ylabel("Number of Contigs")
    
    st.pyplot(fig)
