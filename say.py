import cowsay
import sys

#Dragon
if len(sys.argv) < 2:
    print("There are no arguments")
else:
    cowsay.dragon("Hello, " + sys.argv[1])

#Trex
if len(sys.argv) == 2:
    cowsay.trex("Hey " + sys.argv[1] + ", are you looking for me?")
