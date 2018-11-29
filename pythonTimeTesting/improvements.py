import QuickFind
import QuickUnion
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
    #python will increse size when it needs
    #thus decrease running time
    for i in range(0, n):
        initial_list.append(i)
    return initial_list
def Weighted_QU_Sz_Initial(initial_list):
    sz = []
    for i in range(0,len(initial_list)):
        sz.append(1)
    return sz

def weighted_union_QU(initial_id,size_list, p, q):
#the initial_id will be modified after completion
    local_list = initial_id
    i = QuickUnion.find_root_QU(initial_id,p)
    j = QuickUnion.find_root_QU(initial_id,q)
    if(i != j):
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

def PathCompressionUnion(initial_id,size_list, p, q):
#the initial_id will be modified after completion
    local_list = initial_id
    i = find_root_PC(initial_id,p)#PC way to find root
    j = find_root_PC(initial_id,q)
    if(i != j):
        if(size_list[i]<size_list[j]):
            local_list[i] = j
            size_list[j] = size_list[i]+size_list[j]
        else:
            local_list[j] = i
            size_list[i] = size_list[i]+size_list[j]

    return local_list
