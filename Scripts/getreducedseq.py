import sys
from Bio.Seq import Seq
from Bio import SeqIO, AlignIO

options = sys.argv[1:]
infile = options[0]
idfile = options[1]
outfile = options[2]

records = SeqIO.parse(infile, "fasta")
idlist = open(idfile, "r").read().split("\n")[:-1]

idappendlist = list()

for rec in records:
    if rec.id in idlist:
        idappendlist.append(rec)
    else:
        print "Couldn't find %s" % rec.id
SeqIO.write(idappendlist, outfile, "fasta")
