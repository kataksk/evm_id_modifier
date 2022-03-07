FATSA=$1
SPECIES=$2
GFF=$3
NEW_FASTA_FILE_NAME=$4
NEW_GFF_FILE_NAME=$5

python translate_from_gffread_evm.py $FATSA $SPECIES > $FATSA.aa
python comp_judge_aa.py $FATSA.aa > $FATSA.aa.mod
python comp_judge_gff.py $FATSA.aa.mod $GFF > $GFF.mod

rm -rf tmp_$FATSA $FATSA.aa

mv $FATSA.aa.mod $NEW_FASTA_FILE_NAME
mv $GFF.mod $NEW_GFF_FILE_NAME
