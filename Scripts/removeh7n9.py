#removes H7N9 sequences from FluDB downloads of homologous sequences

from Bio import SeqIO
import sys

options = sys.argv[1:]
infile = options[0]
outfile = options[1]

records = SeqIO.parse(infile, "fasta")
goodlist = list()
for rec in records:
    if len(rec.id.split("|")) >= 3:
        subtype = rec.id.split("|")[2]
        if subtype != "H7N9":
            goodlist.append(rec)
SeqIO.write(goodlist, outfile, "fasta")
