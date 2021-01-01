import csv
a = [[], [], [], [], [], [], []]
with open('./2-1/passby_data.CSV', 'r') as f:
    reader = csv.DictReader(f)
    i = j = 0                                                   # i, j 변수 선언 및 초기화
    for row in reader:                                          # csv 파일에 저장된 데이터 수만큼 반복
        a[i].append(row)                                        # i번째 리스트에 csv 파일의 row행 추가
        j = j + 1                                               # 24개 행을 추가한 후, 다음 요일의 리스트로 이동
        if(j % 24 == 0):
            i = i + 1

x_title = ['MON', 'TUE', 'WED', 'THR', 'FRI', 'SAT', 'SUN']     # 요일 제목 저장

for i in range(0, 7):                                           # 월~일요일까지 7번 반복
    for j in range(0, len(a[i])):                               # 데이터 수만큼 반복
        print(x_title[i], '[', j, '] = ', a[i][j])              # 시간대별로 데이터 출력
