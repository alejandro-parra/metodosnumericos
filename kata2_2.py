def filter_list(lst):
	tmpLst = []
	for i in lst:
		if type(i) is int:
			tmpLst.append(i)
			
	return tmpLst
