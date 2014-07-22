from Bio import SeqIO
import sys

options = sys.argv[1:]
infile = options[0]
list_file = options[1]
outfile = options[2]

records = SeqIO.to_dict(SeqIO.parse(infile, "fasta"))
idlist = list(open(list_file, "r").readlines())
outgrouplist = list()
for idname in idlist:
    temp = idname.strip("\n")
    outgrouplist.append(records[temp])

SeqIO.write(outgrouplist, outfile, "fasta")
