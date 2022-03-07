> USAGE

```
sh evm_id_modifier.sh <fasta file> <species name prefix> <gff3 file> <output fasta file name> <output gff3 file name>
```


> INPIT FILE EXAMPLE

`gff3`

```
scaffold_116    EVM     mRNA    40932   54745   .       +       .       ID=TE.0
scaffold_116    EVM     CDS     40932   40940   .       +       0       ID=TE.0;Parent=TE.0
scaffold_116    EVM     CDS     41033   41224   .       +       0       ID=TE.0;Parent=TE.0
scaffold_116    EVM     CDS     41303   41505   .       +       0       ID=TE.0;Parent=TE.0
scaffold_116    EVM     CDS     41618   41819   .       +       1       ID=TE.0;Parent=TE.0
scaffold_116    EVM     CDS     45528   45661   .       +       0       ID=TE.0;Parent=TE.0
scaffold_116    EVM     CDS     45739   45851   .       +       1       ID=TE.0;Parent=TE.0
...
```

`fasta`

```
>TE.0 CDS=1-1782
ATGAAGCTTTACTGCTTGAGTTGTGATCCAAATAAACCGTGTTATATTTTACGGTTTAAAGAAATAACAT
TGATGTTAGATTGTGGGTTGTCAGCCCATACTGTTCTCAATTTTCTACCATTACCTCTAGTTCCTAGTGC
TCGACTGAACAATTTGCCTGGTTGGATGCCTCGTGATATTGCTGATGCTCAACTTGAAGGGGAATTGAAA
GAATGTTGTGGCAGAGTTTTTGTTGATTCAGCCCCAGAATTTTTCCCACCACAGCCAAAAATAGTTGACT
TCTCAGAAGTAGATGTAATTTTAATATCAAATTACTTATGTATGTTGGCTCTTCCATACATAACAGAAGG
AACAGGATTTTCAGGTGTCGTGTATGCAACAGAACCAACAATGCAGATAGGAAGGTTGTTTCTGGAAGAA
TTAGTTCACCACATTGAGCAAACTCCAAAGGCTACTTTGGCAAGTCACTGGAAAGAACATCTGCATGTGT
TGCCAGCTCCTCTGTCAGACAGTTTGAAGCCAAGAAACTGGAGGCATATTTATGACATGAAAGCTGTGAA
TGACAGTCTTGCGAAGATTCAAATGGTTGGATACAATGAGAAACTGGATATATATGGTGCCTTAGAAGTG
ACTGCAGTAAGCTCAGGGTATTGTTTGGGGTCAAGTAATTGGGTTATAAACTCACATTATGAAAAAATTG
CATATGTCAGTGGTTCTTCGACTCTGACCACACATCCCAAACCAATGGATCAAGGAGCACTAAAGAATGC
AAATGTTCTTATACTCACTGGATTGACCCAAACCCCAACTGCTAATCCTGATTCAATGTTAGGAGAGCTG
TGTATGACAGTAGCTAACACACTTCGATGTGGTGGGAGTGTTCTAATTCCCTGTTATCCATCTGGTGTAG
TGTATGATTTATTTGAATGTTTATCAAGTCATTTGGATGCATCGGGAATGACATCCATTCCTATGTTCTT
CATATCGCCAGTTGCAGACACTTCATTGGCATATTCTAATATTTTAGCAGAATGGCTTTCAACAAACAAG
CAAAACAAAGTGTACTTACCAGAAGAGCCTTTTCCACATGCATTCCTTGTGAGAAATGGCCGTCTCAAAC
ATTTCAAACACATTTATACTGAAGGCTTCAGTACAGATTATAAACAACCATGTGTTGTATTTTGTGGTCA
TCCAAGTCTTCGATTCGGAGATGCAGTTCATTTTGTTGAACTGTGGGGTGGTAATGCTTTAAACACAATA
ATTTTTACAGAACCAGACTTTCCTTATTTGGAAGCTTTAGCACCTTTCCAGCCTTTGGCGATGAAAGCTG
TACATTGTCCTATTGATACAAGCTTGAACTTCACACAAGCCAATAAACTAATCAGAGATTTAAAACCAGG
CACCTTGGTTCTGCCAGAATCCTACAGACAACCTCCTGGTACAGCTCCTCATCGCATGGATCTTATTATA
GAAACAGATAGGCCTCTCTTATCTTTCAAACGGGATGAAGTTCTCACTCTTCCTCTGAAGAGGAAGCAAA
CACAAGTGGATATGAGTCCTGAATTGGCTGAAAATCTAGTGCCAAATGAAGTGAGATCAGGAGTAGCCCT
TGCTACACTGACAGCTGCGATACAAGTGAAAGACAATAAGCACACACTCAAGCCAAATGAAGATACACTC
ATTCAAGTTGAAGATTCATCAACTCATATATTTTGTGAAGGTGATATGCTTTTAAGACAAAAATTAAGAA
CTATATTACTTCAGTGTCTCAACAAATTTTAA
>TE.1 CDS=1-1533
ATGCATAGTCGTCAAGTGGTACGCAAATTATTGCTGTCCCTGAAATGCGAAGCAGCATGTGCTCCAAAAA
CAAGTTCTCATCTTCAGCAACGTTACTTAAGTCACGTATCTCTTGACGAGGCGTACTTACGGACGAAAGA
...
```

