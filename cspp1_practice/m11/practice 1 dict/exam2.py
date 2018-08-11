def create_dictionary(List,n):
	d = {}
	for i in range(0,len(List),2):
		if List[i] not in d:
			d[List[i]] = List[i+1].split(" ")
		
	return d

def main():
	n = int(input())
	L = []
	for i in range(n):
		list_input = input().split(" ")
		L.extend(list_input)
	print(create_dictionary(L, n))
main()

