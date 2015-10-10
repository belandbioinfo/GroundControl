"""
Author: Kevin Beland
Purpose: Parses Youtube Playlist HTML Page for individual videos in playlist and 
		generates VLC command to play all videos. This can then be saved as a VLC playlist
"""

import sys
import platform
import urllib2
from optparse import OptionParser
from lxml import etree as ET

# Option Parsing boilerplate
parser = OptionParser()
parser.add_option("-f", "--file",
	action="store", type="string", dest="filename",
    help="Write VLC Command to play all parsed videos to file", metavar="FILE")
parser.add_option("-u", "--url",
	action="store", type="string", dest="url",
    help="Youtube Playlist URL to parse for individual Youtube Video Links")

(options, args) = parser.parse_args()

print options

# Initialize options passed to script
url = options.url
outputfile = options.filename

# Retrieve data from URL option
fh = urllib2.urlopen(url)
data = fh.read()
fh.close()

# Return indexes of <body> and </body> to prevent following error:
# xml.etree.ElementTree.ParseError: not well-formed (invalid token)
bodydata = data.index("<body")
endbody = data.rindex("</body>")
body = data[bodydata:endbody+len("</body>")]

# Get XML object from data variable parsed from Youtube
tree = ET.HTML(body)

# Get all elements with attribute class=pl-video-title with immediate 'a' child elements
# and save into list
urllist = []
anchors = tree.xpath(".//*[@class='pl-video-title']/a")
for e in anchors:
    urllist.append(e.attrib['href'])

# Generate VLC Command String and append parsed URL's
if "Windows" in platform.system():
	command = "call vlc "
else:
	command = "vlc "
	
for urlitem in urllist:
    command+='"https://www.youtube.com'+urlitem+'" '
	
print command

# Output constructed .bat file to invoke VLC with every youtube video as arguments
outfh = open(outputfile,'w')
outfh.write(command)