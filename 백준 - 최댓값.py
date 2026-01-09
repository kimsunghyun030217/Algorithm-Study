# 백준 - 최댓값(2566)
number_list = []
for i in range(9):
    number = list(map(int,input().split()))
    number_list.append(number)

max = number_list[0][0]

for i in range(0,9):
    for j in range(0,9):
        if max > number_list[i][j]:
            pass
        else:
            max = number_list[i][j]
print(max)

for i in range(9):
    for j in range(9):
        if (max == number_list[i][j]):
            print(i+1,j+1)