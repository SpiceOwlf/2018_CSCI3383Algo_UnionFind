#
#Quick Union features
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
