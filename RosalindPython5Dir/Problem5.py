#!/usr/bin/python
import subprocess
import re

subprocess.call("./textReader")

with open('Output.txt', "r") as f:
    f_contents = f.read()
    with open(f_contents.strip(),"r") as g:
        text = g.read()
        textList = text.split("\n")
        count = len(g.readlines())
        for i, textValue in enumerate(textList, start=0):
            if i % 2 == 1:
                print(textList[i])

            else:
                continue