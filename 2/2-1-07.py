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

day_title = ['MON', 'TUE', 'WED', 'THR', 'FRI', 'SAT', 'SUN']   # 요일 제목
hour_title = ['01', '02', '03', '04', '05', '06',
              '07', '08', '09', '10', '11', '12',
              '13', '14', '15', '16', '17', '18',
              '19', '20', '21', '22', '23', '24']
# 시간대별로 주간 평균 구하기
avgh = []
for j in range(0, 24):                                              # 0~23시간만큼 19~24행 반복
    day_sum = 0                                                     # 시간대별 합을 구하기 위해 0으로 초기화
    # j번째 시간대 주간 총합
    for i in range(0, 7):                                           # 일주일, 즉 7번 반복하기
        day_sum = day_sum + int(a[i][j]['num'])                     # i번째 요일에 j번째 시간대별 행인수 누적

    avgh.append(day_sum / 7)                                        # j번째 시간대별 주간 평균 구하기

# 시간대별 평균 유동 인구 출력하기
for j in range(0, 24):                                              # 24번 반복
    print('[~(0):00]:{1:4}'.format(hour_title[j], int(avgh[j])))    # 시간대별 유동 인구의 평균 출력
