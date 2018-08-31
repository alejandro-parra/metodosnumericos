def cumulative_sum(lst):
    liston = []
    for i in range(len(lst)):
        if i>0:
            lista.append(liston[-1]+ lst[i])
        else:
            liston.append(lst[i])
    return liston
