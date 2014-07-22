from Bio import SeqIO
import sys

options = sys.argv[1:]
infile = options[0]
dictfile = options[1]
outfile = options[2]

records = SeqIO.parse(infile, "fasta")

homodict = dict(eval(open(dictfile, "r").read()))
homolist = list()
for rec in records:
    if rec.id in homodict:
        homolist.append(rec)

SeqIO.write(homolist, outfile, "fasta")
