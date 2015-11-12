#!/usr/bin/python

import sys
import getopt
import subprocess
from subprocess import call
import re
import matplotlib.pyplot as bwplt

linesize=2000
linescale=linesize/10

def main(filename):
    prevline = 0;
    max = 0;
    i = 0;

    for i in xrange(len(files)):
        filename = files[i]
        with open(filename, "r") as f:
            for line in f:
                words = line.split()
                curline = int(words[1])
                if max < curline - prevline:
                    max = curline - prevline
                    pos = words[0]
                prevline = curline 
        print (pos, max)

def timevsloop(files, outfile):
    color = 'blue'
    maxlist = [0, 0]

    bwplt.subplot(2,1,1)
    bwplt.xlabel("Loop Number * 2000")
    bwplt.ylabel("Timestamps")
    bwplt.xlim([0, 1])
    bwplt.ylim([0, 1.5])
    
    bwplt.subplot(2,1,2)
    bwplt.xlabel("CPU share")
    bwplt.ylabel("Cumulative Distribution")
    bwplt.xlim([0, 1])
    bwplt.ylim([0, 1])
    for i in xrange(len(files)):
        filename = files[i]
        maxdata = 0;
        with open(filename, "r") as f:
            for line in f:
                pass
            words = line.split()
            maxlist[i] = int(words[2]) 
            print maxlist


    for i in xrange(len(files)):
        filename = files[i]
        with open(filename, "r") as f:
            for line in f:
                words = line.split()
                loop = int(words[0])
                timestamp = int(words[1])
                offtime = int(words[2])
                x = loop/float(linescale)
                y = timestamp/float(maxlist[i])
                z = 1 - offtime/float(loop + 1)
                bwplt.figure(1)
                bwplt.scatter(x, y, c=color, label=color, alpha=0.5)
                bwplt.figure(2)
                bwplt.scatter(z, x, c=color, label=color, alpha=0.5)
            print z
    bwplt.grid(True)
    bwplt.figure(1)
    bwplt.savefig(looppng)
    bwplt.figure(2)
    bwplt.savefig(sharepng)
    bwplt.show()
    

if __name__ == "__main__":
    tcpfile = sys.argv[1]
    udpfile = sys.argv[2]
    outfile = sys.argv[3]
    files = [tcpfile, udpfile]
    bwplot(files, outfile)
