#!/usr/bin/python
import sys
import os
import re
import subprocess

subprocess.call("./textReader")

with open(r"../RosalindPython5Dir/Output.txt", "r") as f:
    f_contents = f.read()
    with open(f_contents.strip(), "r") as g:
        DNAstring = g.read()
        DNAlist = list(DNAstring)
        for i in range(len(DNAlist)):
            if DNAlist[i] == "A":
                DNAlist[i] = "T"
            elif DNAlist[i] == "T":
                DNAlist[i] = "A"
            elif DNAlist[i] == "G":
                DNAlist[i] = "C"
            elif DNAlist[i] == "C":
                DNAlist[i] = "G"
        seperator = ""
        DNAstring = seperator.join(DNAlist)
        print DNAstring[::-1]