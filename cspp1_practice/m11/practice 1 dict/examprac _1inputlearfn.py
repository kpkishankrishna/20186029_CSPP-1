def create_dictionary(List,n):
	d = {}
	for i in range(0,len(List),2):
		if int(List[i]) not in d:
			d[int(List[i])] = int(List[i+1])
		else:
			d[int(List[i])] += int(List[i+1])
	return d

def main():
	n = int(input())
	L = []
	for i in range(n):
		list_input = input().split(" ")
		L.extend(list_input)
	print(create_dictionary(L, n))
main()

