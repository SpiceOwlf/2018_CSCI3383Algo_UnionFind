import time
import random
#files needed
import QuickFind
import QuickUnion
import improvements
import timingTests

#########################################

# QuickFindTime(txtFile,initial_list)
# QuickUnionTime(txtFile,initial_list)
def Main():
    fileNameList =["10_100_","10_1000_"]
    timingTests.QFTimeMain(10,fileNameList)
########################################################################
    timingTests.QUTimeMain(10,fileNameList)



if __name__ == "__main__":
    Main()
