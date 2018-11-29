import time

#files needed
import QuickFind
import QuickUnion
import improvements
import timingTests

#########################################

# QuickFindTime(txtFile,initial_list)
# QuickUnionTime(txtFile,initial_list)
def Main():
    # fileNameList =["500_10000_"]
    fileNameList =["5000_100000_"]

    timingTests.QFTimeMain(5000,fileNameList)
########################################################################
    # timingTests.QUTimeMain(5000,fileNameList)
    # timingTests.WQUMain(500,fileNameList)
    # timingTests.PathCompressionMain(5000,fileNameList)











    # demoList = improvements.Weighted_QU_List_Initial(5)
    # demoSz = improvements.Weighted_QU_Sz_Initial(demoList)
    #
    ##demo tests:
    #
    # demoList = QuickFind.QuickFindInitial(4)
    # print(demoList)
    # print("------------------")
    # demoList = QuickUnion.union_QU(demoList,0,1)
    # print(demoList)
    # print("------------------")
    # demoList = QuickUnion.union_QU(demoList,3,2)
    # print(demoList)
    # print("------------------")
    # demoList = QuickUnion.union_QU(demoList,2,1)
    # print(demoList)
    # print("------------------")
    # demoList = QuickUnion.union_QU(demoList,1,2)
    # print(demoList)
    # print("------------------")
    # demoList = QuickUnion.union_QU(demoList,3,1)
    # print(demoList)
    # print("------------------")

    # print(demoList)
    # print(demoSz)
    # print("------------------")
    # demoList = improvements.weighted_union_QU(demoList,demoSz,0,1)
    # print(demoList)
    # print(demoSz)
    # print("------------------")
    # demoList = improvements.weighted_union_QU(demoList,demoSz,3,2)
    # print(demoList)
    # print(demoSz)
    # print("------------------")
    # demoList = improvements.weighted_union_QU(demoList,demoSz,0,4)
    # print(demoList)
    # print(demoSz)
    # print("------------------")
    # demoList = improvements.weighted_union_QU(demoList,demoSz,0,3)
    # print(demoList)
    # print(demoSz)
    # print("------------------")
    # demoList = improvements.weighted_union_QU(demoList,demoSz,2,1)
    # print(demoList)
    # print(demoSz)



if __name__ == "__main__":
    Main()
