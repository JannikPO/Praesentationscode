import argparse
import math
parser = argparse.ArgumentParser()
parser.add_argument("Hoehe")
args = parser.parse_args()
def Baume(H):
    listTrees =[]
    for index in range (H):
        x_count = index+1
        space_count = " " * (H - index)
        myString =space_count + "x " * x_count
        listTrees.append(myString)
    listTrees.append((H*" "+"x"))
    return listTrees


tree=Baume(int(args.Hoehe))
for item in tree:
    print (item)
