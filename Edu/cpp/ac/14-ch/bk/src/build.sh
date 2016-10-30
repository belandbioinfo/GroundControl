#!/bin/bash

echo "making executable"
make CXXFLAGS="-std=c++98 -Wall -g"
ctags *
