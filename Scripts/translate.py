# covnerts homologous nucleotide sequences into protein sequences for the purpose of mutation analysis, 
# Then globally alligns newly converted protein sequences for snp analysis

import sys
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio import SeqIO, AlignIO
from Bio.Emboss.Applications import NeedleCommandline
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-i", "--input_file", action = "store", \
    type = "string", dest = "infile")
option, args = parser.parse_args()

infile = parser.values.infile
prot_outfile = "translated_"+infile.rstrip(".fas")+".faa"

records = SeqIO.parse(infile, "fasta")
protlist = list()

for rec in records:
    tempseq = rec.seq
    minlength = 0
    for x in range(3):
        tryseq = tempseq[x:].translate(to_stop=True)
        seqlength = len(tryseq)
        if (seqlength >= minlength):
            bestseq = tryseq
            minlength = seqlength
        else:
            continue
    temprec = rec
    temprec.seq = bestseq
    protlist.append(temprec)
SeqIO.write(protlist, prot_outfile, "fasta")


