import sys

aa_mod_fa_in = sys.argv[1]

id_comp_dict = dict()

with open(aa_mod_fa_in, 'r') as f:
    for line in f:
        if line[0] == '>':
            line = line.split()
            id_comp_dict[line[0][1:]] = ' '.join(line[1:])

# print(id_comp_dict)

gff_in = sys.argv[2]

with open(gff_in, 'r') as f:
    for line in f:
        line = line.split()
        if line[2] == 'mRNA':
            line_feature = line[8].split('=')
            line_feature_new = 'ID="' + line_feature[1] + ' ' + id_comp_dict[line_feature[1]] + '"'
            line[8] = line_feature_new
            output = '\t'.join(line)
            print(output)
        elif line[2] == 'CDS':
            line_feature = line[8].split('=')
            line_feature = line_feature[1].split(';')
            line_feature_new = 'ID="' + line_feature[0] + ' ' + id_comp_dict[line_feature[0]] + '";Parent="'  + line_feature[0] + ' ' + id_comp_dict[line_feature[0]] + '"'
            line[8] = line_feature_new
            output = '\t'.join(line)
            print(output)