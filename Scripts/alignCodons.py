"""This script aligns a previously translated and aligned protein file to a nucleotide"""
"""sequence collection"""

from cogent import LoadSeqs, DNA, PROTEIN
import sys
from optparse import OptionParser


parser = OptionParser()
parser.add_option("-i", "--inputfile", 
    action="store", dest="inputfile", help="Input file name")
parser.add_option("-o", "--outputfile",
    action="store", dest="outputfile", help="Output file name")
parser.add_option("-n", "--nucleotidefile",
    action="store", dest="nucfile", help="File containing nuleotide sequences")

options, args = parser.parse_args()

infile = options.inputfile
outfile = options.outputfile
nucfile = options.nucfile

aligned_aa = LoadSeqs(infile, moltype = PROTEIN, format = 'fasta')
unaligned_dna = LoadSeqs(nucfile, moltype = DNA, aligned = False, format = 'fasta')

aligned_DNA = aligned_aa.replaceSeqs(unaligned_dna)
aligned_DNA.writeToFile(outfile, 'fasta')



