import sys
from Bio import SeqIO, AlignIO, Phylo
from Bio.Alphabet import generic_protein, generic_dna

options = sys.argv[1:]
incheck = options[0]
infile = options[1]
outfile = options[2]
intype = options[3]
outtype = options[4]

if incheck == 'seq':
    SeqIO.convert(infile, intype, outfile, outtype, generic_dna)
elif incheck == 'align':
    AlignIO.convert(infile, intype, outfile, outtype, generic_dna)
elif incheck == 'tree':
    Phylo.convert(infile, intype, outfile, outtype)
