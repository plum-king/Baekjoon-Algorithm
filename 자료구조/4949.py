while True:
    s = input() 
    if s == '.': 
        break 

    stack = []   
    check = True
    for i in s:
        if i == '(' or i == '[': 
            stack.append(i)
        elif i == ')': 
            if stack and stack[-1] == '(': 
                stack.pop()
            else:                         
                check = False 
                break 
        elif i == ']':  
            if stack and stack[-1] == '[': 
                stack.pop()
            else:
                check = False              
                break 

    if check and not stack: 
        print('yes')
    else:
        print('no')