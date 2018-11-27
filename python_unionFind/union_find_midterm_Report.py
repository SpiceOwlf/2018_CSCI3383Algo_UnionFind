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

def connected_QU(initial_id,p,q):
    return(find_root_QU(initial_id,p)==find_root_QU(initial_id,q))
    #find if two nodes have the same root
def union_QU(initial_id, p, q):#not tested yet
    local_id_list = initial_id
    local_i = find_root_QU(initial_id,p)
    local_j = find_root_QU(initial_id,q)
    local_id_list[local_i] = local_j
    return local_id_list
###############################################################
#improvement1
#weighted quick_union
#

#find method is identical to quick_union

#for union, modify the union_QU to:
#link root of smaller tree to the root of the larger trees

#update the sz[] array

#initial the sz array to record the components in the root
def Weighted_QU_List_Initial(n):
    count = n
    initial_list = []
    for i in range(0, n):
        parent.append(i)
    return initial_list
def Weighted_QU_Size_Initial(initial_list):
    size = []
    for i in range(0,len(initial_list)):
        size.append(1)
    return size


def weighted_union_QU(initial_id,size_list, p, q):#not tested yet
    local_list = initial_id
    local_i = find_root_QU(initial_id,p)
    local_j = find_root_QU(initial_id,q)
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

#########################################
def Main():
    demo_list = QuickFindInitial(10)

    demo_list = union_QF(demo_list, 3,4)
    demo_list = union_QF(demo_list, 4,5)

    # for i in range(0,10):
    #     print (find_root_QU(demo_list, i))

    # for i in range(0,9):
    #     print(connected_QU(demo_list,i,i+1))


    # print(demo_list)
    print(connected_QF(demo_list, 1,3))
    print(connected_QF(demo_list, 4,3))


if __name__ == "__main__":
	Main()
