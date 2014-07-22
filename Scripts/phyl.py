#Converts file to phylip relaxed format for raxml


from Bio import AlignIO
import sys

options = sys.argv[1:]
infile = options[0]
outfile = options[1]

records = AlignIO.parse(infile, "fasta")

AlignIO.write(records, outfile, "phylip-relaxed")

