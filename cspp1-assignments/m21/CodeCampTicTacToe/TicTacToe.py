def read_input():
	input_1=[]
	for i in range(3):
		input_1.append(input().split(" "))
	return(input_1)
	
def one_list(game_input):
	one_list = []
	for i in range(len(game_input)):
		for j in range(len(game_input[i])):
			one_list.append(game_input[i][j])
	print(one_list)





def check_winner(game_input):
	pass



def main():
	game_input = read_input()
	winner = check_winner(game_input)
	print(one_list(game_input))


if __name__ == '__main__':
    main()