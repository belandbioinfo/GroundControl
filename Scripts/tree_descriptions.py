import sys
from Bio import Phylo

options = sys.argv[1:]
infile = options[0]
outfile = options[1]

tree = Phylo.read(infile, "nexus")
terminallist = tree.get_terminals()
for term in terminallist:
    #term.name = newdict[term.name.strip("'")]
    print term.description
    print term
#Phylo.write(tree, outfile, "nexus")
