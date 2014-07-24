GroundControl
=============
This repostory is a collection of multiple projects created either
for Bioinformatics workflows, programming tasks or education purposes.

Directories at the root are used to delineate separate projects. They can be fetched
and commited using Sparse Commit. Use the following to checkout only those projects:

```
git init GroundControl
cd GroundControl
git config core.sparsecheckout true
git remote add -f origin https://github.com/belandbioinfo/GroundControl/
```

Then depending on the project you would like to checkout do the following:

For R Projects:  

```
echo "Edu/r/" >> .git/info/sparse-checkout
```

For CPP Projects:

```
echo "Edu/cpp/" >> .git/info/sparse-checkout
```

For Bioinformatics related Python Scripts:

```
echo "Scripts/" >> .git/info/sparse-checkout
```
