def get_combination(input):
    curr_position = 50
    password = 0
    for input in input:
        direction = input[0]
        amount = int(input[1:])

        if direction == 'L':
            curr_position -= amount
            while curr_position < 0:
                curr_position += 100
        elif direction == 'R':
            curr_position += amount
            while curr_position > 99:
                curr_position -= 100
        if curr_position == 0:
            password += 1

    return password

def rotate(curr_position, password, direction, amount):    
    if direction == 'L':
        curr_position -= 1
        if curr_position < 0:
            curr_position = 99
        if curr_position == 0:
            password += 1
            
    elif direction == 'R':
        curr_position += 1
        if curr_position > 99:
            curr_position = 0
        if curr_position == 0:
            password += 1
    
    return curr_position, password


def get_harder_combination(input):
    curr_position = 50
    password = 0
    
    for i, instruction in enumerate(input):
        direction = instruction[0]
        amount = int(instruction[1:])
        
        for _ in range(amount):
            curr_position, password = rotate(curr_position, password, direction, 1)
            
    return password


with open('input.txt', 'r') as f:
    instructions = [line.strip() for line in f]

print(get_harder_combination(instructions))
                
