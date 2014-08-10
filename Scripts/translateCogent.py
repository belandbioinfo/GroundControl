"""This program uses cogent to translate DNA sequences to nucleotide, normally"""
"""for the purpose of aligning codons"""

from cogent import LoadSeqs, DNA, PROTEIN
from Bio import SeqIO
import sys
from cogent.core.genetic_code import DEFAULT as standard_code
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-i", "--inputfile", 
    action="store", dest="inputfile", help="Input file name")
parser.add_option("-o", "--outputfile",
    action="store", dest="outputfile", help="Output file name")
#parser.add_option("-m", "--minlength",
#    action="store", dest="minlength", help="Minimum length of protein sequence")

options, args = parser.parse_args()

infile = options.inputfile
outfile = options.outputfile
#minlength = options.minlength


def main():
    new_dna_dict = dict()
    new_aa_dict = dict()
    dna_dict = SeqIO.to_dict(SeqIO.parse(infile, 'fasta'))
    #unaligned_DNA = LoadSeqs(infile, moltype = DNA, aligned = False, format = 'fasta')
    #help(unaligned_DNA)
    #unaligned_DNA = unaligned_DNA.withoutTerminalStopCodons()
#    help(unaligned_DNA)
    for seqname, sequence in dna_dict.iteritems():
        
        #help(seqitem)
        new_aa_seq, new_dna_seq = findBestSeq(sequence)
        new_aa_dict[seqname] = new_aa_seq
        new_dna_dict[seqname] = new_dna_seq
    unaligned_aa = LoadSeqs(data=new_aa_dict, moltype = PROTEIN, aligned = False)
    new_unaligned_dna = LoadSeqs(data=new_dna_dict, moltype = DNA, aligned = False)
#        print seqitem.getName()
#        while seqitem.hasTerminalStop() == True:
#            print "\nold last sic = "+str(seqitem[-6:])
#            seqitem = seqitem.withoutTerminalStopCodon()
#            print "\nnew last sic = "+str(seqitem[-6:])
#    unaligned_DNA.writeToFile(outfile+".dna")
#    unaligned_aa = myTranslate(unaligned_DNA)
    aa_outstring = unaligned_aa.toFasta()
    dna_outstring = new_unaligned_dna.toFasta()
    dna_outfile_temp = outfile.split('.')[0]
    dna_outfile = dna_outfile_temp+'_dna.fasta'
    aa_outfile_handle = open(outfile, "w")
    aa_outfile_handle.write(aa_outstring)
    aa_outfile_handle.close()
    dna_outfile_handle = open(dna_outfile, 'w')
    dna_outfile_handle.write(dna_outstring)
    dna_outfile_handle.close()

def myRemoveTerminal(seqrecord):
    print seqrecord
    tempseqrecord = seqrecord.withoutTerminalStopCodon()
    if tempseqrecord.hasTerminalStop() == True:
        return myTranslate(seqrecord)

def findBestSeq(seqobject):
    dna_seq = str(seqobject.seq)
    my_seq = DNA.makeSequence(dna_seq,seqobject.id)
#    x=0
#    framedict = dict()
#    while x  < 3:
#        temp1 = my_seq[x:]
#        temp2 = temp1..withoutTerminalStopCodon()
#        framedict[x] = temp2.getTranslation()
#        x+=1
    
    all_six = standard_code.sixframes(my_seq)
    seqlist = list()
    for frame in all_six:
        seqreturned = frame.split('*')[0]
        seqlist.append(seqreturned)
    longestseq = ''
    x=0
    while x < 3:
        if len(longestseq) < len(seqlist[x]):
            longestseq = seqlist[x]
            correctdnaseq = my_seq[x:]
        x+=1
    #longest_seq = max(seqlist, key=len)
    return longestseq, correctdnaseq 

if __name__ == '__main__':
    main()
