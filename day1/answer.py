import os
def getNum(string):
	first_place = 0 
	tenth_place = 0 
	i = 0 
	while i < len(string):
		if string[i].isdigit():
			tenth_place = int(string[i])
			break
		i += 1 

	i = len(string)-1
	while i > -1:
		if string[i].isdigit():
			first_place = int(string[i])
			break
		i -= 1 
	return tenth_place*10 + first_place

def main(input_filename):
	ans = 0 
	with open(input_filename, 'r') as file:
		for line in file.readlines():
			print(line)
			print(getNum(line))
			ans += getNum(line)
	return ans 

print(main('input.txt'))