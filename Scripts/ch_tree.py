import sys
from Bio import Phylo

options = sys.argv[1:]
infile = options[0]
dictfile = options[1]
outfile = options[2]

dictfilehandle = open(dictfile, "r")
dstring = dictfilehandle.read()
namedict = dict(eval(dstring))
newdict = dict()

for key, val in namedict.iteritems():
    newdict[val] = key

tree = Phylo.read(infile, "newick")
terminallist = tree.get_terminals()
for term in terminallist:
    term.name = newdict[term.name.strip("'")]
    
Phylo.write(tree, outfile, "nexus")
