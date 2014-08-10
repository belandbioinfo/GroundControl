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
parser.add_option("-r", "--reference_file", action = "store", \
    type = "string", dest = "ref")
parser.add_option("-o", "--output_file", action = "store", \
    type = "string", dest = "outfile")
parser.add_option("-p", "--alignment_outfile", action = "store", \
    type = "string", dest = "alignment_out")
parser.add_option("-l", "--minimum_length", action = "store", \
    type = "string", dest = "length")
option, args = parser.parse_args()

infile = parser.values.infile
ref_file = parser.values.ref
outfile = parser.values.outfile
minlength = int(parser.values.length)
logfile = "log_"+outfile.rstrip(".fal")+".log"
prot_outfile = "translated_"+infile.rstrip(".fas")+".faa"
refoutfile = "reference_"+prot_outfile
alignment_out =  parser.values.alignment_out

records = SeqIO.parse(infile, "fasta")
protlist = list()

for rec in records:
    temprec = rec
    tempseq = rec.seq
    for x in range(3):
        temprec.seq = tempseq[x:]
        temprec.seq = temprec.seq.translate(to_stop=True)
        seqlength = len(temprec.seq)
        if (seqlength <= minlength):
            print "length = %i" % seqlength
            print "continue"
            continue
        else:
            print "good length = %i" % seqlength
            print "break"
            break
    protlist.append(temprec)
SeqIO.write(protlist, prot_outfile, "fasta")

refrec = SeqIO.read(ref_file, "fasta")
refseq = refrec.seq
temprec = refrec
for x in range(3):
    temprec.seq = refseq[x:]
    temprec.seq = temprec.seq.translate(to_stop=True)
    seqlength = len(temprec.seq)
    if (seqlength <= minlength):
        print "length = %i" % seqlength
        print "continue"
        continue
    else:
        print "good length = %i" % seqlength
        print "break"
        break
newrefrec = temprec
SeqIO.write(newrefrec, refoutfile, "fasta")


x=0
for item in protlist:
    x = x + len(item.seq)

avg = x/len(protlist)
print avg
needle_cline = NeedleCommandline()
needle_cline.asequence=refoutfile
needle_cline.bsequence=prot_outfile
needle_cline.gapopen=10
needle_cline.gapextend=0.5
needle_cline.outfile=alignment_out
print needle_cline
#stdout, stderr = needle_cline()

#logstring = stdout+stderr
#logout = open(logfile, "w")
#logout.write(logstring)
#logout.close()

