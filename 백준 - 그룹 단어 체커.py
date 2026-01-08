# 백준 - 그룹 단어 체커(1316)
# 핵심 : 이 단어의 최종 상태를 저장하는 변수를 선언을 해줘야함! (is_group)
word_list = []
count = 0 
number = input("단어의 개수를 입력하시오 : ")
for i in range(0, int(number)):
    word = input("단어를 입력하시오 : ")
    word_list.append(word)
for j in word_list: #단어 하나씩 꺼냄
    is_group = True #j가 그룹단어라고 생각하고 시작

    for index in range(len(j)):
        char = j[index]
        if char in j[index+1:]: #뒤에 중복되는 단어가 나타남
            next_idx = j.find(char,index+1)
            if(next_idx - index != 1): #중복되는 단어의 index의 차이가 1이상 남\
                if_group = False
                break

        else: # 뒤에 중복되는 단어가 나타나지 않음
            pass

    if is_group:
        count += 1
    print(count)