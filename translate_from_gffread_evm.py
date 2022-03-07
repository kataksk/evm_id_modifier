import sys
import os
import subprocess
from Bio import SeqIO

fasta_in = sys.argv[1]
species_in = sys.argv[2]

tmp_dir_name = 'tmp_' + str(species_in)
os.mkdir(tmp_dir_name)

output = ''

for record in SeqIO.parse(fasta_in, 'fasta'):
    desc_part = record.description
    seq = record.seq
    id_part = record.id
    
    single_fa = '>' + str(desc_part) + '\n' + str(seq) + '\n'
    id_part = id_part.split('.')
    id_part = '_'.join(id_part)
    tmp_file_name = str(id_part) + '.fa'
    f = open(tmp_dir_name + '/' + tmp_file_name, 'w', encoding='UTF-8')
    f.write(single_fa)
    f.close()

    desc_part = desc_part.split()
    f = tmp_dir_name + '/' + tmp_file_name
    result = subprocess.run(['seqkit', 'translate', '--allow-unknown-codon', '--frame', desc_part[1][4:5], f])
    output += str(result)