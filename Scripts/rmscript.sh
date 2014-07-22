#!/bin/bash

find $HOME/public_html/identify/trunk/mutid/uploaded_files/*.faa -type f -exec rm -f {} \;
find $HOME/public_html/identify/trunk/mutid/align1/*.fal -type f -exec rm -f {} \;
find $HOME/public_html/identify/trunk/mutid/align1/*.phy -type f -exec rm -f {} \;
find $HOME/public_html/identify/trunk/mutid/tree/*.txt -type f -exec rm -f {} \;
find $HOME/public_html/identify/trunk/mutid/tree/*.xml -type f -exec rm -f {} \;
find $HOME/public_html/identify/trunk/mutid/tree/tree_image/*.png -type f -exec rm -f {} \;
find $HOME/public_html/identify/trunk/mutid/tree/tree_image/*.png -type f -exec rm -f {} \;
find $HOME/public_html/identify/trunk/mutid/align2/*.fal -type f -exec rm -f {} \;
find $HOME/public_html/identify/trunk/mutid/align2/*.faa -type f -exec rm -f {} \;
find $HOME/public_html/identify/trunk/mutid/output_files/*.ali -type f -exec rm -f {} \;
find $HOME/public_html/identify/trunk/mutid/output_files/*.png -type f -exec rm -f {} \;
find $HOME/public_html/identify/trunk/mutid/socket/*.sock -type f -exec rm -f {} \;
