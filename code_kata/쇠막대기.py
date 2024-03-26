rod_laser = input()
stack = []
count = 0

for i in range(len(rod_laser)):
    if rod_laser[i] == '(':
        stack.append(rod_laser[i])
    else:
        if rod_laser[i] == ')':
            if rod_laser[i-1] == '(':
                stack.pop()
                count += len(stack)
        else:
            count += 1

print(count)