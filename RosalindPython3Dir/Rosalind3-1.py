#!/usr/bin/python
import re
import subprocess


subprocess.call("./textReader")

outputObj = open(r"../Output.txt", "r")
myLocation = outputObj.read()
myLocationObj = open(myLocation.strip(), "r")
text = myLocationObj.read()



numsReg = re.compile(r'(\d+) (\d+) (\d+) (\d+)')
nums = numsReg.search(text)
if nums:
    a = int(nums.group(1))
    b = int(nums.group(2))+1
    c = int(nums.group(3))
    d = int(nums.group(4))+1

    snipText = text[a:b] + " " + text[c:d]
    print(snipText)

else:
    print("Error")