'''
Write a python program to read multiple lines of text input and store the input into a string.
'''
def input_reading():
	no_of_lines = int(input())
	take_input = []
	for i in range(no_of_lines):
		take_input.append(input())
	print(take_input)

def main():
    read_input = input_reading()

if __name__ == '__main__':
    main()
