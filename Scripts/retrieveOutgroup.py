""" This script accepts a sequence list file with -s and sequences in fasta format with -i, then only returns those """
""" Sequences in the ID list file """

from Bio import SeqIO
from optparse import OptionParser
import sys

def main():

    parser = OptionParser()
    parser.add_option("-i", "--inputfile",
        action="store", dest="inputfile", help="Input file name")
    parser.add_option("-o", "--outputfile",
        action="store", dest="outputfile", help="Output file name")
    parser.add_option("-s", "--seqIDfile",
        action="store", dest="seqfile", help="File containing all the sequence ID's for which you want sequences")

    options, args = parser.parse_args()

    infile = options.inputfile
    seqfile = options.seqfile
    outfile = options.outputfile

    records = SeqIO.to_dict(SeqIO.parse(infile, "fasta"))
    seqlist = open(seqfile, "r").read().split("\n")[:-1]
    outlist = list()

    for seqid in seqlist:
        if seqid in records:
            outlist.append(records[seqid])
        else:
            print "%s not in sequence file" % (seqid)

    SeqIO.write(outlist, outfile, "fasta")

if __name__ == "__main__":
    main()
