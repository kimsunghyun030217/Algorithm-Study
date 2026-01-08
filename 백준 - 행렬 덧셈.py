
# 백준 - 행렬 덧셈(2738)
# 내가 헷갈린 포인트 : row_A/B/result를 N안이 아니라 M안에 넣었음 -> M안에 넣으니까 자꾸 반복할때마다 리스트가 생겨서 형태가 이상해짐
A = input().split()
N = int(A[0])
M = int(A[1])

Matrix_A = []
Matrix_B = []
Matrix_result = []

# 행렬 A 입력
for i in range(N):
    row_A = []
    row_A_number = input().split()

    for x in row_A_number:
        row_A.append(int(x))
    Matrix_A.append(row_A)

    # 더 간단한 map(int,input().split()) 이게 있음
    # map함수는 리스트이 모든 요소에 함수 하나를 '일괄 적용'해주는 내장 함수
    # map함수의 기본 형태는 -> map(함수, 반복가능한 데이터)

 
# 행렬 B 입력

for i in range(N):
    row_B = []
    row_B_number = input().split()
    
    for x in row_B_number:
        row_B.append(int(x))
    Matrix_B.append(row_B)

# 행렬 A+B 계산

for i in range(N):
    row_number = []
    for j in range(M):
        row_number.append(Matrix_A[i][j] + Matrix_B[i][j])
    Matrix_result.append(row_number)

# 출력 형식 

for i in range(N):
    for j in range(M):
        print(Matrix_result[i][j], end=" ")
    print()