#You are given with an array. For each element present in the array your task is to print the next smallest than that number. If it is not smallest print -1

#Input Description:
#You are given a number ‘n’ representing size of array. And n space separated numbers.

#Output Description:
#Print the next smallest number present in array and -1 if no smallest is present

#Sample Input :
#7
#10 7 9 3 2 1 15
#Sample Output :
#7 3 3 2 1 -1 -1

n = int(input())
z = list(map(int, input().split()))

list = []
for i in range(0,n):
    is_true = False
    for j in range(i+1,n):
        if z[j] < z[i] :
            list.append(z[j])
            is_true = True
            break
    if not is_true:
        list.append(-1)
print(*list)
