"""
take a directory of files <root_dir> and link them into directories of size
<chunk_size>

the link commands are printed to the standard output, and should be redirected
to a file for review before being executed

to make sure pairs end up in the same directory, use remove_n_chars to indicate
how many characters to remove from the front of the file name to put them
in the same group

for example: if you wanted 'asdf.R1.fq', 'asdf.R2.fq' in the same directory,
remove 4 characters, to get the group 'asdf.R'
"""

import sys, pathlib, collections

chunk_size = int(sys.argv[1]) # 1020
root_dir = sys.argv[2] #'/data/inputs/uploads/phe/210203_mask_derive_TB'
remove_n_chars = 0

fastq_paths = pathlib.Path(root_dir).glob('*.bam') # '*.bam'
sample_pair_map = collections.defaultdict(list)

# group samples
for fastq_path in fastq_paths:
    try:
        sample_pair_map[str(fastq_path)].append(fastq_path)
    except Exception as e:
        print(f"?? {str(e)}: {fastq_path}")

# output group link commands
for i, sample_pair in enumerate(sample_pair_map.values()):
    assert(len(sample_pair) == 1)
    for fastq_path in sample_pair:
        print(f"mv {root_dir}/{fastq_path.name} {root_dir}{1 + (i // chunk_size)}/{fastq_path.name}")


        
        
