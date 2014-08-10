from Bio import SeqIO, AlignIO
from Bio.Align import MultipleSeqAlignment
from Bio.Alphabet import IUPAC
import sys
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-i", "--inputfile", 
    action="store", dest="inputfile", help="Input file name")
parser.add_option("-o", "--outputfile",
    action="store", dest="outputfile", help="Output file name")
parser.add_option("-l", "--left_cutoff_max",
    action="store", dest="leftmax", help="Left cutoff maximum")
parser.add_option("-r", "--right_cutoff_max",
    action="store", dest="rightmax", help="Right cutoff maximum")

options, args = parser.parse_args()

infile = options.inputfile
outfile = options.outputfile
left_cutoff_max = int(options.leftmax)
right_cutoff_max = int(options.rightmax)

#Globals
_left_terminal_gap_cutoff = 0
_right_terminal_gap_cutoff = 0

def main():
    alignment = AlignIO.read(infile, 'fasta')
    new_align_list = list()
    removed_list = list()
    for record in alignment:
        flag=True
        flag = leftGapOperations(record)
        if flag != True:
            removed_list.append(record.id)
            #print "Removing %s from alignment due to \nexceeding left gap cutoff" % record.id
        else:
            flag = rightGapOperations(record)
            if flag == False:
                removed_list.append(record.id)
                #print "Removing %s from alignment due to \nexceeding right gap cutoff" % record.id
            else:
                new_align_list.append(record)
    
    removed_outfile_name = outfile.split('.')[0] + ".rem"
    removed_handle = open(removed_outfile_name, 'w')
    removed_handle.write('\n'.join(removed_list))
    removed_handle.close()
    new_align = MultipleSeqAlignment(new_align_list, alphabet=IUPAC.extended_dna)
    #print new_align
    #print getLeftTerminalCutoff()
    #print getRightTerminalCutoff()
    trim_align = trimSelection(new_align)
    print "Trimmed %i left and %i right" % (getLeftTerminalCutoff(),getRightTerminalCutoff()*-1)
    print "Removed %i sequences due to exceeding gap limits" % (len(removed_list))
    AlignIO.write(trim_align, outfile, 'fasta')
        
def trimSelection(nalign):
    left = getLeftTerminalCutoff()
    right = getRightTerminalCutoff()
    if right == 0:
        trimmed_alignment = nalign[:,left:]
    else:
        trimmed_alignment = nalign[:,left:right]
    return trimmed_alignment 

def leftGapOperations(record):
    left_len_before_gap = len(record.seq)
    left_trim_seq = str(record.seq).lstrip('-')
    left_len_after_gap = len(left_trim_seq)
    left_gap_length = left_len_before_gap - left_len_after_gap
    #print "left_gap_length=%i\tleft_cutoff_max=%i" % (left_gap_length, left_cutoff_max)
    if left_gap_length > left_cutoff_max:
        #Exceeds cutoff
        return False 
    if getLeftTerminalCutoff() < left_gap_length:
        print "Changing left cutoff from %i to %i due to  %s" % (getLeftTerminalCutoff(), left_gap_length, record.id)
        setLeftTerminalCutoff(left_gap_length)
    return True

def rightGapOperations(record):
    right_len_before_gap = len(record.seq)
    right_trim_seq = str(record.seq).rstrip('-')
    right_len_after_gap = len(right_trim_seq)
    right_gap_length = right_len_before_gap - right_len_after_gap
    if right_gap_length > right_cutoff_max:
        #Exceeds cutoff
        return False 
    if getRightTerminalCutoff() * -1 < right_gap_length:
        print "Changing right cutoff from %i to %i due to %s" % (getRightTerminalCutoff() * -1, right_gap_length, record.id)
        setRightTerminalCutoff(right_gap_length)
    return True

def setLeftTerminalCutoff(newVal):
    global _left_terminal_gap_cutoff
    _left_terminal_gap_cutoff = newVal

def getLeftTerminalCutoff():
    global _left_terminal_gap_cutoff
    return _left_terminal_gap_cutoff

def setRightTerminalCutoff(newVal):
    global _right_terminal_gap_cutoff
    _right_terminal_gap_cutoff = newVal * -1

def getRightTerminalCutoff():
    global _right_terminal_gap_cutoff
    return _right_terminal_gap_cutoff

if __name__ == '__main__':
    main()
