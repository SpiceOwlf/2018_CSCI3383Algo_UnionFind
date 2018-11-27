
import time
import random
#
#Quick_find
#
def QuickFindInitial(N):#build a list to represent trees
    initial_id = []
    for i in range(0,N):
        initial_id.append(i)
        # print(initial_id[i])
    return initial_id

def connected_QF(initial_id, p,q):#return if p and q are connected
    return (initial_id[p] == initial_id[q])

def union_QF(initial_id, p, q):#union the thing
    local_list = initial_id
    p_id = local_list[p]
    q_id = local_list[q]
    for i in range(0,len(initial_id)):
        if(local_list[i] == p_id):
            local_list[i] = q_id
    return local_list
###############################################################
#
#Quick Union
#
def find_root_QU(initial_id, i):#find the root of node i
    while (i != initial_id[i]):
        i = initial_id[i]
    return i #return the root

def connected_QU(initial_id,p,q):#find if two nodes have the same root
    return(find_root_QU(initial_id,p)==find_root_QU(initial_id,q))

def union_QU(initial_id, p, q):#list,node1,node2
    local_id_list = initial_id
    local_i = find_root_QU(initial_id,p)
    local_j = find_root_QU(initial_id,q)
    local_id_list[local_i] = local_j
    return local_id_list
###############################################################
#improvement1
#weighted quick_union

#find method is identical to quick_union

#for union, modify the union_QU to:
#link root of smaller tree to the root of the larger trees

#update the sz[] array
#initial the sz array to record the components in the root
def Weighted_QU_List_Initial(n):
    count = n
    initial_list = []
    for i in range(0, n):
        initial_list.append(i)
    return initial_list
def Weighted_QU_Size_Initial(initial_list):
    size = []
    for i in range(0,len(initial_list)):
        size.append(1)
    return size


def weighted_union_QU(initial_id,size_list, p, q):
#the initial_id will be modified after completion
    local_list = initial_id
    i = find_root_QU(initial_id,p)
    j = find_root_QU(initial_id,q)
    if(size_list[i]<size_list[j]):
        local_list[i] = j
        size_list[j] = size_list[i]+size_list[j]
    else:
        local_list[j] = i
        size_list[i] = size_list[i]+size_list[j]

    return local_list

#########################################
#improvement2: path compression
#把它压扁
def find_root_PC(initial_id, i):#find the root of node i
    while (i != initial_id[i]):
        initial_id[i]=initial_id[initial_id[i]]
        i = initial_id[i]
    return i #return the root

########################################
def QuickFindTime(txtFile,initial_list ):
    ticks = time.time()
    f = open(txtFile, "r")
    node_num = f.readline()
    # print(node_num)
    for i in f:
        words = i.split()
        p = int(words[0])#p is first node needs to be connnected
        q = int(words[1])#q is second node needs to be connnected
        union_QF(initial_list, p, q)
    ###use Quick Find to conect graph
    ###timing:
    f.close()
    ticks2 = time.time()
    timeCost = str(ticks2 - ticks)
    # print (initial_list)
    return("costs: "+ timeCost)#return the time we used
#########################################
def QuickUnionTime(txtFile,initial_list):#basic function to test quick union time
    ticks = time.time()
    f = open(txtFile, "r")
    node_num = f.readline()
    # print(node_num)
    for i in f:
        words = i.split()
        p = int(words[0])#p is first node needs to be connnected
        q = int(words[1])#q is second node needs to be connnected
        union_QU(initial_list, p, q)
    ###use Quick Find to conect graph
    ###timing:
    f.close()
    ticks2 = time.time()
    timeCost = str(ticks2 - ticks)
    # print (initial_list)
    return("costs: "+ timeCost)#return the time we used
#########################################
def WeightedQUTime():

#########################################
def Main():
    #basic funtion for QF time tests
    demo_list = QuickFindInitial(10)#the list contains 10 nodes
    f = open("timeResultQU.txt", "w")
    for i in range(0,5):
        file_name="10_100_"+str(i)+".txt"
                                                    #put the time value to a txt
        # timeCost = QuickFindTime(file_name,demo_list)
        #timeCost = QuickUnionTime(file_name,demo_list)

        f.write("time for " + file_name +" is "+timeCost+"\n")
    f.close()
########################################################################




if __name__ == "__main__":
    Main()
