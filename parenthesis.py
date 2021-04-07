def reverseInParentheses(inputString):
    pList = []
    flag = False
    pStr = ''
    for i in inputString:
        if i==')':
            if flag:
                pList.append(pStr)
        if i == '(':
            if flag:
                pStr += i
            else:
                flag= True
        if flag:
            pStr+=i



reverseInParentheses('foo(bar)123')