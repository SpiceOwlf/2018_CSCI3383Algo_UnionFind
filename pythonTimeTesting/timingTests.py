import time
import QuickFind
import QuickUnion
import improvements
#testing times


def QuickFindTime(txtFile,initial_list ):

    f = open(txtFile, "r")
    node_num = f.readline()
    f2 = open(str(txtFile)+"_100QF.txt", "w")
    countIteration = 0
    index = 0
    ticks = time.time()
    for i in f:
        words = i.split()
        p = int(words[0])#p is first node needs to be connnected
        q = int(words[1])#q is second node needs to be connnected
        QuickFind.union_QF(initial_list, p, q)
        ############ record time for every 100 ndoes########
        countIteration = countIteration + 1
        if (countIteration % 100 == 0):
            ticks3 = time.time()
            dif_100 = ticks3 - ticks
            f2.write(str(index)+ "--> time for 100 is: " + str(dif_100) + "\n")
            index =index+1
        ####################################################


    ###timing:
    ticks2 = time.time()
    f.close()
    f2.close()
    timeCost = str(ticks2 - ticks)
    # print(initial_list)
    return("costs: "+ timeCost)#return the time we used


def QFTimeMain(node_num,fileNameList):
    #first fator is node number,
    #second fator is txt nameList
    demo_list = QuickFind.QuickFindInitial(node_num)#the list contains 500 nodes, this is fixed
    f = open("timeResultQF.txt", "w")
    #remember to put the file in the
    #same directory
    for k in fileNameList:
        for i in range(0,5):
            file_name= k+str(i)+".txt"
            timeCost = QuickFindTime(file_name,demo_list)
            demo_list = QuickFind.QuickFindInitial(node_num)#reset the demo list
            f.write("time for " + file_name +" is "+timeCost+"\n")
            print("completed for " + str(file_name))

    f.close()
    return None

##################################################################################
##################################################################################
##################################################################################

def QuickUnionTime(txtFile,initial_list):#basic function to test quick union time

    f = open(txtFile, "r")
    node_num = f.readline()
    # print(node_num)
    f2 = open(str(txtFile)+"_100QU.txt", "w")
    countIteration = 0
    index = 0
    ticks = time.time()
    for i in f:
        words = i.split()
        p = int(words[0])#p is first node needs to be connnected
        q = int(words[1])#q is second node needs to be connnected
        QuickUnion.union_QU(initial_list, p, q)
    ###use Quick Find to conect graph
        ############ record time for every 100 ndoes########
        countIteration = countIteration + 1
        if (countIteration % 100 == 0):
            ticks3 = time.time()
            dif_100 = ticks3 - ticks

            f2.write(str(index)+ "--> time for 100 is: " + str(dif_100) + "\n")
            index =index+1
        ####################################################
    ###timing:
    ticks2 = time.time()
    f.close()
    f2.close()

    timeCost = str(ticks2 - ticks)
    # print (initial_list)
    return("costs: "+ timeCost)#return the time we used


def QUTimeMain(node_num,fileNameList):
    demo_list = QuickFind.QuickFindInitial(node_num)#the list contains 500 nodes, this is fixed
    f = open("timeResultQU.txt", "w")
    for k in fileNameList:
        for i in range(0,5):
            file_name= k+str(i)+".txt"
                                            #put the time value to a txt
            timeCost = QuickUnionTime(file_name,demo_list)
            demo_list = QuickFind.QuickFindInitial(node_num)#reset the demo list


            f.write("time for " + file_name +" is "+timeCost+"\n")
            print("completed for " + str(file_name))
    f.close()
    return None
##################################################################################
##################################################################################
##################################################################################
def WQUTime(txtFile,initial_list,initial_sz):
    f = open(txtFile, "r")
    node_num = f.readline()
    # print(node_num)
    f2 = open(str(txtFile)+"_100WQU.txt", "w")
    countIteration = 0
    index = 0
    ticks = time.time()
    for i in f:
        words = i.split()
        p = int(words[0])#p is first node needs to be connnected
        q = int(words[1])#q is second node needs to be connnected
        improvements.weighted_union_QU(initial_list,initial_sz, p, q)
        ############ record time for every 100 ndoes########
        countIteration = countIteration + 1
        if (countIteration % 100 == 0):
            ticks3 = time.time()
            dif_100 = ticks3 - ticks
            f2.write(str(index)+ "--> time for 100 is: " + str(dif_100) + "\n")
            index =index+1
        ####################################################
     ###timing:
    ticks2 = time.time()
    f.close()
    f2.close()

    timeCost = str(ticks2 - ticks)
    # print (initial_list)
    return("costs: "+ timeCost)#return the time we used

def WQUMain(node_num,fileNameList):
    demo_list = improvements.Weighted_QU_List_Initial(node_num)
    sz = improvements.Weighted_QU_Sz_Initial(demo_list)
    f = open("timeResultWQU.txt", "w")
    for k in fileNameList:
        for i in range(0,5):
            file_name= k+str(i)+".txt"
                                            #put the time value to a txt
            timeCost = WQUTime(file_name,demo_list,sz)

            demo_list = improvements.Weighted_QU_List_Initial(node_num)#reset the demo list
            sz = improvements.Weighted_QU_Sz_Initial(demo_list)

            f.write("time for " + file_name +" is "+timeCost+"\n")
            print("completed for " + str(file_name))
    f.close()
    return None
##################################################################################
##################################################################################
##################################################################################
def PathCompressionTime(txtFile,initial_list,initial_sz):
    f = open(txtFile, "r")
    node_num = f.readline()
    # print(node_num)
    f2 = open(str(txtFile)+"_100PC.txt", "w")
    countIteration = 0
    index = 0
    ticks = time.time()
    for i in f:
        words = i.split()
        p = int(words[0])#p is first node needs to be connnected
        q = int(words[1])#q is second node needs to be connnected
        improvements.weighted_union_QU(initial_list,initial_sz, p, q)
        ############ record time for every 100 ndoes########
        countIteration = countIteration + 1
        if (countIteration % 100 == 0):
            ticks3 = time.time()
            dif_100 = ticks3 - ticks
            f2.write(str(index)+ "--> time for 100 is: " + str(dif_100) + "\n")
            index =index+1
        ####################################################
     ###timing:
    ticks2 = time.time()
    f.close()
    f2.close()

    timeCost = str(ticks2 - ticks)
    # print (initial_list)
    return("costs: "+ timeCost)#return the time we used
def PathCompressionMain(node_num,fileNameList):
    demo_list = improvements.Weighted_QU_List_Initial(node_num)
    sz = improvements.Weighted_QU_Sz_Initial(demo_list)
    f = open("timeResultPC.txt", "w")
    for k in fileNameList:
        for i in range(0,5):
            file_name= k+str(i)+".txt"
                                            #put the time value to a txt
            timeCost = PathCompressionTime(file_name,demo_list,sz)

            demo_list = improvements.Weighted_QU_List_Initial(node_num)#reset the demo list
            sz = improvements.Weighted_QU_Sz_Initial(demo_list)

            f.write("time for " + file_name +" is "+timeCost+"\n")
            print("completed for " + str(file_name))
    f.close()
    return None
