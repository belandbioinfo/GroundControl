import sys
from Bio import AlignIO

options = sys.argv[1:]
infile = options[0]
outfile = options[1]

records = AlignIO.read(infile, "fasta")
iddict = {}
for num, rec in enumerate(records):
    quick = "seq"+str(num)
    iddict[quick] = rec.id
    rec.id = "seq%i" % num
headerout = open(outfile+".hname", "w")
headerout.write(str(iddict))
AlignIO.write(records, outfile, "phylip")
