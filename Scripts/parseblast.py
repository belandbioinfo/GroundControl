# Parses blast output for the n most identical sequences specified on the command line

from Bio.Blast import NCBIXML
from optparse import OptionParser
import sys

parser = OptionParser()
parser.add_option("-i", "--input_file", action = "store", \
    type = "string", dest = "infile")
parser.add_option("-o", "--output_file", action = "store", \
    type = "string", dest = "outfile")
parser.add_option("-n", "--number_hits", action = "store", \
    type = "string", dest = "num")
option, args = parser.parse_args()
infile = parser.values.infile
outfile = parser.values.outfile
num = int(parser.values.num)

result_handle = open(infile)
records = NCBIXML.parse(result_handle)

homodict = {}
for br in records:
    x=0
    y=0
    while x < num or y >= len(br.descriptions): 
        temptitle = br.descriptions[y].title
        tempname = temptitle.split(' ')[1]
        info = "score=%f,e=%i,num_ali=%i" % (br.descriptions[y].score,br.descriptions[y].e,br.descriptions[y].num_alignments) 
        if tempname not in homodict:
            homodict[tempname] = info
            x = x + 1
            print len(homodict)
            print tempname
        y = y + 1

print "# of handles retrieved:%i" % (len(homodict))
otf = open(outfile, "w")
otf.write(str(homodict))
result_handle.close()
otf.close()

