""" This file can convert names of sequences, alignments, and trees to smaller temporary names with an accompanying dictionary file for the conversions"""
""" And then converted back again into the desired format"""

from Bio.Seq import Seq
from Bio import SeqIO, AlignIO, Phylo
from optparse import OptionParser
import sys

def main():

    parser = OptionParser()
    parser.add_option("--toSmall", action="store_false", dest="convert", help="Tells the program to convert taxon names to small names")
    parser.add_option("--toLarge", action="store_true", dest="convert", help="Tells the program to use dictionary file input with -d option to convert back to large taxon names")
    parser.add_option("--Table", action="store_true", dest="tablechoice", help="If used the .dict file will output in tabular format instead.")
    parser.add_option("-d", "--dictionaryfile",
        action="store", dest="dictfile", help="Name of dictionary file to use if --toLarge option is specified")
    parser.add_option("-i", "--inputfile",
        action="store", dest="inputfile", help="Input file name")
    parser.add_option("-o", "--outputfile",
        action="store", dest="outputfile", help="Output file name")
    parser.add_option("-s", "--sequence_list", action="callback", 
        callback=seq, nargs=2, type="string", dest="Filetype", help="Convert Sequence names, input and output file types after -s option(e.g. fasta fasta)")
    parser.add_option("-a", "--alignment", action="callback", 
        callback=align, type="string", nargs=2, dest="Filetype", help="Convert Alignment sequence names, input and output file types after -a option(e.g. fasta phylip)")
    parser.add_option("-t", "--tree", action="callback", 
        callback=tree, type="string", nargs=2, dest="Filetype", help="Convert Phylogenetic tree taxon, input and output file types after -t option(e.g. nexus newick)")

    parser.parse_args()

def seq(option, opt, value, parser):
    inputfile = parser.values.inputfile
    outputfile = parser.values.outputfile
    inputtype = str(value[0])
    outputtype = str(value[1])
    records = SeqIO.parse(inputfile, inputtype)
    tablechoice = parser.values.tablechoice

    # convert sequences to small names and save dictionary to .dict file
    if parser.values.convert == False:
        namedict = dict()
        seqlist = list()
        x = 0
        for rec in records:
            x+=1
            newname = 'seq%i' % x
            namedict[newname] = rec.id
            rec.id = newname
            rec.description = ''
            seqlist.append(rec)
        SeqIO.write(seqlist, outputfile, outputtype)

        dictout(namedict, tablechoice, outputfile)

#        if tablechoice == False:
#            dictoutname = outputfile + ".dict"
#            dicthandle = open(dictoutname, "w")
#            dicthandle.write(str(namedict))
#            dicthandle.close()
#        else:
#            tabstring = ''
#            for key, val in namedict.iteritems():
#                tabstring = "%s\t%s\n" % (key, val)
#            dicthandle = open(dictoutname, "w")
#            dicthandle.write(tabstring)
#            dicthandle.close()

    # use dictionary to convert taxon back to large names
    elif parser.values.convert == True:
        namedict = eval(open(parser.values.dictfile, "r").read())
        seqlist = list()
        for rec in records:
            oldname = namedict[rec.id]
            rec.id = oldname
            rec.description = ''
            seqlist.append(rec)
        SeqIO.write(seqlist, outputfile, outputtype)

def align(option, opt, value, parser):
    inputfile = parser.values.inputfile
    outputfile = parser.values.outputfile
    inputtype = str(value[0])
    outputtype = str(value[1])
    records = AlignIO.read(inputfile, inputtype)
    if parser.values.convert == False:
        namedict = dict()
        x = 0
        for rec in records:
            x+=1
            newname = 'seq%i' % x
            namedict[newname] = rec.id
            rec.id = newname
            rec.description = ''
        AlignIO.write(records, outputfile, outputtype)
#        dictoutname = outputfile + ".dict"
#        dicthandle = open(dictoutname, "w")
#        dicthandle.write(str(namedict))
#        dicthandle.close()
    
    # use dictionary to convert taxon back to large names
    elif parser.values.convert == True:
        namedict = eval(open(parser.values.dictfile, "r").read())
        for rec in records:
            oldname = namedict[rec.id]
            rec.id = oldname
            rec.description = ''
        AlignIO.write(records, outputfile, outputtype)

def tree(option, opt, value, parser):
    inputfile = parser.values.inputfile
    outputfile = parser.values.outputfile
    inputtype = str(value[0])
    outputtype = str(value[1])
    tree = Phylo.read(inputfile, inputtype)
    records = tree.get_terminals()

    # convert sequences to small names and save dictionary to .dict file
    if parser.values.convert == False:
        namedict = dict()
        x = 0
        for clade in records:
            x+=1
            newname = 'seq%i' % x
            namedict[newname] = clade.name
            clade.name = newname
        Phylo.write(tree, outputfile, outputtype)
#        dictoutname = outputfile + ".dict"
#        dicthandle = open(dictoutname, "w")
#        dicthandle.write(str(namedict))
#        dicthandle.close()
    
    # use dictionary to convert taxon back to large names
    elif parser.values.convert == True:
        namedict = eval(open(parser.values.dictfile, "r").read())
        for clade in records:
            oldname = namedict[clade.name]
            clade.name = oldname
        Phylo.write(tree, outputfile, outputtype)

def dictout(namedict, tablechoice, outputfile):
    if tablechoice == False:
        dictoutname = outputfile + ".dict"
        dicthandle = open(dictoutname, "w")
        dicthandle.write(str(namedict))
        dicthandle.close()
    else:
        tabstring = ''
        for key, val in namedict.iteritems():
            tabstring = "%s\t%s\n" % (key, val)
        dicthandle = open(dictoutname, "w")
        dicthandle.write(tabstring)
        dicthandle.close()
    


if __name__ == "__main__":
    main()
