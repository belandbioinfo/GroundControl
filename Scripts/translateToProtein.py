"""This script translates fasta nucleotide sequence files into their protein counterparts of atleast length CUTOFF specified by -c"""
"""Translated protein length must be > 14 and use atleast 3/5 of the nucleotide residues as codons."""

from Bio.Seq import Seq
from Bio import SeqIO
from Bio.Alphabet import generic_protein
from optparse import OptionParser
import sys

def main():

    parser = OptionParser()
    parser.add_option("-c", "--cutoff", action="store", type="int", nargs=1, dest="cutoff", help="Minimum length allowed for the translated sequences, if a sequence does not reach cutoff in any reading frame then it is skipped and an error message is output to stdout")
    parser.add_option("-i", "--inputfile",
        action="store", dest="inputfile", help="Input file name")
    parser.add_option("-o", "--outputfile",
        action="store", dest="outputfile", help="Output file name")

    options, args = parser.parse_args()

    infile = options.inputfile
    outfile = options.outputfile
    cutoff = options.cutoff

    records = SeqIO.parse(infile, "fasta")
    seqlist = list()
    
    for rec in records:
        x=0
        maxlen=0
        #goodseq=Seq('', generic_protein)
        trylist = ''
        
        while x < 3:
            tranlength = 0
            seqremoved = 0
            metindex = -1
            frameseq = rec.seq.upper()[x:]
            splitseq = [str(frameseq[i:i+3]) for i in range(0, len(frameseq), 3)] 
            reclen = float(len(rec.seq))
            while tranlength < 14 and seqremoved < int(round(reclen * 2/5)):
                try:
                    ind = metindex+1
                    metindex = splitseq[ind:].index("ATG")
                except Exception:
                    print "No more Met"
                    break
                frameseq = frameseq[metindex*3-2:]
                seqremoved += metindex*3-2
                transeq = frameseq.translate(to_stop=True)
                tranlength = len(transeq)

            if tranlength < cutoff:
                trylist += " "+str(tranlength)
                x+=1

            else:

                if tranlength < maxlen:
                    trylist += " "+str(tranlength)
                    x+=1

                else:
                    trylist += " "+str(tranlength)
                    goodseq = transeq
                    maxlen = tranlength
                    x+=1

        if maxlen == 0:
            print "Sequence %s could not be translated with lengths %s" % (rec.id, trylist)
        else:
            print "*** Sequence translated with length %i***" % maxlen
            rec.seq = goodseq
            seqlist.append(rec)
    seqiter = (rec for rec in seqlist)
    SeqIO.write(seqiter, outfile, "fasta")

if __name__ == "__main__":
    main()
