import sys
from Bio import SeqIO

options = sys.argv[1:]
infile = options[0]
outfile = options[1]

records = SeqIO.parse(infile, "fasta")
iddict = {}
newreclist = list()
for num, rec in enumerate(records):
    idname = "seq"+str(num)
    iddict[idname] = rec.id
    rec.id = "seq%i" % num
    rec.description = ''
    newreclist.append(rec)
headerout = open(outfile+".hname", "w")
headerout.write(str(iddict))
SeqIO.write(newreclist, outfile, "fasta")
