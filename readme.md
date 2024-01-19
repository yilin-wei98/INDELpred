# ANNOVAR Installation and Database Download Guide

## Step 1: Download ANNOVAR and Related Databases

### ANNOVAR Main Package
First, download the ANNOVAR main package from the official site:
[ANNOVAR Download](https://annovar.openbioinformatics.org/en/latest/user-guide/download/#annovar-main-package)

### Downloading Databases

#### For hg19:
Run the following commands to download the `refGene` and `gnomad211_genome` databases for hg19:

```bash
annotate_variation.pl -buildver hg19 -downdb -webfrom annovar refGene humandb/
annotate_variation.pl -buildver hg19 -downdb -webfrom annovar gnomad211_genome humandb/
```

#### For hg38:
Similarly, to download these databases for hg38, use:

```bash
annotate_variation.pl -buildver hg38 -downdb -webfrom annovar refGene humandb/
annotate_variation.pl -buildver hg38 -downdb -webfrom annovar gnomad211_genome humandb/
```

## Step 2: Running INDELpred.sh

To run `INDELpred.sh`, execute the following command with your input VCF file, output prefix, and reference version (either hg19 or hg38):

```bash
sh INDELpred.sh input_vcf output_prefix ref_version[hg19/hg38]
```