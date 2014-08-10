import sys
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-i", "--InputTaxaFile",
    action="store", dest="Taxa_File", help="File containing taxa seen in the tree (Long names)")
parser.add_option("-o", "--OutputTaxaFile",
    action="store", dest="Output_Taxa_File", help="File to save new smaller publication taxa")

options, args = parser.parse_args()

infile = options.Taxa_File
outfile = options.Output_Taxa_File

taxafile = open(infile, "r").readlines()
linelist = list()
strainlist1 = list()
strainlist2 = list()
for line in taxafile:
    x=1
    y=1

    oldline = line
    tabcount = line.count("\t")
    line = line.lstrip("\t")
    #print temp[:1]
    if line[:1] == "A" or line[:1].isdigit():
        linesplit = line.split(" ")
        if linesplit[0][0] == "A":
            termlist = linesplit[0].split("|")
            if len(termlist) < 4:
                linelist.append(oldline)
                continue
            strain = termlist[0]
            newstrain = strain
            while newstrain in strainlist1:
                x+=1
                newstrain = strain + "_" + str(x)
            strain = newstrain
            strainlist1.append(strain)
            date = termlist[-1]
            if termlist[3][:3] == "EPI":
                subtype = "H7N9"
            else:
                subtype = termlist[2]
            print "strain = %s\tsubtype = %s\tdate = %s" % (strain, subtype, date)   
            newline = "%s(%s)\n" % (strain, subtype)
        else:
            #print linesplit
            termlist = linesplit[1].split("|")
            if len(termlist) < 4:
                linelist.append(oldline)
                continue
            strain = termlist[0]
            newstrain = strain
            while newstrain in strainlist2:
                y+=1
                newstrain = strain + "_" + str(y)
            strain = newstrain
            strainlist2.append(strain)
            date = termlist[-1][:-1]
            if termlist[3][:3] == "EPI":
                subtype = "H7N9"
            else:
                subtype = termlist[2]
            print "strain = %s\tsubtype = %s\tdate = %s" % (strain, subtype, date)   
            newline = "\t\t%s %s(%s),\n" % (linesplit[0], strain, subtype)
            
        linelist.append(newline)
    else:
        linelist.append(oldline)
        
newstring = ''
for line in linelist:
    newstring = newstring + line
outhandle = open(outfile, "w")        
outhandle.write(newstring)
outhandle.close()
#for treefile in tree:
#    terminallist = treefile.get_terminals()
#for term in terminallist:
#    terminal_name = term.name
#    #terminal_name = terminal_name.replace("'", "")
#    #terminal_name = terminal_name.replace(".", "_")
#    termlist = terminal_name.split("|")
#    strain = termlist[0]
#    date = termlist[-1]
#    if "EPI" in terminal_name:
#        subtype = "H7N9"
#    else:
#        subtype = termlist[2]
#    print "strain = %s\tsubtype = %s\tdate = %s" % (strain, subtype, date)   
##Phylo.write(tree, outfile, "nexus")
