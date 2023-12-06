lines = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598..",
]

def is_valid(start, end, prev_line, curr_line, next_line):
    if (start > 0 and curr_line[start-1] != ".") or (end < len(curr_line)-1 and curr_line[end+1] != "."):
        return True 
    if prev_line and ((start > 0 and prev_line[start-1] != ".") or (end < len(prev_line)-1 and prev_line[end+1] != ".")):
        return True 
    if next_line and ((start > 0 and next_line[start-1] != ".") or (end < len(next_line)-1 and next_line[end+1] != ".")):
        return True 
    for i in range(start, end+1):
        if prev_line:
            if not prev_line[i].isdigit() and prev_line[i] != ".":
                return True
        if next_line:
            if not next_line[i].isdigit() and next_line[i] != ".":
                return True

    return False

def get_value_of_line(prev_line, curr_line, next_line):
    i = 0 
    curr_num = 0 
    ans = 0
    flag = "None"
    start = -1
    end = -1
    while i < len(curr_line):
        if curr_line[i].isdigit():
            if flag == "None":
                flag = "start"
                start = i 
                end = i
                curr_num = int(curr_line[i])
            else:
                end = i 
                curr_num = curr_num*10 + int(curr_line[i])
        else:
            if curr_num:
                if is_valid(start, end, prev_line, curr_line, next_line):
                    ans += curr_num
                
            curr_num = 0 
            flag = "None"
            start = -1 
            end = -1
        i += 1
    
    return ans

    


def main(input_file):
    prev_line = ""
    next_line = ""
    curr_line = ""
    ans = 0
    i = 0 
    with open(input_file, 'r') as file:
        while True:
            prev_line = curr_line 
            curr_line = next_line
            next_line = file.readline()

            if next_line == "" and curr_line == "":
                break 

            ans += get_value_of_line(prev_line, curr_line, next_line)

    return ans 

if __name__=="__main__":
    print(main("input.txt"))
