"""This script parses each taxa for a specific annotation"""

from Bio import SeqIO, Phylo, AlignIO
from Bio.Seq import Seq
from optparse import OptionParser
import sys, re

def main():

    parser = OptionParser()
    parser.add_option("-s", "--Align_File",
        action="store", dest="seqfile", help="File containing all the sequences for which you want to search annotations")
    parser.add_option("-t", "--Table_File",
        action="store", dest="tgfile", help="File containing TreeGraph exported tabled of unique node names and taxa names for appending annotation information")
    parser.add_option("-a", "--Annotation",
        action="store", dest="anno", help="Sequence motif you want to search for")
    parser.add_option("-o", "--Output_File",
        action="store", dest="outputfile", help="Tree file with new annotations")

    options, args = parser.parse_args()

    seqfile = options.seqfile
    annotationlist = [int(anno) - 1 for anno in options.anno.split(" ")]
    outfile = options.outputfile
    tgfile = options.tgfile

    inputdict = dict()
    seqdict = dict()
    table = open(tgfile, "r").read()
    tabsplit = table.split("\n")[:-1]
    for line in tabsplit[1:]:
        parts = line.split("\t")
        newpartstemp = re.sub("'","",parts[1])
        newpartstemp = re.sub("\s","_",newpartstemp)
        newpartstemp = re.sub("\|\d+\|","|H7N9|",newpartstemp)
        seqdict[newpartstemp] = parts[1]
        inputdict[newpartstemp] = parts[0]


    align = AlignIO.read(seqfile, "fasta")
    outstring = "Unique node names\tNode names\tMutation value"
    outlist = list()
    for row, rec in enumerate(align):
        if rec.id in inputdict:
            annolist = list()
            for annotation in annotationlist:
                residue = align[row,annotation]
                residuestring = "(%s%d)" % (residue, annotation+1)
                annolist.append(residuestring)

            outstring+= "\n%s\t%s\t%s" % (inputdict[rec.id],seqdict[rec.id],",".join(annolist))

        else:
                print "%s not found in alignment" % rec.id

    
    outhandle = open(outfile, "w")
    outhandle.write(outstring)
    outhandle.close()

if __name__ == "__main__":
    main()
