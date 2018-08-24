def read_input():
	input_1=[]
	for i in range(3):
		input_1.append(input().split(" "))
	return input_1





def check_winner(game_input):
	pass



def main():
	game_input = read_input()
	print(game_input)
	winner = check_winner(game_input)


if __name__ == '__main__':
    main()