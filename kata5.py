def cumulative_sum(lst):
    liston = []
    for i in range(len(lst)):
        if i>0:
            lista.append(liston[-1]+ lst[i])
        else:
            liston.append(lst[i])
    return liston

  def minMaxLengthAverage(lst):
	mini = min(lst);
	maxi = max(lst);
	lengt = len(lst);
	mid = (sum(lst))/c
	lista = [];
	lista.append(mini);
	lista.append(maxi);
	lista.append(lengt);
	lista.append(mid);
	return lista;


def sum_two_smallest_nums(lst):
  lst.sort()
  for i in range(len(lst)):
    if (lst[i] >=0):
      return lst[i]+lst[i+1]
