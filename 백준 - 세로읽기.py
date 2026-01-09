# 백준 - 세로읽기(10798)

# 핵심 - 열을 기준으로 반복(해당 열이 존재하는지부터 파악을 해야함)

answer = ''
word_list = []
for i in range(5):
    word = input("단어를 입력하세요 : ")
    word_list.append(word)

for i in word_list:
    for j in range(len(i)):
