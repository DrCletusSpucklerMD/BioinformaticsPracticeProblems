#!/usr/bin/python
import sys
import os
import re
import subprocess

subprocess.call("./textReader")

with open(r"../RosalindBioinfo1/Output.txt", "r") as f:
    f_contents = f.read()
    with open(f_contents.strip(), "r") as g:
        DNAstring = g.read()

        RNAstring = re.sub("T", "U",DNAstring)
        print RNAstring