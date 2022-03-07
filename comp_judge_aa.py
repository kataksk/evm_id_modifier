import sys
from Bio import SeqIO

fasta_in = sys.argv[1]

for record in SeqIO.parse(fasta_in, 'fasta'):
    seq = record.seq
    id_part = record.id

    if '*' in str(seq) and str(seq)[0] == 'M':
        completeness = ' Complete'
    elif '*' not in str(seq) and str(seq)[0] == 'M':
        completeness = ' Not complete, C-terminal'
    elif '*'  in str(seq) and str(seq)[0] != 'M':
        completeness = ' Not complete, N-terminal'
    elif '*' not in str(seq) and str(seq)[0] != 'M':
        completeness = ' Not complete, N-terminal and C-terminal'
    
    single_fa = '>' + str(id_part) + completeness + '\n' + str(seq)

    print(single_fa)
    # print('@' + completeness)