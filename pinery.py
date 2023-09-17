def bsearch (list , idx0, idx, val):
    if(idx<idx0):
        return None
    else:
        midval = idx0 + ((idx-idx0)//2)
    if list[midval] > val:
        return bsearch(list, idx0, midval-1,val)
    else:
        if list[midval]<val:
            return bsearch(list , midval+1 , idx,val)
        else:
            return midval     
