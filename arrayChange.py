def arrayChange(A):
    count = 0
    for i in range(1,len(A)):
        if A[i-1]>=A[i]:
            if A[i]<0 and A[i-1]>=0: #200 -2
                count += A[i-1]-A[i]+1
            elif A[i]<0 and A[i-1]<0: #-2 -200
                count += A[i-1]+1-A[i]
            else: #200 1 
                count += A[i-1]-A[i]+1
            A[i]=A[i-1]+1  
    return count
        

# print(arrayChange([-200,1,1,1]))
# [-28943, -29728, -24726, -15090, -2555, -9551, -11025, 36442, -23240, -46093, 48516, 44580, -21573, 39172, -38017, -19354, -13460, 38212, -35646, -22288, 36832, -33115, 39055, -15935, -19300, -10419, -18548, 21742, -32032, 27988, -45323, 27454, -5683, -14209, -4168, 51188, 45552, 9899, 49241, -25939, -8344, -25788, 6808, 6931, 6145, -30802, -518, -42362]
print('output',arrayChange([-28943, -29728, -24726, -15090, -2555, -9551, -11025, 36442, -23240, -46093, 48516, 44580, -21573, 39172, -38017, -19354, -13460, 38212, -35646, -22288, 36832, -33115, 39055, -15935, -19300, -10419, -18548, 21742, -32032, 27988, -45323, 27454, -5683, -14209, -4168, 51188, 45552, 9899, 49241, -25939, -8344, -25788, 6808, 6931, 6145, -30802, -518, -42362]))
print('expected',2020705)