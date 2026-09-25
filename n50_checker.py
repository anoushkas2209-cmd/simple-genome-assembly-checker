import sys
from Bio import SeqIO

def calculate_length_stats(records):
    lengths = []
    for rec in records:
        lengths.append(len(rec.seq))
        
    total_length = sum(lengths)
    total_pieces = len(lengths)
    target_mark = total_length / 2.0
    lengths.sort(reverse=True)
    
    running_total = 0
    pieces_used = 0
    n50_score = 0
    l50_score = 0
   
    for piece in lengths:
        running_total = running_total + piece
        pieces_used = pieces_used + 1
        
        if running_total >= target_mark:
            n50_score = piece
            l50_score = pieces_used
            break
            
    
    return total_length, total_pieces, n50_score, l50_score


