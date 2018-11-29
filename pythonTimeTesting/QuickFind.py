#includes features of Quick Find

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
    p_id = local_list[p]#p's id
    q_id = local_list[q]#q's id

    if p_id != q_id:#only go through for loop when
                    #they are not in the same component
        for i in range(0,len(initial_id)):
            if(local_list[i] == p_id):
                local_list[i] = q_id
    return local_list
