# 백준 - 다이얼 문제(5622)

Alphabet = input()

Alphabet_list = list(Alphabet)

answer = 0

Dial = [['A','B','C'],['D','E','F'],['G','H','I'],['J','K','L'],['M','N','O'],['P','Q','R','S'],['T','U','V'],['W','X','Y','Z']]

for i in Alphabet_list:
    for j in Dial:
        for k in j:
            if(i == k):
                answer += Dial.index(j) + 3
print(answer)