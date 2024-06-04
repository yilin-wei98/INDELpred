# INDELpred

## Environment Setup

### Prerequisites

Ensure you have the following installed on your system:
- Python 3.9 or higher
- conda

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yilin-wei98/INDELpred/
    cd INDELpred
    ```

2. **Create a virtual environment:**

    ```bash
    conda create -n INDELpred python=3.9
    ```

3. **Activate the virtual environment:**

    ```bash
    conda activate INDELpred
    ```

4. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

## Download ANNOVAR and Related Databases

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

## Running INDELpred.sh

To run `INDELpred.sh`, execute the following command with your input VCF file, output prefix, and reference version (either hg19 or hg38):

```bash
sh INDELpred.sh input_vcf output_prefix ref_version[hg19/hg38]
```

### Example Usage

Here's an example command using a sample VCF file, `example.vcf`, with the output prefix `example` and using the reference version hg19:

```bash
sh INDELpred.sh example.vcf example hg19
```

This restructured README provides a logical flow from environment setup, through downloading necessary tools and databases, to running the main script.
