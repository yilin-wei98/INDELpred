#!/bin/bash

if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <input_vcf> <output_prefix> <ref_version>"
    exit 1
fi

INPUT_VCF=$1
OUTPUT_PREFIX=$2
REF_VER=$3

echo "Step 1: Running table_annovar.pl..."

table_annovar.pl $INPUT_VCF $annovar/humandb/ -buildver $REF_VER -out $OUTPUT_PREFIX -remove -protocol refGene,gnomad211_genome -operation g,f -nastring . -vcfinput

echo "Step 2: Running clinical_processing_and_prediction.py..."

python clinical_processing_and_prediction.py -i ${OUTPUT_PREFIX}.${REF_VER}_multianno.txt -o ${OUTPUT_PREFIX}.tsv

echo "All steps completed!"

